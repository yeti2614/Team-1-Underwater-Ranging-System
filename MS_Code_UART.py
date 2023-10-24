#ms
from machine import Pin
import machine
import struct
import utime

#spi set up
#ds
import machine
from machine import UART, Pin
uart = UART(0, 9600, tx=Pin(0), rx = Pin(1))
led = machine.Pin(25, machine.Pin.OUT) #Define the LED pin
led.value(True) #LED is turned on to indicate that the system is running
#value = 1234

#notify slave
trigger_pin = machine.Pin(14, machine.Pin.OUT)
fakesignal = machine.Pin(15, machine.Pin.OUT) 


#set constant
speed_of_sound_75f = 1480

#function to send square wave
def trigger_slave():
    trigger_pin(0)
    utime.sleep_ms(10)
    trigger_pin(1)
    utime.sleep_ms(50)

    fakesignal(0)
    utime.sleep_ms(10)
    fakesignal(1)
    utime.sleep_ms(10)
    fakesignal(0)



#input data and calc distance
def uart_interrupt(interrupt_pin):
    message = uart.read()
    utime.sleep(1)
    decoded_message = message.decode('utf-8')
    val = int(decoded_message)
    print(val)
    val = val % (10^4)
    print(val)
    distance = speed_of_sound_75f * val / 2
    print("Distance:", distance)

#when slave is ready to send data
interrupt_pin = Pin(16, Pin.IN, Pin.PULL_UP)   
interrupt_pin.irq(handler=uart_interrupt, trigger=Pin.IRQ_FALLING) #interrupt routine


#ping every 2 sec
while True:
    trigger_slave()
    utime.sleep_ms(2000)

