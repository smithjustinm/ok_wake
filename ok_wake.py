# Neopixel OK to Wake clock

import time
from datetime import datetime, timedelta
import sched

from neopixel import *


# LED ring configuration
LED_COUNT = 12  # Number of LED pixels.
LED_PIN = 18  # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 5  # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 25  # Set to 0 for darkest and 255 for brightest
LED_INVERT = False  # True to invert the signal (when using NPN transistor level shift)


# Define functions which animate LEDs for ok-to-wake clock
def stay_in_bed(strip, color, wait_ms=50):
    """Red color from bedtime until time to wake"""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, Color=(205, 92, 92))
        strip.show()


def up_time(strip, color, wait_ms=50):
    """Green color from wake_up time until 30 minutes has passed"""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, Color=(60, 179, 113))
        strip.show()


def light_off(strip, color):
    """The light is off"""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color=(0, 0, 0))
        strip.show()


if __name__ == '__main__':
    # Create NeoPixel object with appropriate configuration.
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
    # Initialize the library (must be called once before other functions).
    strip.begin()