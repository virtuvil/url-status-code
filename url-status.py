#!/usr/bin/python
import urllib.request
import pyfiglet																																																																		
import subprocess as sp

banner = pyfiglet.figlet_format("URL-Status Checker")
print(banner)

name = input("Enter the file name ")
file = open(name, "r")
print("\n Opening file for reading.",end = "\r")
print("Please be patient ")
Lines = file.readlines()
count = 0
for line in Lines:
    count += 1
    code = urllib.request.urlopen(line.strip()).getcode()
    print("URL {} Status code is {}".format(line.strip(),code))
