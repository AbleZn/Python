# -*- coding: UTF-8 -*-
# Q007
# Created by JKChang
# Wed, 31/05/2017, 15:34
# Tag: extract file extension
# Description: Write a Python program to accept a filename from the user and print the extension of that. 
fileName = raw_input('please input a fileName: ')
s = fileName.split('.')
print 'extension of the file is:', s[-1]