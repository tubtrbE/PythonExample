#pip install pymysql 
#pip install pyserial
#open the rasberry uart port => sudo nano /boot/config.txt => dtoverlay=uart1~5
#dmesg | grep tty : you can see the uart port status

#import pymysql
#import serial
import time

#ser = serial.Serial("/dev/ttyS0",9600, timeout=1.0)

#ser = serial.Serial("/dev/ttyS0",57600) #when using the rasberry pi 3B use this
# let's setting the rasberry pi 4B and using the serial port 
#ser = serial.Serial("/dev/ttyAMA1",115200) #when using the rasberry pi 4B uart2
#ser = serial.Serial("/dev/ttyAMA2",115200) #when using the rasberry pi 4B uart3
#ser = serial.Serial("/dev/ttyAMA3",115200) #when using the rasberry pi 4B uart4
#ser = serial.Serial("/dev/ttyAMA4",115200) #when using the rasberry pi 4B uart5
data_test = "L230F340R120"

data_left = []
data_front = []
data_right = []

try:
    while True:

        byte_test = bytes(data_test, 'utf-8')
        #byte_sonic = ser.read() #stm32 give sonic data to the rasberry use the uart
        data_sonic = byte_sonic.decode('utf-8')
        
        if data_sonic == 'L':
            num = 0
            while num < 3:
                
                byte_sonic = ser.read() #stm32 give sonic data to the rasberry use the uart
                data_sonic = byte_sonic.decode('utf-8')
                data_left.append(data_sonic)
                num = num+1

        if data_sonic == 'F':
            num = 0
            while num < 3:
                               
                byte_sonic = ser.read() #stm32 give sonic data to the rasberry use the uart
                data_sonic = byte_sonic.decode('utf-8')
                data_front.append(data_sonic)
                num = num+1                
   
        if data_sonic == 'R':
            num = 0
            while num < 3:
                   
                byte_sonic = ser.read() #stm32 give sonic data to the rasberry use the uart
                data_sonic = byte_sonic.decode('utf-8')
                data_right.append(data_sonic)
                num = num+1


        print(data_left)
        print(data_front)
        print(data_right)
       
        del data_left[0:]
        del data_front[0:]
        del data_right[0:]
#        data = input() #read the keyboard input and return to the value to the 'data'
#        byte_data = bytes(data, 'utf-8')
#        ser.write(byte_data)
#        print(byte_data)
        
#        print(data_sonic)
#        if data == 0:
#            data_odometry = ser.read()
#            print(data_odometry)        
        

        time.sleep(0.1) # sleep(1) == 1sec
#        print(data_sonic)


        
except KeyboardInterrupt:
            pass
    
ser.close()