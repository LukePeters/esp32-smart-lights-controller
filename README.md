# LIFX ESP32 Macropad

A custom desk-mounted device with buttons that control the LIFX smart lights in my home office. Powered by an ESP32 development board.

I'm using [mpremote](https://github.com/micropython/micropython/tree/master/tools/mpremote) to upload firmware to the ESP32 board. I created a helper script to make it super easy to upload all code changes to the device:

1. Plug the ESP32 into my computer
1. Execute the helper script to upload all code: `./upload.sh`
1. After upload, the script connects to the board so I can see serial output in the console

## Button functionality

The buttons are low-profile mechanical keyboard switches from Gateron.

- Button 1
  - Press once to toggle all lights on or off.
- Button 2
  - Press once to set the lighting scene to my usual default.
- Button 3
  - Press a set number times quickly to set a particular scene.
  - One press will activate Scene 1, two quick presses will activate Scene 2, etc.

## LED functionality

When the board is powered on it will try to connect to my Wi-Fi network. While it's connecting it will blink slowly. Once connected it will flash quickly three times to indicate success.

When idle, the LED remains on at 5% brightness. This helps me navigate to the device in my office at night. It's the little things, y'know? That's the beauty of solving your own problems with custom-built solutions.

Whenever a button is pressed, the LED lights up to 100% brightness until a successful response is received. This gives you confidence that pressing the button did something and that it's working on the request.
