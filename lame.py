#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# enable debugging
import cgitb
import platform

cgitb.enable()

print "Content-Type: text/plain;charset=utf-8"
print

print "Hello Moon!\n\n"
print "Rendered on:", platform.uname()[1]
