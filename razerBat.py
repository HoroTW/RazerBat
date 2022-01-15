#!/usr/bin/env python3
from openrazer.client import DeviceManager

devices = DeviceManager().devices
bat_devices = [d for d in devices if d.battery_level]

for device in bat_devices:
    charging = "" if device.is_charging else "🔋"
    print(f"{device.name} {charging} {device.battery_level}%")
