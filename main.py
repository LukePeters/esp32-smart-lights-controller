from boot import KEY1, KEY2, KEY3, MULTIPRESS_WINDOW
import tools  # type: ignore
from time import sleep, ticks_ms, ticks_diff

# Global variables and state
key1_prev_state = 1
key2_prev_state = 1
key3_prev_state = 1
key3_press_count = 0
key3_last_press_time = 0

station = tools.connect_to_wifi()

while True:

    # Reconnect to Wi-Fi if not connected
    if not station.isconnected():
        station = tools.connect_to_wifi()
        continue

    # Read current key states
    key1_state = KEY1.value()
    key2_state = KEY2.value()
    key3_state = KEY3.value()

    # Key 1: Handle press
    if key1_prev_state == 1 and key1_state == 0:
        tools.toggle_lifx_power()

    # Key 2: Handle press
    if key2_prev_state == 1 and key2_state == 0:
        tools.set_lifx_scene(5)

    # Key 3: Handle multipress
    if key3_prev_state == 1 and key3_state == 0:
        now = ticks_ms()
        # If time since last press is short, increment count
        if ticks_diff(now, key3_last_press_time) < MULTIPRESS_WINDOW:
            key3_press_count += 1
        else:
            key3_press_count = 1  # New sequence
        key3_last_press_time = now

    # Key 3: Check if multipress window has elapsed
    if (
        key3_press_count > 0
        and ticks_diff(ticks_ms(), key3_last_press_time) > MULTIPRESS_WINDOW
    ):
        # Send the number of presses as the scene number
        tools.set_lifx_scene(key3_press_count)

        # Reset press count after handling
        key3_press_count = 0

    # Update previous key states
    key1_prev_state = key1_state
    key2_prev_state = key2_state
    key3_prev_state = key3_state

    # Sleep to reduce CPU usage and debounce buttons
    sleep(0.1)
