#! /usr/bin/env python
# -*-coding:utf-8-*-

'		a pratice answer set		'

_author_	=	'	Shuzhan Li	'


#7-3(a)
'''
def seq():

	aDict = {'y': 'asdf', 'p': 'rte', 'v': 'asdger', 'b': 'sdf',  'a': 'ewry', 'c': 'aw'}
	n = len(aDict)
	aList = list(aDict.keys())
	values = aDict.values()
	for i in range(n-1,0,-1):
		for j in range(i):
			if aList[j] > aList[j+1]:
				aList[j], aList[j+1] = aList[j+1], aList[j]
	return aList
if __name__ == '__main__':
	print(seq())

#7-3(a)(b)
def seq():
	aDict = {'y': 'asdf', 'p': 'rte', 'v': 'asdger', 'b': 'sdf',  'a': 'ewry', 'c': 'aw'}
	for i in sorted(aDict):
		print (i, aDict[i])
	return 0

if __name__ == '__main__':
	print(seq())

#7-3(c)
def seq():
	aDict = {'y': 'asdf', 'p': 'rte', 'v': 'asdger', 'b': 'sdf',  'a': 'ewry', 'c': 'aw'}
	for i in sorted(aDict.values()):
		for j in aDict:
			if i == aDict[j]:
				print (j, i)
	

if __name__ == '__main__':
	print(seq())

'''

#7-4
'''
aList = [11,22,33,44,55,66,77]
bList = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqr', 'stu']

R_order = dict(zip(aList, bList))

print (R_order)
'''

#7-5
import time
from datetime import *

global state_dict
global time_log
global name
db = {}
state_dict = {}
time_log = []


def newuser():
	
	prompt = 'login desired:'
	while True:
		name = input(prompt)
		if name in db:
			prompt = 'name taken, try another:\n'
			continue
		else:
			break
	pwd = input('passwd:')
	db[name] = pwd
	now = datetime.today() #当前时间
	now_key = now.strftime('%Y-%m-%d %H:%M:%S') #格式化日期以便转换
	time_log.append(now_key) #记录此次登录的日期
	#print (db, str(now_key), time_log,'newuser part')


def olduser():
	global flag
	
	name = input('login:')
	pwd = input('passwd:')
	passwd = db.get(name)	
	flag = str(name)
	#current_t = datetime.today()
	#current_t.strftime('%Y-%m-%d %H:%M:%S')
	
	if passwd == pwd:
		print ('Welcome back', name)
		#print(datetime.strptime(state_dict[str(passwd)], '%Y-%m-%d %H:%M:%S'))# + timedelta(hours=4)  >= current_t
			#print ('You already logged in at: %s ' % state_dict[pwd])
	else:
		print ('Incorrect user name or passwd')
	
	return db
	
def user_log():
	
	global state_pwd
	
	if choice == 'n':	
		state_dict.update(dict(zip(db.keys(), time_log))) #更新‘名字-登录时间’的字典
		state_pwd = list(state_dict.values()) 
		print (time_log, db, state_dict, state_pwd)
	elif choice == 'e':
		#if time_log[-1] != '':
		current_t = datetime.today()
		#print (state_pwd[-1])
		print ('Current time: %s' % current_t)
		strp_time = datetime.strptime(str(state_dict[flag]), '%Y-%m-%d %H:%M:%S') + timedelta(hours=4) #str转化为datetime，并加入时间差
		if strp_time >= current_t: #与当前时间比较
			print ('You already logged in at: %s ' % state_dict[flag])				
		else:
			print('Time-out, please log in again.')
		#time_log.append(str(current_t))
	
def showmenu():
	prompt = '''
(N)ew User Login
(E)xisting User Login
(Q)uit

Enter choice:'''

	done = False
	global choice
	
	while not done:
		chosen = False
		while not chosen:
			try:
				choice = input(prompt).strip()[0].lower()
			except (EOFError, KeyboardInterrupt):
				choice = 'q'
			print ('\nYou picked: [%s]' % choice)
			if choice not in 'neq':
				print ('Invalid option, try again')
			else:
				chosen = True

		if choice == 'q': done = True
		if choice == 'n':			
			newuser()
			user_log()
		if choice == 'e': 
			olduser()
			user_log()
		

if __name__ == '__main__':
	showmenu()








