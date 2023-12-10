import struct
import utime
import ustruct
import machine
import math
from machine import UART, Pin
uart = UART(0, 9600, tx=Pin(0), rx=Pin(1), parity = None, stop = 2)
#led setup
led = machine.Pin(25, machine.Pin.OUT)  # Define the LED pin
# LED is turned on to indicate that the system is running
# control pins
trigger_pin = machine.Pin(14, machine.Pin.OUT)
output = machine.Pin(15, machine.Pin.OUT)
# Set constants
speed_of_sound_75f = 1480
start_time = 0
end_time = 0
init = 0
inc = 15
# Function to send square wave and take start_time
def truncate(distance):
    rounded_dist = math.trunc(distance)
    decimal_val = distance - rounded_dist
    decimal_val = decimal_val * 100
    decimal_val = math.trunc(decimal_val)
    decimal_val = decimal_val / 100
    final_dist = rounded_dist + decimal_val
    return final_dist

def pulse():
    global start_time
    led.value(True)
    output.value(1)
    start_time = utime.ticks_us()
    utime.sleep_ms(1000)
    output.value(0)
    led.value(False)
def first():
    global init
    if init == 0:
        uart.write(' ')
    init = init + 1

def send_distance(distance):
    pack = str(truncate(distance))
    first()
    uart.write(pack + "m")
    
    
# Input data and calc distance
def listening_branch(interrupt_pin):

    global end_time
    global start_time
    end_time = utime.ticks_us()-30
    time_diff = end_time - start_time
    time_diff = time_diff/1000000.0
    distance = speed_of_sound_75f * time_diff / 2
    print("Distance: {:.2f}".format(distance))
    send_distance(distance)
# Listening_branch pulse
interrupt_pin = Pin(16, Pin.IN, Pin.PULL_UP)
interrupt_pin.irq(handler=listening_branch, trigger=Pin.IRQ_FALLING)  # Interrupt routine
# Ping every 2 sec
while True: 
    pulse()
    #trigger_pin.value(1)
    utime.sleep_ms(inc)
    #trigger_pin.value(0)
    utime.sleep_ms(1000)


















