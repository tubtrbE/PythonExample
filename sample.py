sum = 300
temp_sum = '[3, {:04d}]'.format(sum)
return_sum = bytes(temp_sum, 'utf-8')
ser.write(return_sum)
print(byte)
