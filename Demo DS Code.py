#ds
import machine
from machine import UART
from machine import Pin
import utime
import ustruct
import struct
uart1 = UART(0, 9600, tx=Pin(0), rx = Pin(1), parity = None, stop = 1)
    
start_time=0
end_time=0
# start
def trigger_interrupt(trigger_pin):
    global start_time
    start_time = utime.ticks_us()
# stop
def sensor_interrupt(lb_pin):
    global end_time
    global start_time
    end_time = utime.ticks_us()
    send_time_difference(start_time, end_time)
# communicate
def send_time_difference(start_time, end_time):
    time_diff = end_time - start_time
    print(time_diff)
    pack=ustruct.pack("<i", time_diff)
    expect_pin(0)  
    uart1.write(pack)
    expect_pin(1)  
#pins
trigger_pin = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_UP)
lb_pin = machine.Pin(16, machine.Pin.IN, machine.Pin.PULL_UP)
expect_pin = machine.Pin(2, machine.Pin.OUT)

trigger_pin.irq(trigger=machine.Pin.IRQ_FALLING, handler=trigger_interrupt)
lb_pin.irq(trigger=machine.Pin.IRQ_FALLING, handler=sensor_interrupt)
while(True):
    utime.sleep(100)