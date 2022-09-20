import serial
import time

# 테스트용 문자열 데이터 입니다

# 1번 : 옳은 문자열이 들어오는 경우
data_test = "<L230F340R120>"

# 2번 : 데이터의 길이가 맞지 않을 경우
data_test2 = "<L230F34R120>"

# 3번 : 데이터의 길이는 맞지만 내용이 다를 경우
data_test3 = "<L2A0F340R120>"

# 시리얼 통신시에 byte 로 주고 받으므로 byte 를 while loop 내부에서 처리 할 수 있도록 byte 변환 하였습니다.
byte_test = bytes(data_test, 'utf-8')
byte_test2 = bytes(data_test2, 'utf-8')
byte_test3 = bytes(data_test3, 'utf-8')


list_test = list(data_test)
# 문자열 데이터의 길이를 받는 변수 len
len = len(data_test)
print(len)

count = 0

test_list = []
data_left = []
data_front = []
data_right = []

while True:

    num = 0
    if byte_test[num] == '<':
        while byte_test[num] != '>':
            test_list

            num += 1

    del data_left[0:]
    del data_front[0:]
    del data_right[0:]
