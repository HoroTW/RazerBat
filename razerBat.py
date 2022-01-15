#!/usr/bin/env python3

from openrazer.client import DeviceManager

device_manager = DeviceManager()
dock = mouse = None

for device in device_manager.devices:
    mouse = device if device.name == "Razer Viper Ultimate (Wireless)" else mouse
    dock = device if device.name == "Razer Mouse Dock" else dock

charging = "" if mouse.is_charging else "🔋"
print(f"{mouse.name} {charging} {mouse.battery_level}")
