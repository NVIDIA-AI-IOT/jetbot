This page lists everything you need to build JetBot, along with purchasing links from popular vendors.

Some of the parts are 3D printed.  We provide the STL files needed to print these parts.  Please see our [3d printing](3d_printing.md) page for tips on printing.

### Common parts

You need these components for each JetBot.

|  **Part** | **Quantity** | **Cost** | **URL** | **Notes** |
| --- | --: | --: | --- | --- |
| Jetson Nano | 1 |  $99.00 | [NVIDIA](https://developer.nvidia.com/embedded/buy/jetson-nano-devkit)  |  |
| Micro SD card | 1 | $13.99 | [Amazon](https://amzn.to/2Us6bOv) | 64GB |
| Power supply | 1 | $7.50 | [Adafruit](http://bit.ly/af1995) | Micro USB, 5V, 2.5A |
| Motor | 2 | $5.90 | [Adafruit](http://adafru.it/3777), [Amazon(1)](https://amzn.to/2MYln32), [Amazon(2)](https://amzn.to/2MU9zPb) | "TT" form factor |
| Motor Driver | 1 | $19.95 | [Adafruit](http://adafru.it/2927), [Amazon](https://amzn.to/2GvJhBA) |  |
| Caster ball | 1 | $6.30 | [Amazon](http://amzn.com/B01N2S7CX6/) | 1-inch diameter |
| Battery | 1 | $15.99 | [Amazon](https://amzn.to/2WRcIUe) | 2x 5V/3A output, 10,000mAh |
| USB cable pack | 1 | $6.99 | [Amazon](http://amzn.com/B01N337FQF/) | Type A to Micro, right angle |
| *PiOLED* display | 1 | $14.95 | [Adafruit](http://adafru.it/3527), [Amazon](https://amzn.to/2GgxUxX) |  |
| *PiOLED* header | 1 | $5.95 | [Adafruit](http://adafru.it/1541), [Amazon](https://amzn.to/2taLSJf), [Sparkfun](https://www.sparkfun.com/products/12792) | 2x(3+) right angle male |
| Chassis | 1 | -- | [STL file](cad/chassis.stl) | see [3D printing](3d-printing) | |
| Camera Mount | 1 | -- | [STL file](cad/camera_mount.stl) | see [3D printing](3d-printing) |

### Camera

You need a camera with appropriate sensor and field of view for each JetBot.  Select an option and get the parts specified.

#### Option 1 (default) - Leopard Imaging Camera

|  **Part** | **Quantity** | **Cost** | **URL** | **Notes** |
| --- | --: | --: | --- | --- |
| Camera | 1 | $29.00 | [Leopard Imaging](https://leopardimaging.com/product/li-imx219-mipi-ff-nano/) | LI-IMX219-MIPI-FF-NANO-**H145**|

#### Option 2 - IMX219-160 Camera

|  **Part** | **Quantity** | **Cost** | **URL** | **Notes** |
| --- | --: | --: | --- | --- |
| Camera | 1 | $29.90 | [Amazon](http://amzn.com/B07T43K7LC/) | IMX219-160 Camera |

#### Option 3 - RPi Camera V2 + Lens Attachment

|  **Part** | **Quantity** | **Cost** | **URL** | **Notes** |
| --- | --: | --: | --- | --- |
| Camera | 1 | $23.90 | [Amazon](https://amzn.to/2MSi6lL), [Adafruit](http://adafru.it/3099) | Raspberry Pi Camera V2 |
| Camera lens attachment | 1 | $18.99 | [Amazon(1)](https://amzn.com/B07HMXJ9Y1), [Amazon(2)](https://amzn.com/B07HF81BVL/), [eBay](https://ebay.us/Fz7HGd) | 160-degree FoV |

### WiFi

You need a WiFi solution for each JetBot.  Select an option and get the parts specified.

#### Option 1 (default) - M2 Card + Antennas

This option is a good choice if you're building JetBot with the original Jetson Nano 4GB.  It has been widely tested and used for JetBot.

???+ attention

    Jetson Nano 2GB does not have a M.2 connector, so this option will not work with it.

|  **Part** | **Quantity** | **Cost** | **URL** | **Notes** |
| --- | --: | --: | --- | --- |
| WiFi card | 1 | $18.95 | [Amazon](https://amzn.to/2WKEkum), [NewEgg](https://www.neweggbusiness.com/Product/Product.aspx?Item=9SIV21M85N2699) | M2, Intel Wireless-AC 8265 |
| WiFi antenna | 2 | $5.06 | [Arrow](https://www.arrow.com/en/products/2042811100/molex) | U.FL connectors |

#### Option 2 - USB Dongle

This option is compatible with both the original Jetson Nano (4GB) and Jetson Nano 2GB.

|  **Part** | **Quantity** | **Cost** | **URL** | **Notes** |
| --- | --: | --: | --- | --- |
| WiFi Dongle - TP-Link Archer T2U Nano | 1 | $17.99 | [Amazon](https://amzn.com/B07PB1X4CN/) | RTL8811AU chipset |
| WiFi Dongle - TP-Link Archer T2U Plus | 1 | $19.99 | [Amazon](https://amzn.com/B07P5PRK7J/) | RTL8811AU chipset |

???+ info
    For other possible USB Wi-fi dongles that you can use on Jetson Nano, please check the Suported Components List.

    - [Jetson Nano 2GB Developer Kit User Guide - Supported Component List](https://developer.nvidia.com/embedded/learn/jetson-nano-2gb-devkit-user-guide#id-.JetsonNano2GBDeveloperKitUserGuidevbatuu_v1.0-SupportedComponentList)

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
|  Adhesive pads | 2 | 48 | $0.14 | [Amazon](http://amzn.com/B01FIK56Q4) | |
|  M2 screw | 20 | 100 | $1.29 | [Amazon](http://amzn.com/B00YBMRAH4) | 8mm long, self tapping |
|  M3 screw | 4 | 60 | $0.47 | [Amazon](https://amzn.to/2tcdluk) | 25mm long|
|  M3 nut | 4 | 100 | $0.24 | [Amazon](https://amzn.to/2tb8PMo) |  |
|  Jumper wires | 4 | 40 | $0.13 | [Amazon](https://amzn.to/2tacYQD) | Female-female, ~20cm |
