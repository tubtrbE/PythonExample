data_test = "L230F340R120"

byte_test = bytes(data_test, 'utf-8')
print(data_test)
data_sonic = byte_test.decode('utf-8')
print(byte_test)


print(data_test[0])
print(data_test[1])
print(byte_test[0])
print(byte_test[1])
