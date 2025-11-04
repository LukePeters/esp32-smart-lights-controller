from boot import KEY1, KEY2, KEY3, MULTIPRESS_WINDOW
import tools
from time import sleep, ticks_ms, ticks_diff

# Global variables and state
key1_prev_state = 1
key2_prev_state = 1
key3_prev_state = 1
key3_press_count = 0
key3_last_press_time = 0

station = tools.connect_to_wifi()

while station.isconnected():

    # READ KEYS
    key1_state = KEY1.value()
    key2_state = KEY2.value()
    key3_state = KEY3.value()

    # KEY 1 PRESSED
    if key1_prev_state == 1 and key1_state == 0:
        tools.toggle_lifx_power()

    # KEY 2 PRESSED
    if key2_prev_state == 1 and key2_state == 0:
        tools.set_lifx_scene(5)

    # KEY 3: MULTIPRESS DETECTION
    if key3_prev_state == 1 and key3_state == 0:
        now = ticks_ms()
        # If time since last press is short, increment count
        if ticks_diff(now, key3_last_press_time) < MULTIPRESS_WINDOW:
            key3_press_count += 1
        else:
            key3_press_count = 1  # New sequence
        key3_last_press_time = now

    # KEY 3: CHECK IF MULTIPRESS WINDOW EXPIRED
    if (
        key3_press_count > 0
        and ticks_diff(ticks_ms(), key3_last_press_time) > MULTIPRESS_WINDOW
    ):
        # Send the number of presses as the scene number
        tools.set_lifx_scene(key3_press_count)

        # Reset press count after handling
        key3_press_count = 0

    # UPDATE PREV STATES
    key1_prev_state = key1_state
    key2_prev_state = key2_state
    key3_prev_state = key3_state

    # Sleep to reduce CPU usage and debounce buttons
    sleep(0.1)
