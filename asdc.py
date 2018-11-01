#!/usr/bin/python3
import os, module

print('[!] Made by CrimsonTorso [!]\n')
module.clear()
print('Welcome to ASDC!')
print('1 - Check Permissions')
print('2 - Quit')
raw_input = ('Please input a number: ')
if raw_input == '1':
	module.clear()
	print('Checking Permissions!')
	responce = os.system("dsa.msc")
if raw_input == '2':
	module.clear()
	print('Quitting!')
