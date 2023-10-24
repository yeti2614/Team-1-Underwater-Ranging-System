from machine import Pin
import machine
import struct
import utime

#notify slave
trigger_pin = machine.Pin(20, machine.Pin.OUT)
global start_time



def trigger_slave():
    global start_time
    trigger_pin(0)
    start_time = utime.ticks_us()

    utime.sleep_ms(1000)
    trigger_pin(1)
# start
def trigger_interrupt(interrupt_pin):
    global start_time
    stop = utime.ticks_us()
    print(stop-start_time)

#when slave is ready to send data
interrupt_pin = Pin(14, Pin.IN, Pin.PULL_UP)   
interrupt_pin.irq(handler=trigger_interrupt, trigger=Pin.IRQ_FALLING) #interrupt routine
    
while True:
    trigger_slave()
    utime.sleep_ms(2000)
