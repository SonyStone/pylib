from sys import version_info
py3 = version_info[0] > 2

if py3:
    response = input("Please enter your name: ")
else:
    response = raw_input("Please enter your name: ")

print("Hello " + response)