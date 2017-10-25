import os
import time


#Compatibility Finder, Crayon OS, and ComPy have all been designed, structured, and programmed by Kyle Fry (2017)
print("\n\n =====CRAYON OS v1.0.1=====")
time.sleep(3)
print("Initializing client...please wait.")
time.sleep(5)

file = input("\n \n Please type in the EXACT directory of your start-crayon.html file. This should be your folder you extracted. Please ensure that this file is located inside your C drive folder ONLY, and the name has not been changed: ")
print(file)

if file == "C:\crayon-start\start-crayon.html" :
	os.system("C:\crayon-start\start-crayon.html")
	print("File found, please refer to the HOW-TO-INSTALL.txt file for any help.")
else:
	print("ERROR: File cannot be found or retrieved try again.")
	print(file)
	
