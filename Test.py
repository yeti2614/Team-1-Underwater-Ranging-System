#ms
import machine
from machine import UART, Pin
import utime
uart = UART(0, 9600, tx=Pin(0), rx = Pin(1))
led = machine.Pin(25, machine.Pin.OUT) #Define the LED pin
led.value(True) #LED is turned on to indicate that the system is running
interrupt_pin = machine.Pin(0, machine.Pin.OUT)
value = 1234

while(True):
    utime.sleep_ms(1000)
    uart.write('1234')