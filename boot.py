from machine import Pin, PWM
from secrets import LIFX_AUTH_TOKEN

# LED Configuration
LED = PWM(Pin(4))
LED.freq(1000)
LED_STANDBY_DUTY = 5

# Key Configurations
KEY1 = Pin(14, Pin.IN, Pin.PULL_UP)
KEY2 = Pin(12, Pin.IN, Pin.PULL_UP)
KEY3 = Pin(27, Pin.IN, Pin.PULL_UP)
MULTIPRESS_WINDOW = 500  # Milliseconds

# LIFX API Configurations
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
