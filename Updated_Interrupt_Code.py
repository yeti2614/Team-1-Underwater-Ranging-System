#https://www.coderdojotc.org/micropython/advanced-labs/02-interrupt-handlers/
#https://docs.micropython.org/en/latest/index.html
#Import Needed Coding Processes
from machine import Pin
import micropython
import utime

#Communicate Function:
#This function is called when the GPIO pin goes high. When the pin goes high a time stamp is collected and a prompt is printed to the shell.
#When the GPIO pin is low, the system waits for an incoming signal and prints a prompt to the shell.
def MS_signal(MS):
            init_time = utime.ticks_ms() 
    
def communicate(GP):

            final_time = utime.ticks_ms()
            print(final_time)
            #dt=final_time-init_time
#spi response


GP = Pin(28, Pin.IN, Pin.PULL_DOWN) #Pin 28 is the tuned to the input and is brought low to wait for an incoming signal
MS = Pin(21, Pin.IN, Pin.PULL_UP) #Pin 28 is the tuned to the input and is brought low to wait for an incoming signal

led = machine.Pin(25, machine.Pin.OUT) #Define the LED pin
led.value(True) #LED is turned on to indicate that the system is running

GP.irq(handler=communicate, trigger=Pin.IRQ_RISING) #interrupt routine
MS.irq(handler=MS_signal, trigger=Pin.IRQ_RISING)

while True:
    utime.sleep(100)
#    print('Waiting for an incoming signal...')

SPI.send(1234, timeout = 5000)
    
