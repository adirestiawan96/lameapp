#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# enable debugging
import cgitb
import platform

cgitb.enable()

print ("Content-Type: text/plain;charset=utf-8")
print ()

print ("Hello Moon!\n")
print ("Hello Sun!\n\n")
print ("Rendered on:", platform.uname()[1])
