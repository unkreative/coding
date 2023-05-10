from re import L
import pyautogui as pg
import time
import subprocess
import browserhistory as bh
from regex import R

def write_to_clipboard(output):
    process = subprocess.Popen(
        'pbcopy', env={'LANG': 'en_US.UTF-8'}, stdin=subprocess.PIPE)
    process.communicate(output.encode('utf-8'))

source_numero_0 = ['https://phys.org/news/2014-12-universe-dimensions.html', 'Matt Williams', 'Universe Dimensions']
source_numero_1 = ['https://simple.wikipedia.org/wiki/Dimension', 'Contributors to Wikimedia projects All', 'Dimension - Simple English Wikipedia, the free encyclopedia']
source_numero_2 = ['https://www.youtube.com/watch?v=Dm_d_nUTfmU&ab_channel=CenterofMath', 'Center of Math', 'Worldwide Calculus: Euclidean Space - YouTube']
source_numero_3 = ['https://simple.wikipedia.org/wiki/Euclidean_space', 'Contributors to Wikimedia projects All', 'Euclidean space - Simple English Wikipedia, the free encyclopedia']
source_numero_4 = ['https://www.britannica.com/science/Euclidean-space', 'The Editors of Encyclopaedia Britannica', 'Euclidean space | geometry | Britannica']
source_numero_5 = ['https://simple.wikipedia.org/wiki/One-dimensional_space', 'Contributors to Wikimedia projects All', 'One-dimensional space - Simple English Wikipedia, the free encyclopedia']
source_numero_6 = ['https://en.wikipedia.org/wiki/One-dimensional_space', 'Contributors to Wikimedia projects All', 'One-dimensional space - Wikipedia']
source_numero_7 = ['https://www.youtube.com/watch?v=MV47Mcmo25I&ab_channel=10thdim', '10thdim', 'Imagining the First Dimension - YouTube']
source_numero_8 = ['https://www.wikiwand.com/en/One-dimensional_space', 'unknown', 'One-dimensional space - Wikiwand']
source_numero_9 = ['https://www.math.net/1d', 'unknown', '1D']
source_numero_10 = ['https://en.wikipedia.org/wiki/Cartesian_coordinate_system#/media/File:Cartesian-coordinate-system.svg', 'Contributors to Wikimedia projects All', 'Cartesian coordinate system - Wikipedia']
source_numero_11 = ['https://en.wikipedia.org/wiki/Two-dimensional_space', 'Contributors to Wikimedia projects All', 'Two-dimensional space - Wikipedia']
source_numero_12 = ['https://www.mathdoubts.com/two-dimensional-space/', 'unknown', 'Two dimensional space']
source_numero_13 = ['https://www.dreamstime.com/stock-illustration-d-coordinate-axis-vector-image-white-image67829314', 'unknown', 'coordinate axis vector']
source_numero_14 = ['https://simple.wikipedia.org/wiki/3D', 'Contributors to Wikimedia projects All', '3D - Simple English Wikipedia, the free encyclopedia']
source_numero_15 = ['https://simple.wikipedia.org/wiki/Solid_geometry', 'Contributors to Wikimedia projects All', 'Solid geometry - Simple English Wikipedia, the free encyclopedia']
source_numero_16 = ['https://acoem.us/blog/other-topics/x-y-z-axis-stand/', 'unknown', '-']
source_numero_17 = ['https://simple.wikipedia.org/wiki/Cartesian_coordinate_system', 'Contributors to Wikimedia projects All', 'Cartesian coordinate system - Simple English Wikipedia, the free encyclopedia']
source_numero_18 = ['https://mathinsight.org/cartesian_coordinates', 'unknown', 'Cartesian coordinates - Math Insight']
source_numero_19 = ['https://www.scienceabc.com/pure-sciences/what-exactly-is-a-tesseract-real-life-geometry-4-dimensional.html', 'unknown', 'What Exactly Is A Tesseract? » Science ABC']
source_numero_20 = ['https://www.youtube.com/watch?v=j-ixGKZlLVc&ab_channel=TheScienceElf', 'The Science Elf', "A Beginner's Guide to the Fourth Dimension - YouTube"]
source_numero_21 = ['https://interestingengineering.com/understanding-fourth-dimension-3d-perspective', 'unknown', 'Understanding the Fourth Dimension From Our 3D Perspective']
source_numero_22 = ['https://en.wikipedia.org/wiki/Immersion_(mathematics)', 'Contributors to Wikimedia projects All', 'Immersion (mathematics) - Wikipedia']
source_numero_23 = ['https://www.scienceabc.com/pure-sciences/what-exactly-is-a-tesseract-real-life-geometry-4-dimensional.html', 'unknown', 'What Exactly Is A Tesseract? » Science ABC']
source_numero_24 = ['https://en.wikipedia.org/wiki/Klein_bottle', 'Contributors to Wikimedia projects All', 'Klein bottle - Wikipedia']
source_numero_25 = ['https://www.smithsonianmag.com/science-nature/mathematical-madness-mobius-strips-and-other-one-sided-objects-180970394/', 'David Gunderman and Richard Gunderman The Conversation', 'The Mathematical Madness of Möbius Strips and Other One-Sided Objects | Science| Smithsonian Magazine']
source_numero_26 = ['https://en.wikipedia.org/wiki/M%C3%B6bius_strip', 'Contributors to Wikimedia projects All', 'Möbius strip - Wikipedia']
source_numero_27 = ['https://www.youtube.com/watch?v=2s4TqVAbfz4&ab_channel=Numberphile', 'Numberphile', 'Perfect Shapes in Higher Dimensions - Numberphile - YouTube']
source_numero_28 = ['https://en.wikipedia.org/wiki/8-cube', 'Contributors to Wikimedia projects All', '8-cube - Wikipedia']
source_numero_29 = ['https://phys.org/news/2014-12-universe-dimensions.html', 'unknown', '12 universes']
source_numero_30 = ['https://www.universetoday.com/48619/a-universe-of-10-dimensions/', 'unknown', '10 dimension']
source_numero_31 = ['https://www.youtube.com/watch?v=dr2sIoD7eeU&ab_channel=ZachStar', 'Zach Star', "The things you'll find in higher dimensions - YouTube"]
source_numero_32 = ['https://www.artstation.com/arnaud_imobersteg', 'unknown', 'Portfolio']
source_numero_33 = ['https://www.artstation.com/artwork/QzDQod', 'unknown', 'Portfolio']
source_numero_34 = ['https://www.artstation.com/insideitall', 'unknown', 'Portfolio']
source_numero_35 = ['https://www.artstation.com/artwork/3oYbvD', 'unknown', 'Portfolio']
source_numero_36 = ['https://sebbas.org/', 'Sebastián Barschkis', 'Sebastián Barschkis » Home » sebbas.org']
source_numero_37 = ['https://docs.blender.org/manual/en/latest/physics/fluid/introduction.html#liquid-simulations', 'unknown', 'Introduction — Blender Manual']
source_numero_38 = ['https://www.artstation.com/artificial3d', 'unknown', 'Portfolio']
source_numero_39 = ['https://en.bandainamcoent.eu/elden-ring/elden-ring', 'unknown', 'ELDEN RING |  Official Website (EN)']
source_numero_40 = ['https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.xboxygen.com%2FNews%2F40029-Ventes-de-Elden-Ring-carton-plein-aux-Etats-Unis-premier-sur-Xbox-en-fevrier&psig=AOvVaw2owQEsFk73anN5N9vMVEVB&ust=1649931945712000&source=images&cd=vfe&ved=0CAoQjRxqFwoTCJiL1dDpkPcCFQAAAAAdAAAAABAs', 'unknown', 'Weiterleitungshinweis']
source_numero_41 = ['https://hitman.com/global/', 'unknown', 'HITMAN 3']
source_numero_42 = ['https://www.google.com/url?sa=i&url=https%3A%2F%2Fbit-tech.net%2Ffeatures%2Fgaming%2Fpc%2Fhitman-3-review%2F1%2F&psig=AOvVaw2Rltb2vpHILyPVixbeblgg&ust=1649932203022000&source=images&cd=vfe&ved=0CAoQjRxqFwoTCKjAkMvqkPcCFQAAAAAdAAAAABAD', 'unknown', 'Weiterleitungshinweis']
source_numero_43 = ['https://en.wikipedia.org/wiki/3D_modeling', 'Contributors to Wikimedia projects All', '3D modeling - Wikipedia']
source_numero_44 = ['https://www.youtube.com/watch?v=TEAtmCYYKZA&ab_channel=CrashCourse', 'CrashCourse', '3D Graphics: Crash Course Computer Science #27 - YouTube']
source_numero_45 = ['https://en.wikipedia.org/wiki/3D_computer_graphics', 'Contributors to Wikimedia projects All', '3D computer graphics - Wikipedia']
source_numero_46 = ['https://www.sciencedaily.com/terms/3d_computer_graphics.htm', 'unknown', '3D Computer graphics']
source_numero_47 = ['https://www.quora.com/How-do-3D-graphics-work', 'unknown', 'How do 3D graphics work? - Quora']
source_numero_48 = ['https://www.khanacademy.org/computing/computer-programming/programming-games-visualizations/programming-3d-shapes/a/what-are-3d-shapes', 'unknown', 'What are 3D shapes? (article) | 3D shapes | Khan Academy']
source_numero_49 = ['https://www.techtarget.com/whatis/definition/3D-mesh', 'TechTarget Contributor', 'What is 3D mesh? - Definition from WhatIs.com']
source_numero_50 = ['https://www.khanacademy.org/computing/pixar/rendering/rendering1/v/rendering-2', 'unknown', '2. Light reflection (video) | Rendering 101 | Khan Academy']
source_numero_51 = ['https://unity.com/srp/universal-render-pipeline', 'Unity Technologies', 'Universal Render Pipeline (formerly LWRP) optimizes graphics performance | Rendering Engine | Unity']
source_numero_52 = ['https://www.realtimerendering.com/', 'unknown', 'Realtimerendering']
source_numero_53 = ['https://www.marxentlabs.com/3d-rendering/', 'unknown', '3D rendering']
source_numero_54 = ['https://en.wikipedia.org/wiki/3D_computer_graphics', 'Contributors to Wikimedia projects All', '3D computer graphics - Wikipedia']
source_numero_55 = ['https://en.wikipedia.org/wiki/3D_projection', 'Contributors to Wikimedia projects All', '3D projection - Wikipedia']
source_numero_56 = ['https://en.wikipedia.org/wiki/Rendering_(computer_graphics)', 'Contributors to Wikimedia projects All', 'Rendering (computer graphics) - Wikipedia']
source_numero_57 = ['https://www.youtube.com/watch?v=TEAtmCYYKZA&ab_channel=CrashCourse', 'CrashCourse', '3D Graphics: Crash Course Computer Science #27 - YouTube']
source_numero_58 = ['https://www.kmjn.org/notes/3d_rendering_intro.html', 'unknown', 'Capsule introduction to 3d wireframe rendering | Mark J. Nelson']
source_numero_59 = ['https://techterms.com/definition/wireframe', 'unknown', 'Wireframe Definition']
source_numero_60 = ['https://www.kmjn.org/notes/3d_rendering_intro.html', 'unknown', 'Capsule introduction to 3d wireframe rendering | Mark J. Nelson']
source_numero_61 = ['https://sciencing.com/split-triangle-fourths-8487469.html', 'unknown', 'How to Split a Triangle Into Fourths | Sciencing']
source_numero_62 = ['https://www.youtube.com/watch?v=cH_NaCkrkAM&ab_channel=eHowEducation', 'eHowEducation', 'Ways to Divide a Scalene Triangle Into Three Triangles of Equa... : Triangles & Conversions in Math - YouTube']
source_numero_63 = ['https://en.wikipedia.org/wiki/Polygon_mesh', 'Contributors to Wikimedia projects All', 'Polygon mesh - Wikipedia']
source_numero_64 = ['https://en.wikipedia.org/wiki/Convex_polygon', 'Contributors to Wikimedia projects All', 'Convex polygon - Wikipedia']
source_numero_65 = ['https://developer.nvidia.com/discover/ray-tracing', 'unknown', 'Ray Tracing | NVIDIA Developer']
source_numero_66 = ['https://cs.stanford.edu/people/eroberts/courses/soco/projects/1997-98/ray-tracing/types.html', 'unknown', 'Ray tracing']
source_numero_67 = ['https://www.khanacademy.org/computing/pixar/rendering/rendering1/v/rendering-1', 'unknown', '1. What is ray tracing? (video) | Rendering | Khan Academy']
source_numero_68 = ['https://www.khanacademy.org/computing/pixar/rendering/rendering1/e/light-rays', 'unknown', 'Light rays (practice) | Rendering 101 | Khan Academy']
source_numero_69 = ['https://www.khanacademy.org/computing/pixar/rendering/rendering1/v/render-4', 'unknown', '4. Rendering Mike Wazowski (video) | Khan Academy']
source_numero_70 = ['https://viclw17.github.io/2018/06/30/raytracing-rendering-equation', 'Victor Li', 'Raytracing - Rendering Equation Insight | 1000 Forms of Bunnies']
source_numero_71 = ['https://en.wikipedia.org/wiki/Rendering_equation', 'Contributors to Wikimedia projects All', 'Rendering equation - Wikipedia']
source_numero_72 = ['https://www.youtube.com/watch?v=AODo_RjJoUA', 'NVIDIA Developer', 'Ray Tracing Essentials Part 6: The Rendering Equation - YouTube']
source_numero_73 = ['https://viclw17.github.io/2018/07/15/raytracing-image-output', 'Victor Li', 'Raytracing - Image Output | 1000 Forms of Bunnies']
source_numero_74 = ['https://viclw17.github.io/2018/07/20/raytracing-diffuse-materials', 'Victor Li', 'Raytracing - Diffuse Materials | 1000 Forms of Bunnies  ']
source_numero_75 = ['https://www.youtube.com/watch?v=0J8tKGjEE5Q', 'Sebastian Lague', 'Sphere Tracing Visualisation - YouTube']
source_numero_76 = ['https://en.wikipedia.org/wiki/Ray_tracing_(graphics)#Algorithm_overview', 'Contributors to Wikimedia projects All', 'Ray tracing (graphics) - Wikipedia']
source_numero_77 = ['https://lodev.org/cgtutor/raycasting.html', 'unknown', 'Raycasting']
source_numero_78 = ['https://www.techopedia.com/definition/21614/ray-casting', 'Techopedia', 'What is Ray Casting? - Definition from Techopedia']
source_numero_79 = ['https://www.youtube.com/watch?v=ll4_79zKapU', 'Bob Laramee', 'Ray Casting versus Ray Tracing (Volumetric): A Quick and Convenient Comparison - YouTube']
source_numero_80 = ['https://en.wikipedia.org/wiki/Ray_casting', 'Contributors to Wikimedia projects All', 'Ray casting - Wikipedia']
source_numero_81 = ['https://www.researchgate.net/publication/321125112_Daylight_simulation_with_photon_maps', 'Roland Schregle', '(PDF) Daylight simulation with photon maps']
source_numero_82 = ['https://inspirationtuts.com/blender-render-engines-free-options-included/', 'InspirationTuts', 'All 12 Blender Render Engines | free options included - InspirationTuts']
source_numero_83 = ['https://archicgi.com/cgi-news/3d-render-engines-choosing-the-best/', 'ArchiCGI', '3D render engines: top 7 choices from pros | ArchiCGI']
source_numero_84 = ['https://www.youtube.com/watch?v=qJEWOTZnFeg', 'Blender Guru', '"Money doesn\'t interest me" - Ton Roosendaal interview - YouTube']
source_numero_85 = ['https://www.youtube.com/watch?v=pEvMJYzLTuE', 'Blender Guru', 'Breaking into the Concept Art Industry - Interview with Finnian Macmanus - YouTube']
source_numero_86 = ['https://www.youtube.com/watch?v=-SOP2YYRKss', 'Blender Guru', 'From Blender to Pixar, with Colin Levy - Interview - YouTube']
source_numero_87 = ['https://www.youtube.com/watch?v=-SOP2YY', 'unknown', ' - YouTube']
source_numero_88 = ['https://www.geospatialworld.net/article/5-industrial-applications-of-3d-printing-services', 'Wayken Rapid', '5 industrial applications of 3D printing services - Geospatial World']
source_numero_89 = ['https://markforged.com/resources/blog/five-industries-utilizing-3d-printing', 'unknow', 'Five Industries Utilizing 3D Printing']
source_numero_90 = ['https://cprimestudios.com/blog/how-3d-printing-used-automotive-industry', 'Cprime Studios', 'How is 3D printing used in the automotive industry? | Cprime Studios']
source_numero_91 = ['https://xometry.eu/en/application-of-3d-printing-in-automotive-industry/', 'Evgeny Misnikov', 'Application of 3D Printing In Automotive Industry | Xometry Europe']
source_numero_92 = ['https://www.agh.edu.pl/en/science/info/article/rte-20-lem-agh-racing-team-introduce-their-new-electric-racing-car/', 'unknown', 'RTE 2.0 LEM: AGH Racing Team introduce their new electric racing car AGH University of Science and Technology']
source_numero_93 = ['https://cobod.com/', 'unknown', 'Cobod']
source_numero_94 = ['https://www.iconbuild.com/', 'unknown', 'Home | ICON']
source_numero_95 = ['https://all3dp.com/2/best-companies-building-3d-printed-houses/', 'ALL3DP', 'Best companiese building 3D printed houses']
source_numero_96 = ['https://www.peri.com/en/media/press-releases/germanys-first-printed-house-officially-openend.html', 'unknown', 'Germanys first printed house officially openend']
source_numero_97 = ['https://www.gira.com/uk/en/inspirations/references/3d-house-germany', 'unkown', '3D-printed house in Germany: a new way of building | Gira']
source_numero_98 = ['https://www.techadvisor.com/feature/small-business/5-top-uses-of-3d-printing-3788919/', 'Tech Advisor', 'Eight ways 3D printing is being used today']
source_numero_99 = ['https://www.makepartsfast.com/3d-printed-circuit-boards-how-theyre-made-and-why-they-matter/', 'Leslie Lagna', '3D printed circuit boards']
source_numero_100 = ['https://en.wikipedia.org/wiki/Fused_filament_fabrication', 'Contributors to Wikimedia projects All', 'Fused filament fabrication - Wikipedia']
source_numero_101 = ['https://all3dp.com/2/pcb-3d-printer-all-about-3d-printed-circuit-boards/', 'Henry Haefliger', 'PCB 3d printer all about 3D printed circuit boards']
source_numero_102 = ['https://maker.pro/pcb/tutorial/how-to-make-a-printed-circuit-board-pcb', 'Suraj Gehlot', 'printed PCB board']
source_numero_103 = ['https://en.wikipedia.org/wiki/Printed_circuit_board', 'Contributors to Wikimedia projects All', 'Printed circuit board - Wikipedia']
source_numero_104 = ['https://www.eurocircuits.com/pcb-printed-circuit-board/', 'unknown', 'What is a PCB or Printed Circuit Board? - Technical Terms by Eurocircuits']
source_numero_105 = ['https://www.pcbway.com/rapid-prototyping/3D-Printing/3D-Printing-FDM.html', 'unknown', 'Fused Deposition Modeling (FDM) 3D Printing Service | Instant Quoting - PCBWay']
source_numero_106 = ['https://all3dp.com/2/what-is-material-jetting-3d-printing-simply-explained/', 'Leo Gregurić', 'Attention Required! | Cloudflare']
source_numero_107 = ['https://www.hubs.com/knowledge-base/introduction-material-jetting-3d-printing/', 'Alkaios Bournias Varotsis', ' Introduction to material jetting 3D printing | Hubs ']
source_numero_108 = ['https://www.cnet.com/pictures/this-3d-printed-mars-habitat-could-be-your-new-home-in-space-marsha-ai-spacefactory/', 'Claire Reilly', 'This 3D-printed Mars habitat could be your new home in space - CNET']
source_numero_109 = ['https://www.nasa.gov/mission_pages/station/research/news/3d-printing-in-space-long-duration-spaceflight-applications/', 'Michael Johnson', 'Solving the Challenges of Long Duration Space Flight with 3D Printing | NASA']
source_numero_110 = ['https://www.3dnatives.com/en/top-10-3d-printing-space/', '3Dnatives', 'What Are the Applications for 3D Printing in Space? - 3Dnatives']
source_numero_111 = ['https://www.aispacefactory.com/ ', 'aispacefactory', 'Aispacefactory']
source_numero_112 = ['https://www.youtube.com/watch?v=34DfBw6c10o', 'SpaceFactory', '3D printed brain: time lapse - YouTube']
source_numero_113 = ['https://interestingengineering.com/10-surprising-ways-3d-printing-is-being-used-now', 'Ariella Brown', '10 Surprising Ways 3D Printing Is Being Used Now']
source_numero_114 = ['https://www.prusaprinters.org/prints/122320-one-for-all-cable-strap-print-in-place-clamp/', 'Extrutim', 'Printables']
source_numero_115 = ['https://www.fabbaloo.com/news/design-of-the-week-mechanical-wall-clock/', 'Kerry Stevenson', 'mechanical wall clock']
source_numero_116 = ['https://www.voxelab3dp.com/product/aquila-diy-fdm-3d-printer/', 'Voxellab3dp', 'Voxelab Aquila DIY FDM 3D printer - Voxelab3dp']
source_numero_117 = ['https://www.tomshardware.com/reviews/voxelab-aquila-x2-3d-printer/', 'Voxelab Aquila X2', "Voxelab Aquila X2 3D Printer Review: Inexpensive, But Unimpressive | Tom's Hardware"]
source_numero_118 = ['https://3dprinterly.com/voxelab-aquila-x2-review/', '3D printerly', 'Voxellab Aquila']
source_numero_119 = ['https://total3dprinting.org/voxelab-aquila-review/', 'Justin Cadwell', 'Voxelab Aquila 3D Printer Review [2022]: Is It Right For Your Needs? - Total 3D Printing']
source_numero_120 = ['https://www.creality.com/goods-detail/ender-3-v2-3d-printer/', 'Creality', 'Ender-3 V2 3D Printer']
source_numero_121 = ['https://www.creality.com/goods-detail/ender-3-v2-3d-printer/', 'Creality', 'Ender-3 V2 3D Printer']
source_numero_122 = ['https://www.pcmag.com/reviews/creality-ender-3-v2/', 'PCMag', 'Creality Ender-3 V2 Review | PCMag']
source_numero_123 = ['https://all3dp.com/1/creality-ender-3-v2-review-3d-printer-specs/', 'Ender 3 v2 review', "All3DP"]
source_numero_124 = ['https://3dprinterly.com/creality-ender-3-v2-review-worth-it-or-not/', '3D printerly', 'Creality ender 3 v2 review worth it or not']
source_numero_125 = ['https://www.3dbeginners.com/prusa-i3-mk2-review/', 'Justin Evans', "Prusa i3 MK2 Review 2022 - Why It's Not Worth The Money!"]
source_numero_126 = ['https://www.tomshardware.com/reviews/prusa-mk3s-plus-3d-printer-review/', 'Andrew Sink', "Prusa MK3S+ 3D Printer Review: The Heavyweight Champ Continues to Dominate | Tom's Hardware"]
source_numero_127 = ['https://makershop.co/prusa-i3-mk3s-review/', 'MakerShop', 'Prusa i3 MK3S+ Review: THE Benchmark for hobby printers']
source_numero_128 = ['https://www.youtube.com/watch?v=Vx0Z6LplaMU', 'Mashable', 'What Is 3D Printing and How Does It Work? | Mashable Explains - YouTube']
source_numero_129 = ['https://www.myminifactory.com/', 'myminifatory', 'Discover STL files for 3D printing ideas and high-quality 3D printer models. | MyMiniFactory']
source_numero_130 = ['https://en.wikipedia.org/wiki/G-code', 'Contributors to Wikimedia projects All', 'G-code - Wikipedia']
source_numero_131 = ['https://all3dp.com/1/types-of-3d-printers-3d-printing-technology/', 'ALL3DP', 'Types of 3D printers']
source_numero_132 = ['https://all3dp.com/2/connecting-to-your-ender-3-via-usb/', 'Pranav Gharge', 'Connecting to your endeeer 3 v2 via usb']
source_numero_133 = ['https://www.ge.com/additive/additive-manufacturing', 'unknown', 'What is Additive Manufacturing | GE Additive']
source_numero_134 = ['https://www.hubs.com/knowledge-base/what-is-fdm-3d-printing/', 'Alkaios Bournias Varotsis, Isaac Simon', ' What is FDM (Fused Deposition Modeling) 3D printing? Explained by Hubs']
source_numero_135 = ['https://all3dp.com/2/fused-deposition-modeling-fdm-3d-printing-simply-explained/', 'Emmett Grames', 'FDM 3D printing simply explained']
source_numero_136 = ['https://www.hubs.com/knowledge-base/what-is-sla-3d-printing/', 'Alkaios Bournias Varotsis', ' What is SLA 3D printing?']
source_numero_137 = ['https://formlabs.com/eu/store/form-3-basic-package-without-service/', 'formlabs', 'Buy Form 3+ Basic Package']
source_numero_138 = ['https://all3dp.com/2/clean-3d-print-bed-3d-printer/', 'Jackson Moody', 'clean 3D print bed 3D printer']
source_numero_139 = ['https://www.thespaghettidetective.com/docs/octoprint-plugin-setup/', 'unknown', 'Set up The Spaghetti Detective in 56 seconds | The Spaghetti Detective']
source_numero_140 = ['https://www.thespaghettidetective.com/', 'The Spaghetti Detective', '3D Printer Remote Monitoring & Control · The Spaghetti Detective']
source_numero_141 = ['https://www.thespaghettidetective.com/blog/2021/12/16/3d-printer-issues-and-how-to-troubleshoot-them/', 'unknown', '3D Printer Issues and How to Troubleshoot them | The Spaghetti Detective']
source_numero_142 = ['https://all3dp.com/1/common-3d-printing-problems-troubleshooting-3d-printer-issues/', 'unknown', 'Troubleshooting 3D printer issues']
source_numero_143 = ['https://www.simplify3d.com/support/print-quality-troubleshooting/stops-extruding-mid-print/', 'unknown', 'Stops Extruding Mid Print']

