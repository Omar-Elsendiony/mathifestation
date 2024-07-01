#!/usr/bin/python3
from tests.test_utility import *
import MySQLdb
"""
 Tests
"""
username="ntnteh"
first_name="omar" 
last_name="Else" 
email="omar.e" 
password="lolo"


result = exec_command(my_console, "create User username=\"{}\" first_name=\"{}\" last_name=\"{}\" email=\"{}\" password=\"{}\"".format(username, first_name, last_name, email, password))
if result is None or result == "":
    print("FAIL: No ID retrieved")



user_id = result
title = "Do you want to see the maths?"
body = "Do not wish the last element of the list to be displayed."


result = exec_command(my_console, "create Question user_id=\"{}\" title=\"{}\" body=\"{}\"".format(user_id, title, body))
print(result)
if result is None or result == "":
    print("FAIL: empty output")

question_id = result

username="bbtetew"
first_name="mariam" 
last_name="soso" 
email="omar.e" 
password="lolo"


result = exec_command(my_console, "create User username=\"{}\" first_name=\"{}\" last_name=\"{}\" email=\"{}\" password=\"{}\"".format(username, first_name, last_name, email, password))
if result is None or result == "":
    print("FAIL: No ID retrieved")

new_user_id = result

question_id = question_id
user_id = new_user_id
body = "Your question is pretty vague, can you elaborate?"

result = exec_command(my_console, "create Answer question_id=\"{}\" user_id=\"{}\" body=\"{}\"".format("iot", user_id, body))
print(result)

print("OK", end="")

shutil.copy("tmp_console_main.py", "console.py")
shutil.copy("models/tmp__init__.py", "models/__init__.py")
