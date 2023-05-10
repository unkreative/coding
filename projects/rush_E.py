import PIL
from PIL import Image
image = '/Users/lousergonne/Downloads/349-3497431_ode-to-joy-easy-piano-sheet-music-pdf.png'

with Image.open(image).convert('RGB') as pim:
    pim.show()
    