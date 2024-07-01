#!/usr/bin/python3
from tests.test_utility import *
import MySQLdb
"""
 Tests
"""
username="gtege"
first_name="omar" 
last_name="Else" 
email="omar.e" 
password="lolo"

# try:
result = exec_command(my_console, "create User username=\"{}\" first_name=\"{}\" last_name=\"{}\" email=\"{}\" password=\"{}\"".format(username, first_name, last_name, email, password))
if result is None or result == "":
    print("FAIL: No ID retrieved")
# except Exception as e:
#     exit(1)
#     print(e)


user_id = result

title = "What is an even number?"
body = "I am trying to understand what an even number is. Can someone explain it to me?"
rating = 6
result = exec_command(my_console, "create Review user_id=\"{}\" body=\"{}\" rating=\"{}\"".format(user_id, body, rating))
print(result)
if result is None or result == "":
    print("FAIL: empty output")

review_id = result

result = exec_command(my_console, "show Review {}".format(review_id))
print(result)


print("OK", end="")

shutil.copy("tmp_console_main.py", "console.py")
shutil.copy("models/tmp__init__.py", "models/__init__.py")
