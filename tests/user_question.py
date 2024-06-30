#!/usr/bin/python3
from test_utility import *

"""
 Tests
"""
username="loooooooooo"
first_name="omar" 
last_name="Else" 
email="omar.e" 
password="lolo"

result = exec_command(my_console, "create User username=\"{}\" first_name=\"{}\" last_name=\"{}\" email=\"{}\" password=\"{}\"".format(username, first_name, last_name, email, password))
if result is None or result == "":
    print("FAIL: No ID retrieved")


user_id = result

title = "What is an even number?"
body = "I am trying to understand what an even number is. Can someone explain it to me?"

result = exec_command(my_console, "create Question user_id=\"{}\" title=\"{}\" body=\"{}\"".format(user_id, title, body))
print(result)
if result is None or result == "":
    print("FAIL: empty output")

question_id = result

result = exec_command(my_console, "show Question {}".format(question_id))
print(result)
if result is None or result == "":
    print("FAIL: empty output")    

print("OK", end="")

shutil.copy("tmp_console_main.py", "console.py")
shutil.copy("models/tmp__init__.py", "models/__init__.py")
