import inspect
import io
import sys
import cmd
import shutil

"""
 Cleanup file storage
"""
import os
file_path = "file.json"
if not os.path.exists(file_path):
    try:
        from models.engine.file_storage import FileStorage
        file_path = FileStorage._FileStorage__file_path
    except:
        pass
if os.path.exists(file_path):
    os.remove(file_path)

"""
 Backup console file
"""
if os.path.exists("tmp_console_main.py"):
    shutil.copy("tmp_console_main.py", "console.py")
shutil.copy("console.py", "tmp_console_main.py")

"""
 Backup models/__init__.py file
"""
if os.path.exists("models/tmp__init__.py"):
    shutil.copy("models/tmp__init__.py", "models/__init__.py")
shutil.copy("models/__init__.py", "models/tmp__init__.py")

"""
 Overwrite models/__init__.py file with switch_to_file_storage.py
"""
if os.path.exists("switch_to_file_storage.py"):
    shutil.copy("switch_to_file_storage.py", "models/__init__.py")


"""
 Updating console to remove "__main__"
"""
with open("tmp_console_main.py", "r") as file_i:
    console_lines = file_i.readlines()
    with open("console.py", "w") as file_o:
        in_main = False
        for line in console_lines:
            if "__main__" in line:
                in_main = True
            elif in_main:
                if "cmdloop" not in line:
                    file_o.write(line.lstrip("    ")) 
            else:
                file_o.write(line)

import console

"""
 Create console
"""
console_obj = "MATHSCommand"
for name, obj in inspect.getmembers(console):
    if inspect.isclass(obj) and issubclass(obj, cmd.Cmd):
        console_obj = obj

my_console = console_obj(stdout=io.StringIO(), stdin=io.StringIO())
my_console.use_rawinput = False
