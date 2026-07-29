# with open('text.txt', 'w') as fh:
#     fh.write("Some Data")

with open('text.txt', 'w') as fh:
    fh.write("first line\nsecond line\nthird line")

with open('text.txt', 'r') as fh:
    lines = [el.strip() for el in fh.readlines()]

print(lines)
