import machine
import utime


#https://how2electronics.com/how-to-use-adc-in-raspberry-pi-pico-adc-example-code/
analog_value = machine.ADC(28)
li = []
i = 0
while i < 1000:
    reading = analog_value.read_u16()     
    print("ADC: ",reading)
    utime.sleep(0.0001)
    li.append(reading)
    
    i += 1
sum = 0
for i in range(1000):
    sum += li[i]
avg = sum/1000

#https://docs.micropython.org/en/v1.15/library/utime.html
time = 0
counter = 0
freq = 0
while reading - avg > 0.01:
    reading = analog_value.read_u16()     
    print("ADC: ",reading)
    utime.sleep(0.0001) #read values at 10000 samples per second (0.0001 seconds per cycle)
while counter < 2: #starts right after the average value is acheived, and counts hitting two averages
    reading = analog_value.read_u16()     
    print("ADC: ",reading)
    utime.sleep(0.0001) 
    time += 0.0001 #count cycles between a full period
    if reading - avg < 0.01:
        counter += 1 #exits loop once a full period has been reached
freq = 1/time #take 1/seconds passed to get the frequency of the signal      
print("The frequency of the signal is " + str(freq) + " Hz.")    

