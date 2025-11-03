#!/bin/bash

# Set your ESP32 serial port
PORT="/dev/tty.usbserial-0001"

echo "----------------------------------------"

# Optional: remove all files on device first
mpremote connect $PORT fs rm *.py > /dev/null
mpremote connect $PORT fs rm -r lib/ > /dev/null

# Upload all Python files in the current directory
for file in *.py; do
    echo "⬆️  Uploading $file..."
    mpremote connect $PORT fs cp "$file" : > /dev/null
done

# Upload the entire lib/ directory
echo "⬆️  Uploading lib/ dir..."
mpremote connect $PORT fs cp -r "lib" : > /dev/null

echo "✅ Upload complete!"

echo "----------------------------------------"

mpremote connect $PORT reset # Reset the device so boot.py runs
sleep 1
mpremote connect $PORT run main.py # Run the code in dev mode
