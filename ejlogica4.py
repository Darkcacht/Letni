#!/usr/bin/env python
# coding: utf-8

import os
clear = lambda: os.system('clear')
clear()

pal = raw_input("Ingrese una palabra: ")

if pal == pal[::-1]:
    print("Es un palíndromo!")
else:
    print("No es un palíndromo")
