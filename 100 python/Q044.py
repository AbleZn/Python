# Q044
# Created by JKChang
# 28/04/2017, 14:59
# Description: Write a program which accepts a string as input to print "Yes" if the string is "yes" or "YES" or "Yes",
#              otherwise print "No".

x = raw_input('Input:  ')
if x.upper() == "YES":
    print x.lower().capitalize()
else:
    print "No"
