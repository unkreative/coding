<?php

/*
 * Copyright (c) 2021 Heimrich & Hannot GmbH
 *
 * @license LGPL-3.0-or-later
 */

namespace HeimrichHannot\PdfCreator\Concrete;

use Dompdf\Adapter\CPDF;
use Dompdf\Dompdf;
use Dompdf\Options;
use HeimrichHannot\PdfCreator\AbstractPdfCreator;
use HeimrichHannot\PdfCreator\BeforeCreateLibraryInstanceCallback;
use HeimrichHannot\PdfCreator\BeforeOutputPdfCallback;
use HeimrichHannot\PdfCreator\Exception\MissingDependenciesException;
use setasign\Fpdi\Tcpdf\Fpdi;
use Symfony\Component\Filesystem\Filesystem;

class DompdfCreator extends AbstractPdfCreator
{
    public static function getType(): string
    {
        return 'dompdf';
    }

    public static function isUsable(bool $triggerExeption = false): bool
    {
        if (!class_exists('Dompdf\Dompdf')) {
            if ($triggerExeption) {
                throw new MissingDependenciesException(static::getType(), ['"dompdf/dompdf": "^1.0"']);
            }

            return false;
        }

        return true;
    }

    public function render()
    {
        static::isUsable(true);

        $options = new Options();
        $options->setIsRemoteEnabled(true);

        if ($this->getBeforeCreateInstanceCallback()) {
            /** @var BeforeCreateLibraryInstanceCallback $result */
            $result = \call_user_func(
                $this->getBeforeCreateInstanceCallback(),
                new BeforeCreateLibraryInstanceCallback(static::getType(), ['options' => $options])
            );

            if ($result && isset($result->getConstructorParameters()['options'])) {
                $options = $result->getConstructorParameters()['options'];
            }
        }

        $dompdf = new Dompdf($options);

        if ($this->getHtmlContent()) {
            $dompdf->loadHtml($this->getHtmlContent());
        }

        $orientation = static::ORIENTATION_PORTRAIT;

        if ($this->getOrientation()) {
            switch ($this->getOrientation()) {
                case static::ORIENTATION_LANDSCAPE:
                    $orientation = $this->getOrientation();

                    break;
            }
        }

        $format = 'A4';

        if ($this->getFormat()) {
            if (\is_string($this->getFormat()) && isset(CPDF::$PAPER_SIZES[mb_strtolower($this->getFormat())])) {
                $format = $this->getFormat();
            } elseif (\is_array($this->getFormat())) {
                $width = ($this->getFormat()[0] / 25.4) * 72;
                $height = ($this->getFormat()[1] / 25.4) * 72;
                $format = [0, 0, $width, $height];
            }
        }

        $dompdf->setPaper($format, $orientation);

        $filename = $this->getFilename();
        $renderOptions = [];

        switch ($this->getOutputMode()) {
            case static::OUTPUT_MODE_DOWNLOAD:
                $renderOptions = ['Attachment' => 1];

                break;

            case static::OUTPUT_MODE_INLINE:
                $renderOptions = ['Attachment' => 0];

                break;
        }

        if ($this->getBeforeOutputPdfCallback()) {
            /** @var BeforeOutputPdfCallback $result */
            $result = \call_user_func($this->getBeforeOutputPdfCallback(), new BeforeOutputPdfCallback(static::getType(), $dompdf, [
                'filename' => $filename,
                'options' => $renderOptions,
            ]));

            if ($result) {
                if (isset($result->getOutputParameters()['filename']) && \is_string($result->getOutputParameters()['filename'])) {
                    $filename = $result->getOutputParameters()['filename'];
                }

                if (isset($result->getOutputParameters()['options']) && \is_array($result->getOutputParameters()['options'])) {
                    $renderOptions = $result->getOutputParameters()['options'];
                }
            }
        }

        $dompdf->render();

        if ($this->getTemplateFilePath() && class_exists('setasign\Fpdi\Tcpdf\Fpdi')) {
            if (file_exists($this->getTemplateFilePath())) {
                return $this->applyMasterTemplate($filename, $dompdf);
            }
            trigger_error('Pdf template does not exist.', E_USER_NOTICE);
        }

        switch ($this->getOutputMode()) {
            default:
            case static::OUTPUT_MODE_DOWNLOAD:
            case static::OUTPUT_MODE_INLINE:
                $dompdf->stream($filename, $renderOptions);

                exit;

            case static::OUTPUT_MODE_STRING:
                return $dompdf->output($renderOptions);

            case static::OUTPUT_MODE_FILE:
                // @ToDo (https://ourcodeworld.com/articles/read/799/how-to-create-a-pdf-from-html-in-symfony-4-using-dompdf)
                // should then also be covered in applyMasterTemplate
        }
    }

    public function getSupportedOutputModes(): array
    {
        return [
            self::OUTPUT_MODE_INLINE,
            self::OUTPUT_MODE_DOWNLOAD,
            self::OUTPUT_MODE_STRING,
        ];
    }

    public function supports(): array
    {
        $support = [];

        if (class_exists('setasign\Fpdi\Tcpdf\Fpdi')) {
            $support[] = static::SUPPORT_MASTERTEMPLATE;
        }

        return $support;
    }

    /**
     * @param $filename
     *
     * @throws \setasign\Fpdi\PdfParser\CrossReference\CrossReferenceException
     * @throws \setasign\Fpdi\PdfParser\Filter\FilterException
     * @throws \setasign\Fpdi\PdfParser\PdfParserException
     * @throws \setasign\Fpdi\PdfParser\Type\PdfTypeException
     * @throws \setasign\Fpdi\PdfReader\PdfReaderException
     */
    protected function applyMasterTemplate($filename, Dompdf $dompdf)
    {
        $filesystem = new Filesystem();

        while (true) {
            $tmpFilename = $this->getTempPath().'/dompdf/'.$filename.'_'.uniqid().'.pdf';

            if (!$filesystem->exists($tmpFilename)) {
                break;
            }
        }
        $filesystem->dumpFile($tmpFilename, $dompdf->output());
        $pdf = new Fpdi();
        $pdf->setPrintHeader(false);
        $pdf->setSourceFile($this->getTemplateFilePath());
        $masterTemplate = $pdf->importPage(1);
        $pageCount = $pdf->setSourceFile($tmpFilename);

        for ($i = 1; $i <= $pageCount; ++$i) {
            $pdf->AddPage();
            $currentPage = $pdf->importPage($i);
            $pdf->useTemplate($masterTemplate);
            $pdf->useTemplate($currentPage);
        }

        switch ($this->getOutputMode()) {
            case static::OUTPUT_MODE_STRING:
                $outputMode = 'S';

                break;

//            case static::OUTPUT_MODE_FILE:
//                if ($folder = $this->getFolder() && $this->getFilename()) {
//                    $filename = rtrim($folder, \DIRECTORY_SEPARATOR).\DIRECTORY_SEPARATOR.$filename;
//                }
//
//                $outputMode = 'F';
//
//                break;

            case static::OUTPUT_MODE_DOWNLOAD:
                $outputMode = 'D';

                break;

            default:
            case static::OUTPUT_MODE_INLINE:
                $outputMode = 'I';

                break;
        }
        $filesystem->remove($tmpFilename);

        return $pdf->Output($this->getFilename(), $outputMode);
    }
}