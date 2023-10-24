#https://github.com/raspberrypi/pico-micropython-examples/blob/master/irq/irq.py
# import machine
import utime
# import time
# import ustruct
from machine import Pin
init_time = utime.ticks_ms()


GP = Pin(28, Pin.IN, Pin.PULL_DOWN)
led = machine.Pin(25, machine.Pin.OUT)
led.value(True)
i = 0    
while GP.value() == 0:
   read = GP.value()
   time_out = utime.ticks_ms()
   if time_out - init_time > 4999:
       print('Timeout, no signal')
       break
led.value(False)
receive = utime.ticks_ms()
print(receive - init_time)

