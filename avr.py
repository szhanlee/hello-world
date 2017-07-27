
# -*- coding: utf-8 -*

'''
#6-11
import string

def ip_2_int():
	Fir = input('Enter an ip address:\n')
	ip_ad = Fir.split('.')
	ip = list(ip_ad)

	if len(ip) != 4:
		return 'Invalid ip'
	else:
		return int(ip[0])*256*256*256 + int(ip[1])*256*256 + int(ip[2])*256 + int(ip[3])

def int_2_ip():
	num_1 = input('Enter a number:\n')
	num = int(num_1)

	W_ = divmod(num,256**3)
	X_ = divmod(W_[1],256**2)
	Y_ = divmod(X_[1],256)
	Z = Y_[1]
	return '.'.join((str(W_[0]),str(X_[0]),str(Y_[0]),str(Z)))
	
	

if __name__ == '__main__':
	k = input('ip or int?\n')

	if k == 'ip':
		print(ip_2_int())
	elif k == 'int':
		print(int_2_ip())
	else:
		'Invalid option'

'''

'''
#6-12
import string

def findchr(string, char):
	re = ''.join(string)
	n = len(re)
	
	if char not in re:
		return '-1'
	else:
		for i in range(n):
			if re[i] == char:		
				return i
			else:
				continue
	
def rfindchr(string, char):
	re = ''.join(string)
	n = len(re)
	
	if char not in re:
		return '-1'
	else:
		for i in range(n):
			if re[i] == char:		
				return i
			else:
				continue

if __name__ == '__main__':
	string = input('Enter a string:\n')
	char = input('Enter a char to find:\n')
	print(findchr(string,char))
'''

'''
import time
from datetime import *


Key = input('Enter:')
Log = []
count = 0

if Key.strip().lower() == 'e':
	Log.append(str(datetime.today()))
	print Log
	
else:
	print ('The alpha %s is not correct' % Key.strip()[i].lower())

'''

'''
#7-7
dic={1:'g',6:'i',4:'l',9:'y'}
new_keys = []
new_values = []

for i in range(len(dic)):
	new_keys.append(dic.values()[i])
	new_values.append(dic.keys()[i])
print (dict(zip(new_keys, new_values)))
'''


#7-8
import string


user_name = []
user_ID = []

def HR():
	prompt = """
(N)ew Employee Info
(Q)uit current process
"""

	done = True


	while True:
		Hint = input(prompt).strip()
		if  Hint[0].lower() == 'n':
			while done:				
				print_info()
				user_name.append(str(NAME))
				user_ID.append(str(ID))
				#print (user_name,user_ID)
				while True:							
					more = input('More names to log?(y/n):\n')
					if more == 'n':					
						#done = False
						return 'Name input completed.'					
					elif more == 'y':
						break
					else:
						print('Invalid option, try again')
		elif Hint[0].lower() == 'q':
			print ('Quit now')
			done = False
		else:
			print ('Please try again')



def print_info():

	# global Profile_name
	# global Profile_ID
	# Profile_name = []
	# Profile_ID = []
	#打印名字
	global NAME
	global ID
	
	dot = True
	while dot:
		flag = 0
		NAME = input('Please enter your name:\n')
		ID = input('Please enter your ID:\n')
		for i in range(len(str(NAME))):
			if str(NAME)[i] not in string.ascii_letters:
				flag = 1							
				break
			else:
				continue	
		#打印ID
		for j in range(len(str(ID))):
			if str(ID)[j] not in '0123456789':
				flag = 1
				break
			else:
				continue

		if flag != 0:
			print ('Invalid name or ID, try again')
		else:
			dot = False
			#return (Profile_ID.append((str(ID))), Profile_name.append((str(NAME))))
			


	



if __name__ == '__main__':
	print(HR())
	#print (dict(zip(user_name, user_ID))) 
	#按照ID排序
	print ([(value, key) for (key, value) in sorted([(value,key) for (key,value) in dict(zip(user_name, user_ID)).items()])])


