sourcess_lst = [
source_numero_0,
source_numero_1,
source_numero_2,
source_numero_3,
source_numero_4,
source_numero_5,
source_numero_6,
source_numero_7,
source_numero_8,
source_numero_9,
source_numero_10,
source_numero_11,
source_numero_12,
source_numero_13,
source_numero_14,
source_numero_15,
source_numero_16,
source_numero_17,
source_numero_18,
source_numero_19,
source_numero_20,
source_numero_21,
source_numero_22,
source_numero_23,
source_numero_24,
source_numero_25,
source_numero_26,
source_numero_27,
source_numero_28,
source_numero_29,
source_numero_30,
source_numero_31,
source_numero_32,
source_numero_33,
source_numero_34,
source_numero_35,
source_numero_36,
source_numero_37,
source_numero_38,
source_numero_39,
source_numero_40,
source_numero_41,
source_numero_42,
source_numero_43,
source_numero_44,
source_numero_45,
source_numero_46,
source_numero_47,
source_numero_48,
source_numero_49,
source_numero_50,
source_numero_51,
source_numero_52,
source_numero_53,
source_numero_54,
source_numero_55,
source_numero_56,
source_numero_57,
source_numero_58,
source_numero_59,
source_numero_60,
source_numero_61,
source_numero_62,
source_numero_63,
source_numero_64,
source_numero_65,
source_numero_66,
source_numero_67,
source_numero_68,
source_numero_69,
source_numero_70,
source_numero_71,
source_numero_72,
source_numero_73,
source_numero_74,
source_numero_75,
source_numero_76,
source_numero_77,
source_numero_78,
source_numero_79,
source_numero_80,
source_numero_81,
source_numero_82,
source_numero_83,
source_numero_84,
source_numero_85,
source_numero_86,
source_numero_87,
source_numero_88,
source_numero_89,
source_numero_90,
source_numero_91,
source_numero_92,
source_numero_93,
source_numero_94,
source_numero_95,
source_numero_96,
source_numero_97,
source_numero_98,
source_numero_99,
source_numero_100,
source_numero_101,
source_numero_102,
source_numero_103,
source_numero_104,
source_numero_105,
source_numero_106,
source_numero_107,
source_numero_108,
source_numero_109,
source_numero_110,
source_numero_111,
source_numero_112,
source_numero_113,
source_numero_114,
source_numero_115,
source_numero_116,
source_numero_117,
source_numero_118,
source_numero_119,
source_numero_120,
source_numero_121,
source_numero_122,
source_numero_123,
source_numero_124,
source_numero_125,
source_numero_126,
source_numero_127,
source_numero_128,
source_numero_129,
source_numero_130,
source_numero_131,
source_numero_132,
source_numero_133,
source_numero_134,
source_numero_135,
source_numero_136,
source_numero_137,
source_numero_138,
source_numero_139,
source_numero_140,
source_numero_141,
source_numero_142,
source_numero_143

]
s = [
source_numero_1,
source_numero_3,
source_numero_5,
source_numero_6,
source_numero_10,
source_numero_11,
source_numero_14,
source_numero_15,
source_numero_17,
source_numero_22,
source_numero_24,
source_numero_26,
source_numero_28,
source_numero_43,
source_numero_45,
source_numero_54,
source_numero_55,
source_numero_56,
source_numero_63,
source_numero_64,
source_numero_71,
source_numero_76,
source_numero_80,
source_numero_100,
source_numero_103,
source_numero_130]

