#ms
from machine import Pin
import machine
import struct
import utime

#spi set up
cs = machine.Pin(17, machine.Pin.OUT)
sck_pin = machine.Pin(18, machine.Pin.OUT)
mosi_pin = machine.Pin(19, machine.Pin.OUT)
miso_pin = machine.Pin(16, machine.Pin.OUT)
spi = machine.SPI(0, baudrate=9600, polarity=0, phase=0, sck=sck_pin, mosi=mosi_pin, miso=miso_pin)

#notify slave
trigger_pin = machine.Pin(20, machine.Pin.OUT)
fakesignal = machine.Pin(15, machine.Pin.OUT) 


#set constant
speed_of_sound_75f = 1480

#function to send square wave
def trigger_slave():
    trigger_pin(0)
    utime.sleep_ms(10)
    trigger_pin(1)
    utime.sleep_ms(25)
    fakesignal(0)
    utime.sleep_ms(10)
    fakesignal(1)



    

#input data and calc distance
def spi_interrupt(interrupt_pin):
    utime.sleep_ms(50)

    value = read_float_from_spi() 
    distance = speed_of_sound_75f * value / 2
    print("Distance:", value)

#when slave is ready to send data
interrupt_pin = Pin(14, Pin.IN, Pin.PULL_UP)   
interrupt_pin.irq(handler=spi_interrupt, trigger=Pin.IRQ_FALLING) #interrupt routine



#read float
def read_float_from_spi():
    data = bytearray(8) 
    spi.readinto(data)
    return struct.unpack('f', data)[0]

#ping every 2 sec
while True:
    trigger_slave()
    utime.sleep_ms(2000)
