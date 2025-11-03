from machine import Pin, PWM

# Components
LED = PWM(Pin(4))
LED.freq(1000)
LED_STANDBY_DUTY = 5

KEY1 = Pin(14, Pin.IN, Pin.PULL_UP)
KEY2 = Pin(12, Pin.IN, Pin.PULL_UP)
KEY3 = Pin(27, Pin.IN, Pin.PULL_UP)
