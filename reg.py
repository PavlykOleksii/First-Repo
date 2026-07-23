# this_is_string = "Hi there!"

# the_same_string = 'Hi there!'

# print(this_is_string == the_same_string)  # True

# text = """This is first line
# And second line
# Last third line"""

# song = '''Jingle bells, jingle bells
# Jingle all the way
# Oh, what fun it is to ride
# In a one horse open sleigh'''

# print(text)
# print(song)

# one_line_text = "Textual data in Python is handled with str objects, or strings. Strings are immutable sequences of Unicode code points. String literals are written in a variety of ways: single quotes, double quotes, triple quoted."
# print(one_line_text)

# one_line_text = "Textual data in Python is handled with str objects," \
#                 " or strings. Strings are immutable sequences of Unicode" \
#                 " code points. String literals are written in a variety " \
#                 " of ways: single quotes, double quotes, triple quoted."
# print(one_line_text)

# print(("spam " "eggs") == "spam eggs")

# one_line_text = ("Textual data in Python is handled with str objects,"
#                 " or strings. Strings are immutable sequences of Unicode"
#                 " code points. String literals are written in a variety "
#                 " of ways: single quotes, double quotes, triple quoted.")
# print(one_line_text)

# query = ("SELECT * "
#          "FROM some_table "
#          "WHERE condition1 = True "
#          "AND condition2 = False")
# print(query)

# print("Hello\tWorld")
# print("Hello my little\rsister")
# print("Hello\\World")

# print('It\'s a beautiful day')
# print("He said, \"Hello\"")

# s = "Hi there!"

# start = 0
# end = 7

# print(s.find("er", start, end)) # 5
# print(s.find("q")) # -1

# s = 'Some words'

# print(s.find("o"))
# print(s.rfind('o'))

# s = 'Some words'

# print(s.index("o"))
# print(s.rindex('o'))

# text = "hello world"
# result = text.split()
# print(result)  # Виведе: ['hello', 'world']

# text = "apple,banana,cherry"
# result = text.split(',')
# print(result)  # Виведе: ['apple', 'banana', 'cherry']

# list_of_strings = ['Hello', 'world']
# result = " ".join(list_of_strings)
# print(result)  # Виведе: 'Hello world'

# elements = ['earth', 'air', 'fire', 'water']
# result = ', '.join(elements)
# print(result)  # Виведе: 'earth, air, fire, water'

clean = '   spacious   '.strip()
print(clean) # spacious
