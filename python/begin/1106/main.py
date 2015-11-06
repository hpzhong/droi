#!/usr/bin/env python
# this is code for study pytone one day.
# date:  Fri Nov  6 15:33:20 CST 2015
# end


print 1 + int("1") # error 1 + "1"

# Python codes are usually 1/3 or 1/5 of the java code. 
# It means we can write less code in Python to achieve the same thing as in Java.
# open and read a file is very easy.
with open("myfile.txt") as f:
    print(f.read())

# study from: http://thepythonguru.com/getting-started-with-python/
# Who uses python:
#
#    Python is used by many large organization like Google, NASA, Quora, HortonWorks and many others.
#
#    Okay what i can start building in python ?
#
#    Pretty much anything you want. For e.g
#
#    GUI application.
#    Create Websites.
#    Scrape data from website.
#    Analyse Data.
#    System Administration Task.
#    Game Development.
#    and many more.

#int 
print int("0b11", 0) # 0 is auto set. 2 is manually.
print int("0b11", 2) # 0 is auto set. 2 is manually.
print int("0x11", 0) # 0 is auto set. 16 is manually.
print int("0x11", 16) # 0 is auto set. 16 is manually.
