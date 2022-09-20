# pip install pymysql
# pip install pyserial
# open the rasberry uart port => sudo nano /boot/config.txt => dtoverlay=uart1~5
# dmesg | grep tty : you can see the uart port status

from mimetypes import init
from serial import Serial
import time

# ser = serial.Serial("/dev/ttyS0",9600, timeout=1.0)

# ser = serial.Serial("/dev/ttyS0",57600) #when using the rasberry pi 3B use this
# let's setting the rasberry pi 4B and using the serial port
# ser = serial.Serial("/dev/ttyAMA1",115200) # when using the rasberry pi 4B uart2
# ser = serial.Serial("/dev/ttyAMA2",115200) #when using the rasberry pi 4B uart3
# ser = serial.Serial("/dev/ttyAMA3",115200) #when using the rasberry pi 4B uart4
# ser = serial.Serial("/dev/ttyAMA4",115200) #when using the rasberry pi 4B uart5
ser = Serial('COM4', 115200)  # when using the Window Desktop

data_list = []
data_left = []
data_front = []
data_right = []

byte_sonic = ser.read()  # stm32 give sonic data to the rasberry use the uart
print(byte_sonic)


def init_data():
    del data_list[0:]
    del data_left[0:]
    del data_front[0:]
    del data_right[0:]


try:
    while True:

        byte_sonic = ser.read()  # stm32 give sonic data to the rasberry use the uart
        data_sonic = byte_sonic.decode("utf-8")

        time.sleep(0.1)

        # makelist
        try:
            if data_sonic == '<':
                while data_sonic != '>':
                    data_list.append(data_sonic)
                    byte_sonic = ser.read()
                    data_sonic = byte_sonic.decode("utf-8")
            data_list.append(data_sonic)

        except:
            init_data()
            continue

        # checking
        data_len = len(data_list)

        if data_len != 14:
            init_data()

        else:
            if data_list[0] != '<':
                init_data()
            else:
                if data_list[13] != '>':
                    init_data()
                else:
                    if data_list[1] != 'L' or data_list[5] != 'F' or data_list[9] != 'R':
                        init_data()
                    else:

                        L_List = data_list[2:4]

                        for i in L_List:
                            if int(i) > 9 or int(i) < 0:
                                init_data()

                        F_List = data_list[6:8]
                        for i in F_List:
                            if int(i) > 9 or int(i) < 0:
                                init_data()

                        R_List = data_list[10:12]
                        for i in R_List:
                            if int(i) > 9 or int(i) < 0:
                                init_data()

        data_left = data_list[1:5]
        data_front = data_list[5:9]
        data_right = data_list[9:13]

        print(data_left)
        print(data_front)
        print(data_right)
        init_data()

# i have to handle data immediately
# so i dont need time.sleep(0.01)
# sleep(1) == 1sec

except KeyboardInterrupt:
    pass

ser.close()
