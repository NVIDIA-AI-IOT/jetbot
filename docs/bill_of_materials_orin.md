# Bill of Materials - Jetson Orin Nano version

!!! note

    JetBot was originally designed with ***Jetson Nano Developer Kit***, which was [discontinued](https://forums.developer.nvidia.com/t/jetson-nano-developer-kit-eol/276729).

    For those newly starting, we recommend planning the JetBot assembly with **Jetson Orin Nano 8GB Developer Kit**. 

    Please note that, currently, the software for the Orin version of JetBot is still work in progress.


This page lists all the parts you need to build the open-source JetBot with the new [**Jetson Orin Nano 8GB Developer Kit**](https://developer.nvidia.com/embedded/learn/get-started-jetson-orin-nano-devkit), along with purchasing links from popular vendors.

Some of the parts are 3D printed.  We provide the STL files needed to print these parts.  Please see our [3d printing](3d_printing.md) page for tips on printing.

### Common parts

You need these components for each JetBot.

|  **Part** | **Quantity** | **Cost** | **URL** | **Notes** |
| --- | --: | --: | --- | --- |
| Jetson Orin Nano 8GB Developer Kit | 1 |  $499.00 | [NVIDIA](https://store.nvidia.com/jetson/store/)  |  |
| Micro SD card | 1 | $14.95 | [Amazon](https://a.co/d/0aOqPQh) | 128GB |
| Motor | 2 | $5.90 | [Adafruit](http://adafru.it/3777), [Amazon(1)](https://a.co/d/cQ489BJ), [Amazon(2)](https://amzn.to/2MU9zPb) | "TT" form factor |
| Motor Driver | 1 | $19.95 | [Adafruit](http://adafru.it/2927), [Amazon](https://a.co/d/aUs8dwA) |  |
| Caster ball | 1 | $10.99 | [Amazon](https://a.co/d/3WmVtqU) | 1-inch diameter |
| USB cable pack | 1 | $6.99 | [Amazon](http://amzn.com/B01N337FQF/) | Type A to Micro, right angle |
| *PiOLED* display | 1 | $13.45 | [Adafruit](http://adafru.it/3527), [Amazon](https://a.co/d/cmRS0RE) |  |
| *PiOLED* header | 1 | $7.99 | [Adafruit](http://adafru.it/1541), [Amazon](https://a.co/d/fGDbnIE), [Sparkfun](https://www.sparkfun.com/products/12792) | 2x(3+) right angle male |
| Chassis | 1 | -- | [STL file](cad/chassis.stl) | see [3D printing](3d-printing) | |
| Camera Mount | 1 | -- | [STL file](cad/camera_mount.stl) | see [3D printing](3d-printing) |

### Power source

|  **Part** | **Quantity** | **Cost** | **URL** | **Notes** |
| --- | --: | --: | --- | --- |
| Battery | 1 | $12.99 | [Amazon](https://a.co/d/5DvsXGu) | PD 20W output, 10,000mAh |
| USB-C PD cable | 1 | $10.99 | [Amazon](https://a.co/d/ihjA431) | USB-C to DC 5.5mm x 2.5mm, right angle |

!!! note

    With this power source option, we recommend setting Jetson Orin Nano in `7W` mode (`sudo nvpmodel -m 1`), as we observed Jetson in `15W` mode shutdown in certain scenarios like suddenly ramping up the motor from 0% to 100% speed or having motors stalled.

### Camera

You need a camera module with 22pin cable for interfacing to Jetson Orin Nano 8GB Developer Kit carrier board and the appropriate wide field of view for each JetBot.  

Select an option and get the parts specified.

#### Option 1 (default) - IMX219 175-degree FoV camera

|  **Part** | **Quantity** | **Cost** | **URL** | **Notes** |
| --- | --: | --: | --- | --- |
| Camera | 1 | $19.99 | [ArduCam](https://www.arducam.com/product/8mp-imx219-175-degree-ultra-wide-angle-raspberry-pi-b0392/), [Amazon](https://a.co/d/gbWtB9X) | ArduCam B0392 - IMX219 175-degree |

<!-- #### Option 2 - IMX477 12.3MP 88°(D)×75°(H)

|  **Part** | **Quantity** | **Cost** | **URL** | **Notes** |
| --- | --: | --: | --- | --- |
| Camera | 1 | $64.99 | [ArduCam](https://www.arducam.com/product/arducam-high-quality-camera-for-jetson-nano-and-xavier-nx-12mp-m12-mount/), [Amazon](https://a.co/d/gIJkaBO) | ArduCam B0251 - IMX477 12.3MP 88°(D)×75°(H) | -->

### Wheels

You need wheels with a "TT" motor shaft connector for each JetBot.  Select an option and get the parts specified.

#### Option 1 - 60mm

|  **Part** | **Quantity** | **Cost** | **URL** | **Notes** |
| --- | --: | --: | --- | --- |
| Wheel | 2 | $5.00 | [Adafruit](http://adafru.it/3757) | 60mm diameter |
| Caster base | 1 | -- | [STL file](cad/caster_base_60mm.stl) | for 60mm wheel |
| Caster shroud | 1 | -- | [STL file](cad/caster_shroud_60mm.stl) | for 60mm wheel |

#### Option 2 - 65mm

|  **Part** | **Quantity** | **Cost** | **URL** | **Notes** |
| --- | --: | --: | --- | --- |
| Wheel | 2 | $3.00 | [Adafruit](https://www.adafruit.com/product/3763) | 65mm diameter |
| Caster base | 1 | -- | [STL file](cad/caster_base_65mm.stl) | for 65mm wheel|
| Caster shroud | 1 | -- | [STL file](cad/caster_shroud_65mm.stl) | for 65mm wheel |

### Assembly Hardware

You need the following parts to build JetBot.  They come in packs, so order the quantity you need for the number of JetBots you are going to build.

|  **Part** | **Qty per JetBot** | **Qty per pack** | **Cost per JetBot** | **URL** | **Notes** |
| --- | --- | --: | --: | --: | --- |
| Adhesive Strips (Poster Strips) | 2 | 60 | $0.14 | [Amazon](https://a.co/d/0vJTr7M) | |
|  M2 screw | 20 | 100 | $1.40 | [Amazon](https://a.co/d/cyiag7K) | 8mm long, self tapping |
|  M3 screw | 4 | 60 | $0.47 | [Amazon](https://a.co/d/2foBYX5) | 25mm long|
|  M3 nut | 4 | 150 | $0.20 | [Amazon](https://a.co/d/05wzwMC) |  |
|  Jumper wires | 4 | 40 | $0.56 | [Amazon](https://a.co/d/5FdEzo4) | Female-female, ~20cm |
