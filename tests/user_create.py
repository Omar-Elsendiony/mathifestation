#!/usr/bin/python3
from tests.test_utility import *

"""
 Exec command
"""
def exec_command(my_console, the_command, last_lines = 1):
    my_console.stdout = io.StringIO()
    real_stdout = sys.stdout
    sys.stdout = my_console.stdout
    my_console.onecmd(the_command)
    sys.stdout = real_stdout
    lines = my_console.stdout.getvalue().split("\n")
    return "\n".join(lines[(-1*(last_lines+1)):-1])

"""
 Tests
"""
username="hthhht" 
first_name="omar" 
last_name="Else" 
email="omar.e" 
password="lolo"

result = exec_command(my_console, "create User username=\"{}\" first_name=\"{}\" last_name=\"{}\" email=\"{}\" password=\"{}\"".format(username, first_name, last_name, email, password))
if result is None or result == "":
    print("FAIL: No ID retrieved")


user_id = result

result = exec_command(my_console, "show User {}".format(user_id))
if result is None or result == "":
    print("FAIL: empty output")
    

    

print("OK", end="")

shutil.copy("tmp_console_main.py", "console.py")
shutil.copy("models/tmp__init__.py", "models/__init__.py")
