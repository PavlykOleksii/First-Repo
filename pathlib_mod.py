# from pathlib import PurePath

# p = PurePath("/usr/bin/simple.jpg")
# print("Name: ",p.name)
# print("Suffix: ", p.suffix)
# print("Parent: ", p.parent)
# print(p.drive)

# from pathlib import Path

# p = Path("test1.txt")
# p.write_text("ADD text")
# print(p.read_text())
# print(p.exists())

# from pathlib import Path

# # Початковий шлях
# base_path = Path("/usr/bin")

# # Додавання додаткових частин до шляху
# full_path = base_path / "subdir" / "script.py"

# print(full_path)  # Виведе: /usr/bin/subdir/script.py

# from pathlib import Path

# # Перетворення відносного шляху в абсолютний
# relative_path = Path("test.txt")
# absolute_path = relative_path.absolute()

# current_working_directory = Path("E:\WebDir\Works\Python\python-help-solution\example_for_new_core\l04")
# relative_path = absolute_path.relative_to(current_working_directory)
# print(relative_path)
