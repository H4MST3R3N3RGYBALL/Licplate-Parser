#!/bin/python
import subprocess
import re
def main():
	#tmp_user_v = str(raw_input('What is the file name for the video as a .mp4?: '))
	tmp_user_v = 'test.mp4'
	caller = 'alpr -j ' + tmp_user_v + '> standout.licplate'
	subprocess.call(caller, shell=True)
	licplate()

def licplate():
	#useri = str(raw_input("What file do you want to parse?: "))
	useri = 'standout.licplate'
	file = open(useri, 'r')
	writeFile = open('plateout.licplate', 'a')
	for line in file:
		x = line
		x = x.split('results')
		x = x[2]
		x = x.split('{')
		for y in x:
			#y = y.split('')
			z = str(y)
			if "\"plate\"" in z:
				z = z.split('\"matches_template\"')

				print z[0]#, '\n'
				writeFile.write(z[0])

def regex():
	file = open('standout.licplate', 'r')
	
	for line in file:
		regex = r"(\{\"plate\"\:\"*.{1,8}\,\"confidence\":[0-9]{2}\.[0-9]{6})"
		matches = re.findall(regex, line, re.MULTILINE)
		for matche in matches:
			print matche
		
		if len(matches) != 0:
			print '-' * 40

		

if __name__ == '__main__':
	regex()