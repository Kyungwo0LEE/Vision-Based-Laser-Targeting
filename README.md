# Vision-Based-Laser-Targeting
Camera-based circular target detection and coordinate calibration for a vision-guided laser targeting system.

This project develops a vision-based laser targeting system that detects circular targets using a camera, performs coordinate calibration, and ultimately aims to fire a laser to track targets in real tiem.

## Project Overview
The system is designed to follow a **stage-by-stage development approach**:
1. Camera Test & Vision Validation
2. Laser Control Integration
3. Vision-Guided Laser Targeting with Feedback

## Phase 1: Camera Test
- Camera connection and live video streaming
- Circular target detection using OpenCV (Hough Transform)
- Camera coordinate normalization
- Linear coordinate calibration (camera-->laser space)
- Real-time target tracking (vision only)

### Phase 1 Implementation Details
- Vision modules are organized under the `vision/` package.
- Calibration and tracking results are logged locally as CSV files.
- No laser hardware is required for this phase.

### How to Run Phase 1
```bash
pip install -r phase1_camera_test/requirements.txt
python phase1_camera_test/main.py

### Demo (Phase 1)

![Phase 1 Demo](docs/phase1_demo.gif)

The demo above shows real-time circular target detection and vision-only tracking
using a live camera feed.


## Phase 2: Laser Integration
- Laser control backend integration
- Real-time laser firing on tracked targets
- Vision-laser closed-loop feedback
- Support for hardware-specific laser control software (e.g. SAMLight)

## Author
Kyungwoo Lee  
Undergraduate Student, Mechanical Engineering
