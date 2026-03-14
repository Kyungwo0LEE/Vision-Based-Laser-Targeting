# System Architecture

The vision-guided laser targeting system separates **vision processing** and **laser control**
to ensure stable operation with SAMLight hardware.

```mermaid
flowchart LR

Camera[Camera Input]

subgraph Python_Vision_System
A[OpenCV Circle Detection]
B[Coordinate Calibration]
C[Coordinate Transformation]
D[Target Selection]
end

subgraph Communication
E[TCP Socket]
end

subgraph Laser_Controller_CSharp
F[C# WinForms Controller]
G[SAMLight OCX API]
end

H[Galvo Laser Scanner]

Camera --> A
A --> B
B --> C
C --> D
D --> E
E --> F
F --> G
G --> H
