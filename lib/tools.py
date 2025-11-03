from time import sleep
from boot import LED, LED_STANDBY_DUTY
from secrets import WIFI_SSID, WIFI_PASSWORD, LIFX_AUTH_TOKEN
import network
import urequests

LIFX_HEADERS = {"Authorization": f"Bearer {LIFX_AUTH_TOKEN}"}

LIFX_SCENES = [
    {
        "name": "Daytime Work",
        "id": "69486701-6477-4d22-97ea-00adebe1a8c8",
    },
    {
        "name": "Chill Neon",
        "id": "f8d2de78-25e1-490f-8095-e2629aeefbc8",
    },
    {
        "name": "Deep Vibes",
        "id": "e9898260-b9ab-4337-b0a0-65a12d7fba6f",
    },
    {
        "name": "Into the Blue",
        "id": "66dafa6b-2483-46e2-9218-122668ef73ee",
    },
    {
        "name": "Library",
        "id": "f27b4b60-437e-4c84-af51-1408762f2145",
    },
    {
        "name": "Cozy Nighttime",
        "id": "ee7857af-2ecf-4141-851c-5eaf5990d79c",
    },
    {
        "name": "Summer Light",
        "id": "c5198da7-b4e8-43e4-9ee4-6f325c2453f8",
    },
]


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


def fade_led_in_out(led, speed):
    for duty in range(0, 1024, 8):
        led.duty(duty)
        sleep(speed)
    for duty in range(1023, -1, -8):
        led.duty(duty)
        sleep(speed)


def toggle_lifx_power():
    print("🎚️ Toggling lights power...")
    LED.duty(1023)

    # Make the POST request
    resp = urequests.request(
        "POST", "https://api.lifx.com/v1/lights/all/toggle", headers=LIFX_HEADERS
    )

    # Handle the response
    data = resp.json()
    power_state = data["results"][0]["power"]
    resp.close()

    print(f"✅ Lights powered {power_state}!")
    LED.duty(LED_STANDBY_DUTY)


def set_lifx_scene(scene_index):
    LED.duty(1023)

    scene_name = LIFX_SCENES[scene_index]["name"]
    scene_id = LIFX_SCENES[scene_index]["id"]
    print(f"🎚️ Toggling scene: {scene_name}...")

    # Make the PUT request
    resp = urequests.request(
        "PUT",
        f"https://api.lifx.com/v1/scenes/scene_id:{scene_id}/activate",
        headers=LIFX_HEADERS,
    )
    resp.close()

    print("✅ Scene activated!")
    LED.duty(LED_STANDBY_DUTY)
