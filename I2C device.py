import machine

sdaPIN=machine.Pin(16) #for ESP32
sclPIN=machine.Pin(17)
expect_pin = machine.Pin(0, machine.Pin.OUT)
expect_pin(1)

i2c=machine.I2C(0, sda=sdaPIN, scl=sclPIN, freq=10000)

devices = i2c.scan()
if len(devices) == 0:
    print("No i2c device !")
else:
    print('i2c devices found:',len(devices))
    for device in devices:
        print("At address: ",hex(device))