from machine import Pin
from machine import UART
import utime
import ustruct

#referenced Jake's to write this code

uart_send = UART(1, 9600, tx=Pin(8), rx=Pin(9))
uart_rec = UART(1, 9600, tx=Pin(4), rx=Pin(5))

def read_values(data_receive): 
    data_received = uart_rec.read()
    data_received = bytes(data_received)
    data_normal = ustruct.unpack("<i", data_received)
    dist = data_normal[0]
    print(dist)
    display_LCD(dist)
    
    
def display_LCD(dist):
    dist_comp = ustruct.pack("<i", dist)
    uart_send.write(dist_comp)
       
data_receive = machine.Pin(10, machine.Pin.IN, machine.Pin.PULL_DOWN)
data_receive.irq(trigger= machine.Pin.RISING, handler=read_values)

while True:
    utime.sleep(100)