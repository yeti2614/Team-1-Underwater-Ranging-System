#ds
import machine
import utime
import struct

# SPI setup
cs = machine.Pin(17, machine.Pin.OUT)
sck_pin = machine.Pin(18, machine.Pin.OUT)
mosi_pin = machine.Pin(19, machine.Pin.OUT)
miso_pin = machine.Pin(16, machine.Pin.OUT)

spi = machine.SPI(0, baudrate=9600, polarity=0, phase=0, sck=sck_pin, mosi=mosi_pin, miso=miso_pin)


start_time = 0
end_time = 0

# start
def trigger_interrupt(pin):
    global start_time
    start_time = utime.ticks_us()

# stop
def sensor_interrupt(trigger_pin ):
    global end_time
    end_time = utime.ticks_us()
    send_time_difference()

# communicate
def send_time_difference():
    global start_time, end_time
    expect_pin(0)  
    time_diff = end_time - start_time
    send_float_over_spi(time_diff)
    expect_pin(1)  

# send a float value
def send_float_over_spi(value):
    data = struct.pack('f', float(value))
    spi.write(data)
    
#pins
trigger_pin = machine.Pin(20, machine.Pin.OUT)
interrupt_pin = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_UP)
expect_pin = machine.Pin(21, machine.Pin.OUT)

trigger_pin.irq(trigger=machine.Pin.IRQ_FALLING, handler=trigger_interrupt)
interrupt_pin.irq(trigger=machine.Pin.IRQ_FALLING, handler=sensor_interrupt)

# Main loop
while True:
    utime.sleep_ms(2000)
