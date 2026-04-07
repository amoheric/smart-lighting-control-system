"""
lighting_logic.py

Simple simulation of a smart lighting control workflow for a commercial office.
This is a portfolio demonstration script and not production building-controls code.
"""

from dataclasses import dataclass


@dataclass
class ZoneState:
    name: str
    motion_detected: bool
    daylight_level: int  # 0 to 100
    manual_override: str | None = None  # "ON", "OFF", or None


def lighting_control(zone: ZoneState) -> str:
    """
    Determine lighting behavior based on occupancy, daylight, and override state.
    """
    if zone.manual_override == "ON":
        return f"{zone.name}: Lights ON (Manual Override)"
    if zone.manual_override == "OFF":
        return f"{zone.name}: Lights OFF (Manual Override)"

    if zone.motion_detected:
        if zone.daylight_level < 50:
            return f"{zone.name}: Lights ON (High Brightness)"
        return f"{zone.name}: Lights ON (Dimmed)"
    return f"{zone.name}: Lights OFF"


def demo() -> None:
    test_zones = [
        ZoneState("Reception", True, 20, None),
        ZoneState("Conference Room", True, 70, None),
        ZoneState("Private Office 1", False, 40, None),
        ZoneState("Hallway", True, 35, "ON"),
        ZoneState("Private Office 2", True, 60, "OFF"),
    ]

    for zone in test_zones:
        print(lighting_control(zone))


if __name__ == "__main__":
    demo()
