# pip install pymysql
# pip install pyserial
# open the rasberry uart port => sudo nano /boot/config.txt => dtoverlay=uart1~5
# dmesg | grep tty : you can see the uart port status

from serial import Serial
from threading import Thread
import time

# ser = serial.Serial("/dev/ttyS0",9600, timeout=1.0)
# ser = serial.Serial("/dev/ttyS0",57600) #when using the rasberry pi 3B use this
# let's setting the rasberry pi 4B and using the serial port
# ser = serial.Serial("/dev/ttyAMA1",115200) # when using the rasberry pi 4B uart2
# ser = serial.Serial("/dev/ttyAMA2",115200) #when using the rasberry pi 4B uart3
# ser = serial.Serial("/dev/ttyAMA3",115200) #when using the rasberry pi 4B uart4
# ser = serial.Serial("/dev/ttyAMA4",115200) #when using the rasberry pi 4B uart5
ser = Serial('COM6', 115200)  # when using the Window Desktop


# buffer for (Producer Consumer Model)
odo_list = []
serial_data = ser.read()  # stm32 give odo data to the rasberry use the uart


def init_odo():
    del odo_list[0:]

# Uart input Thread (Producer Thread) STM32 <> Pi Client


def Uart_input():
    try:
        while True:

            serial_data = ser.read()  # stm32 give odo data to the rasberry use the uart
            data_uart = serial_data.decode("utf-8")
            # when using this code block the sleep (because sleep is onlt use for the testing)
            time.sleep(0.1)

            # makelist Buffer
            try:

                if data_uart == '<':
                    while data_uart != '>':
                        odo_list.append(data_uart)
                        serial_data = ser.read()
                        data_uart = serial_data.decode("utf-8")
                    odo_list.append(data_uart)

            except:
                pass

            print(odo_list)

    except KeyboardInterrupt:
        pass

    ser.close()  # at the end of thread serial close

# Uart Consumer Thread Client <> DB Server


# Uart output Thread
def Uart_output():

    while True:
        data = input()
        byte_data = bytes(data, 'utf-8')
        ser.write(b'[1,300]')
#        ser.write(byte_data)
        print(byte_data)


if __name__ == "__main__":
    START, END = 0, 100000000
    result = list()
    th_uart_input = Thread(target=Uart_input, name='th_uart_input')
    th_uart_output = Thread(target=Uart_output, name='th_uart_output')

    th_uart_input.start()
    th_uart_output.start()

    th_uart_input.join()
    th_uart_output.join()
