#!/bin/bash

# Flash the ESP32 with the MicroPython firmware
esptool.py --chip esp32 --port /dev/tty.usbserial-0001 write_flash -z 0x1000 ESP32_GENERIC-20250911-v1.26.1.bin