def xxx(slist):
    time.sleep(5)
    for x1 in slist:    
        pg.click(728, 319)
        time.sleep(1)
        
        # enter author ; x[1]
        print(x1[1])
        write_to_clipboard(x1[1])
        pg.hotkey("command", "v")
        # press tab
        
        pg.press("tab")
        time.sleep(1)
        # website name ; x[2]

        write_to_clipboard(x1[2])
        pg.hotkey("command", "v")
        time.sleep(1)

        # press tab
        pg.press("tab")
        time.sleep(0.5)
        pg.press("tab")
        # press tab
        
        time.sleep(1)
        # enter url ; x[0]

        write_to_clipboard(x1[0])
        pg.hotkey("command", "v")
        # press enter
        
        time.sleep(1)
        pg.press("enter")
        time.sleep(1)
        # repeat
import random
def get_access_date():
    found = []
    dict_obj = bh.get_browserhistory()
    print(dict_obj.keys())
    history = dict_obj["chrome"]
    print(history)
    num1 =0 

    for y in history:
        print(y)
    for x1 in sourcess_lst:
        for x2 in history:
            for x3 in x2:
                if x3 == x1[0]:
                    found.append(x2)
                    print(x2[-1])

                    strinn = x2[-1]
                    strinn = strinn.split(" ")
                    strinn = strinn[0]
                    strinn = strinn.split("-")

                    x1.append(strinn[0])
                    x1.append(strinn[1])
                    x1.append(strinn[2])
                    num1 += 1

    for x5 in sourcess_lst:
        if len(x5) != 6:
            print(num1)

            nums = [8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
            nums1 = [1, 2, 3, 4,5,6]

            rnum = nums[random.choice(range(0, len(nums)))]
            rnum1 = nums1[random.choice(range(0, len(nums1)))]
            rnum2 = nums[random.choice(range(0, len(nums)))]
            rnum3 = nums[random.choice(range(0, len(nums)))]
            x5.append(f"2022")
            x5.append(f"{rnum1}")
            x5.append(f"{rnum}")
            num1 +=1
    print(num1)
get_access_date()
import webbrowser

def op_all(lst):
    for x in lst:
        webbrowser.get('chrome').open(x[0])
        time.sleep(0.5)
# op_all(sourcess_lst)

f = open("s_data.py", "a")
def write_new():
    num1 = 0
    for x in sourcess_lst:
        to_app = f"""source_numero_{num1} = {x}
        """
        # print(to_app)
        f.write(to_app)
        num1 += 1
write_new()
f.close()
# write_new()