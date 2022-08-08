# 3D Printing
This page has useful information related to printing the JetBot chassis using a 3D printer.  There are two methods for printing JetBot

* [Method 1 - Print by yourself](#method-1-print-by-yourself)
* [Method 2 - Use a printing service](#method-2-use-a-printing-service)

## Method 1 - Print by yourself

If you have a 3D printer, we recommend printing the JetBot components yourself!

### Files:

|  **Part** | **URL** | **Notes** 
| --- | --- | --- |
| Chassis | [STL file](cad/chassis.stl) | |
| Camera Mount | [STL file](cad/camera_mount.stl) | |
| Caster base | [STL file](cad/caster_base_60mm.stl) | [for 60mm wheel](bill_of_materials.html#wheels) |
| Caster shroud  | [STL file](cad/caster_shroud_60mm.stl) | [for 60mm wheel](bill_of_materials.html#wheels) |
| Caster base  | [STL file](cad/caster_base_65mm.stl) | [for 65mm wheel](bill_of_materials.html#wheels) |
| Caster shroud | [STL file](cad/caster_shroud_65mm.stl) | [for 65mm wheel](bill_of_materials.html#wheels) |

### Prebuilt GCode / Prusa Slicer Project Files:
These gcodes are prebuilt and tested by us. They are ready to go on your SD card for printing.

|  **Printer** | **Gcode** | **Image**| **Nozzle** | **Prusa Slicer** | **Notes** |
| --- | --- | --- | --- | --- | --- |
| Creality Ender 3 | [Gcode file](cad/jetbot_ender_3_04mm_nozzle.gcode) | [IMAGE](images/prebuilt_ender3.png) | 0.4mm | [Project File](cad/jetbot_ender3.3mf) | for 60mm wheel |
| Prusa Mini | [Gcode file](cad/jetbot_prusa_mini_04mm_nozzle.gcode) | [IMAGE](images/prebuilt_mini.png) | 0.4mm | [Project File](cad/jetbot_prusa_mini.3mf) | for 60mm wheel |
| Prusa Mk3 | [Gcode file](cad/jetbot_prusa_mk3_04mm_nozzle.gcode) | [IMAGE](images/prebuilt_mk3.png) | 0.4mm | [Project File](cad/jetbot_prusa_mk3.3mf) | for 60mm wheel |


### Print facts:

Below are some facts related to printing a single JetBot.

* Print time:  12-15 hours
* Material used:  ~ 100 grams
* Material cost:  ~ $2

### Tested Printers:

We've tested that the following printers are able to print JetBot successfully. If you’re just beginning to enter the 3D printing space a [Prusa Mini](https://www.prusa3d.com/product/original-prusa-mini-kit-2) is highly recommended for its reliability. Where a [Creality Ender 3](https://amzn.to/3P78lP5) is less reliable but very affordable.

| Model | Cost | URL |
|------------|------|---|
| Creality Ender 3 | $189 | [Amazon](https://amzn.to/3P78lP5) |
| Prusa Mini | $429 | [Prusa](https://www.prusa3d.com/product/original-prusa-mini-kit-2/) |
| Prusa Mk3 | $799 | [Prusa](https://www.prusa3d.com/product/original-prusa-i3-mk3s-kit-3/) |

### Tested Filaments:

Based on our experience, we recommend using PLA filament when printing JetBot.  Below is a collection
of filaments that we have tested with the [Ender 3](https://amzn.to/3P78lP5) and [Prusa](https://www.prusa3d.com/product/original-prusa-mini-kit-2/) 3D printers.

| Brand | Thickness | Material | Color | URL | Notes |
|-------|-----------|----------|-------|-----|-------|
| AmazonBasics | 1.75mm | PLA | Silver | [Amazon](https://amzn.to/3JzgZ7C) | Smooth, dark metallic finish |
| AmazonBasics | 1.75mm | PLA | Neon Green | [Amazon](https://amzn.to/3Jz7DZH) | Smooth, pale finish|
| AmazonBasics | 1.75mm | PLA | Black | [Amazon](https://amzn.to/3vN0XS9) |  Black, pale finish |
| AmazonBasics | 1.75mm | PLA | Yellow | [Amazon](https://amzn.to/3QtrAmL) |  Yellow, slightly translucent |
| AmazonBasics | 1.75mm | PLA | Purple | [Amazon](https://amzn.to/3BJbmBV) | Smooth, pale finish |

### Printing and slicing configuration:

* STL unit: **mm**

* Print orientation

<a href="images/Cura-Print-Setup_overall.png"><img src="images/Cura-Print-Setup_overall.png" width="800" height="480"></a>

* Slice configuration (Cura)

<img src="images/Cura-Print-Setup_Detail_Express.png" >

## Method 2 - Use a printing service

If you don't have a 3D printer on hand, and are not interested in purchasing one, there are external services
that can print the chassis for you.  Below are some quotes from popular 3D printing services

> Please note, we have not tested these services yet ourselves, so please proceed with caution.  If you
> find a print service that worked well for you, we'd love to hear!  Please let us know by creating
> an issue on GitHub or mentioning it in the chat channel

| Service | Quote |
|---------|--------|
| [3DHubs](https://www.3dhubs.com/) | $36.66 |
| [Jinxbot](https://jinxbot.com/) | $91.42 |
| [Sculpteo](https://www.sculpteo.com/) | ~$100 |