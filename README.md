# Vision-Based-Laser-Targeting
Camera-based circular target detection and coordinate calibration for a vision-guided laser targeting system.

This project develops a vision-based laser targeting system that detects circular targets using a camera, performs coordinate calibration, and ultimately aims to fire a laser to track targets in real time.

## Project Overview
The system is designed to follow a **stage-by-stage development approach**:
1. Camera Test & Vision Validation
2. Laser Control Integration
3. Vision-Guided Laser Targeting with Feedback

The project is designed with a modular architecture separating:

- Vision processing (Python / OpenCV)  
- Laser control backend (C# / SAMLight OCX)  
- Future inter-process communication bridge  

---

## Phase 1: Camera Test (Completed)

### Features

- Camera connection and live video streaming  
- Circular target detection using OpenCV (Hough Transform)  
- Camera coordinate normalization  
- Linear coordinate calibration (camera → laser space)  
- Real-time target tracking (vision only)  
- CSV logging of calibration and tracking data  

### Implementation Details

- Vision modules are organized under the `vision/` package.  
- Calibration parameters (a, b, c, d) are computed from 3-point reference alignment.  
- Tracking results are logged locally for reproducibility.  
- No laser hardware is required for this phase.  

### How to Run Phase 1
```bash
pip install -r phase1_camera_test/requirements.txt
python phase1_camera_test/main.py
```

### Demo (Phase 1)

![Phase 1 Demo](docs/phase1_demo.gif)

The demo above shows real-time circular target detection and vision-only tracking
using a live camera feed.

---
## Phase 2: Laser Integration (Partially Verified)

### Objective

Integrate the vision-based coordinate system with laser control software and enable real-time laser firing on tracked targets.

### Current Status

- SAMLight integration via C# (WinForms + OCX): ✅ Verified
- Laser entity creation and marking test: ✅ Verified
- Direct Python → SAMLight COM control: ❌ Not supported / unstable

SAMLight is built on an ActiveX (OCX) architecture primarily designed for .NET (C#) environments.
Direct COM control from Python was tested but resulted in instability due to threading and ActiveX constraints.

### Technical Findings

- SAMLight OCX operates reliably inside a WinForms (.NET) environment.
- Python-based COM access through pywin32 is not officially supported.
- Stable laser control requires a dedicated C# controller application.

### Architecture Decision

To ensure stability and hardware safety, the system architecture will follow:

Python (Vision Processing)
→ C# Laser Controller (SAMLight OCX)
→ Laser Hardware

A TCP-based communication bridge between Python and C# will be implemented in the next stage.

### Why This Approach?

- Prevents COM threading conflicts
- Maintains compatibility with SAMLight’s intended API usage
- Enables modular system expansion
- Aligns with industrial vision–laser system design practices

---

### Next Step (Phase 3)

- Implement TCP-based communication between Python and C#
- Transmit real-time transformed coordinates
- Execute stable laser marking sequence
- Validate vision–laser synchronization

## Author
Kyungwoo Lee  
Undergraduate Student, Mechanical Engineering
