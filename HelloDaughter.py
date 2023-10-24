#ds
import machine
from machine import UART
from machine import Pin
import utime
uart1 = UART(1, 9600, tx=Pin(4), rx = Pin(5))

    
interrupt_pin = machine.Pin(0, machine.Pin.IN, Pin.PULL_DOWN)
led = machine.Pin(25, machine.Pin.OUT) #Define the LED pin
led.value(True) #LED is turned on to indicate that the system is running

def pri(interrupt_pin):
    message = uart1.read()
    utime.sleep(1)
    decoded_message = message.decode('utf-8')
    val = int(decoded_message)
    print(type(val))
    print(val)
interrupt_pin.irq(handler=pri, trigger = Pin.IRQ_RISING)

while(True):
    utime.sleep(100)
