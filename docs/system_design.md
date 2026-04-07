# System Design Notes

## Project Title
**Smart Lighting Control System Design for a Commercial Office**

## 1. Problem Statement
Commercial spaces often waste energy when lights remain on in unoccupied rooms or operate at full brightness even when daylight is available. This project demonstrates a practical lighting-control concept that addresses those problems with a structured control design.

## 2. Design Goal
Design a project-specific lighting control solution that:
- supports occupant comfort
- reduces energy waste
- allows manual override
- is easy to explain to technical and non-technical stakeholders

## 3. Simulated Site Scope
The simulated site is a small commercial office floor with:
- reception area
- open workspace
- conference room
- two private offices
- hallway circulation zones

## 4. Main Components
| Component | Qty | Purpose |
|---|---:|---|
| LED Fixtures | 12 | General illumination |
| Motion Sensors | 4 | Occupancy detection by zone |
| Daylight Sensors | 2 | Detect natural light near windows |
| Manual Switches | 3 | User override in key spaces |
| Control Panel | 1 | Central logic and coordination |

## 5. Control Intent
### Automatic mode
- When motion is detected in a zone, the system checks available daylight.
- If daylight is low, fixtures in that zone turn on at high brightness.
- If daylight is sufficient, fixtures dim to a reduced level.
- If no motion is detected for a defined period, fixtures turn off.

### Manual override mode
- A wall switch can force a zone on or off temporarily.
- The override remains active until timeout or reset.

## 6. Design Decisions
### Sensor placement
Motion sensors are placed near the center of occupied zones to maximize detection coverage while limiting overlap. Daylight sensors are located closer to exterior windows where light variation is strongest.

### Fixture arrangement
Fixtures are spaced to provide even illumination and reduce dark spots. This also simplifies zoning for future expansion.

### Central control philosophy
A single control panel improves serviceability, documentation clarity, and coordination between field service and quotations teams.

## 7. Documentation Value
This project was structured like an applications-support deliverable rather than a classroom-only model. The documentation is meant to show:
- system thinking
- traceable design intent
- clean technical communication
- readiness to support submittals, layouts, and project discussions

## 8. Next Version
Future versions can include:
- detailed CAD sheets
- submittal-style device schedules
- energy calculations
- sequence-of-operations tables
- dashboard analytics
