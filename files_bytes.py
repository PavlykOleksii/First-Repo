# with open('raw_data.bin', 'wb') as fh:
#     fh.write(b"Hello world!")

# byte_str = "some text".encode()
# print(byte_str)

numbers = [0,128,255]
byte_numbers = bytes(numbers)
print(byte_numbers)