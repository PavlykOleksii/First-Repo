# with open('raw_data.bin', 'wb') as fh:
#     fh.write(b"Hello world!")

# byte_str = "some text".encode()
# print(byte_str)

# numbers = [0,128,255]
# byte_numbers = bytes(numbers)
# print(byte_numbers)

# print(chr(123) + " " + chr(124))


# s = "Привіт"

# utf8 = s.encode()
# print(f"UTF-8: {utf8}")

# utf16 = s.encode("utf-16")
# print(f"UTF-16: {utf16}")

# cp1251 = s.encode("cp1251")
# print(f"CP1251: {cp1251}")

# s_from_utf16 = utf16.decode("utf-16")
# print(s_from_utf16 == s)

# print(b'Hello world!'.decode('utf-16'))

# # Відкриття текстового файлу з явним вказівкам UTF-8 кодування
# with open('text.txt', 'r', encoding='utf-8') as file:
#     content = file.read()
#     print(content)

# byte_array = bytearray(b"Kill Bill")
# byte_array[0] = ord("B")
# byte_array[5] = ord("K")
# print(byte_array)

# byte_array = bytearray(b"Hello")
# byte_array.append(ord("!"))  
# print(byte_array)

# byte_array = bytearray(b"Hello World")
# string = byte_array.decode("utf-8")
# print(string)  # Виведе: 'Hello World'

# import shutil

# # Створення TAR.GZ архіву
# shutil.make_archive('example', 'gztar', root_dir='my_folder')
# shutil.unpack_archive('example.tar.gz')

# import shutil

# # Копіюємо файл
# source_file = '/path/to/source/file.txt'
# destination_dir = '/path/to/destination'
# shutil.copy(source_file, destination_dir)

# # Копіюємо всю директорію
# source_dir = '/path/to/source/directory'
# destination_dir = '/path/to/destination/directory'
# shutil.copytree(source_dir, destination_dir)
