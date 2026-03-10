from time import sleep
from boot import LED, LED_STANDBY_DUTY, LIFX_SCENES, LIFX_HEADERS
from secrets import WIFI_SSID, WIFI_PASSWORD
import network  # type: ignore
import urequests  # type: ignore

REQUEST_TIMEOUT = 10


def connect_to_wifi():
    print("📡 Connecting to Wi-Fi...")
    station = network.WLAN(network.STA_IF)
    station.active(True)
    sleep(1)
    station.connect(WIFI_SSID, WIFI_PASSWORD)

    while not station.isconnected():
        blink_led(LED, 1, 0.5)

    if station.isconnected():
        print("✅ Connected!")
        blink_led(LED, 3, 0.15)

    return station


def blink_led(led, times, speed):
    for i in range(times):
        led.duty(1023)
        sleep(speed)
        led.duty(LED_STANDBY_DUTY)
        sleep(speed)


def toggle_lifx_power():
    print("⏳ Toggling lights power...")
    LED.duty(1023)

    try:
        # Make the POST request
        resp = urequests.request(
            "POST",
            "https://api.lifx.com/v1/lights/all/toggle",
            headers=LIFX_HEADERS,
            timeout=REQUEST_TIMEOUT,
        )

        # Handle the response
        data = resp.json()
        power_state = data["results"][0]["power"]
        resp.close()

        # Set LED back to standby brightness
        print(f"✅ Lights powered {power_state}!")
        LED.duty(LED_STANDBY_DUTY)

    except Exception as e:
        handle_failure(e)


def set_lifx_scene(scene_number):
    if scene_number < 1 or scene_number > len(LIFX_SCENES):
        print("❌ Scene index out of range!")
        return

    LED.duty(1023)

    scene_name = LIFX_SCENES[scene_number - 1]["name"]
    scene_id = LIFX_SCENES[scene_number - 1]["id"]
    print(f"⏳ Toggling scene {scene_number}: {scene_name}...")

    try:
        # Make the PUT request
        resp = urequests.request(
            "PUT",
            f"https://api.lifx.com/v1/scenes/scene_id:{scene_id}/activate",
            headers=LIFX_HEADERS,
            timeout=REQUEST_TIMEOUT,
        )
        resp.close()

        if resp.status_code != 207:
            raise RuntimeError("LIFX API didn't return a 207 status code")

        # Set LED back to standby brightness
        print("✅ Scene activated!")
        LED.duty(LED_STANDBY_DUTY)

    except Exception as e:
        handle_failure(e)


def handle_failure(err):
    # Blink the LED 5 times quickly to indicate an error
    blink_led(LED, 5, 0.05)
    print("❌ HTTP failed:", err)
