import time
from sht11 import SHT11

#pin sck and data used, change with yours
sht = SHT11(sck=5, data=4)


while True:
    #read temperature and humidity
    tempOut = sht.temperature()
    humOut = sht.humidity()

    #print temperature and humidity
    print('Temperature: ', tempOut, '*C')
    print('Humidity: ', humOut, '%')
    time.sleep(1)
