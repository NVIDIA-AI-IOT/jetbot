# Changes

## [Master]

## [0.4.3]

### Added

- Added ``LocalController`` class which allows users to directly connect controller to JetBot

## [0.4.2] - 11/10/2020

### Fixed

- Resolved software issue which affected certain motor driver variants

## [0.4.1] - 10/22/2020

### Added

- ZMQ Camera publisher to improve stability of Camera and allow camera use in multiple notebooks
- Docker containers for ML dependencies, PiOLED display, ZMQ Camera publisher, and Jupyter Lab server
- Inline documentation using mkdocs-material and mike

### Changed

- Default ``Camera`` class now uses ZMQ Camera.  This means you must run the ZMQ camera publisher to access the camera as before.  If you wish to use the old Camera class, do ```from jetbot.camera.opencv_gst_camera import OpenCvGstCamera``` and ``camera = OpenCvGstCamera()``

### Deprecated

- JetPack 4.3 SD card image

### Fixed

- Camera shutdown failures are avoided by addition of ZMQ Camera. No longer need for constant ``systemctl restart nvargus-daemon`` calls.
- Camera queue buildup for heavier image processing workloads is fixed in ZMQ Camera by dropping old frames using conflate option.

## [0.4.0] - 1/15/2020

### Added

- Added support for JetPack 4.3 SD card image.  Found [here](https://drive.google.com/open?id=1G5nw0o3Q6E08xZM99ZfzQAe7-qAXxzHN).

### Changed

- Updated Object Detector SD card image.  Found [here](https://drive.google.com/open?id=1KjlDMRD8uhgQmQK-nC2CZGHFTbq4qQQH)

## [0.3.0] - 3/9/2019

### Added

- Initial release with JetPack 4.2 SD card image.  Found [here](https://drive.google.com/open?id=1RgQ99QOqhcNxivSNJpetXdoOCqUWAWH_)

[Master]: https://github.com/NVIDIA-AI-IOT/jetbot/compare/v0.4.0...HEAD
[0.4.0]: https://github.com/NVIDIA-AI-IOT/jetbot/compare/v0.3.0...v0.4.0
[0.3.0]: https://github.com/NVIDIA-AI-IOT/jetbot/releases/tag/v0.3.0
