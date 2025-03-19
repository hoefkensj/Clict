import os
import sys
from logging import exception
from re import escape,findall
from pathlib import Path
from configparser import ConfigParser,ExtendedInterpolation,BasicInterpolation,RawConfigParser



# import inspect
# class Config(Clict):
# 	__module__ = Clict
# 	__qualname__ = "ClictConfig"
# 	__version__ = '0.2.01'
# 	_self: ConfSelf
#
# 	def __init__(__s, *a, **k):
# 		path = k.get('path')
# 		if not k.pop('ischild', False):
# 			k['isroot'] = True
# 			if (len(a) == 1) * (not k.get('path', False)):
# 				if (isinstance(a[0], str) + (isinstance(a[0], Path))):
# 					path = a[0]
# 			k['path'] = path
#
# 		__s.__args__(*a)
# 		__s.__kwargs__(**k)
#
# 		__s.__load__()
#
# 	def __self__(__s, *a, **s):
# 		self = s.pop('self', None)
# 		path = s.get('path')
# 		isroot = s.get('isroot')
# 		if isinstance(self, ConfSelf):
# 			__s._self = self
# 		else:
# 			s['path'] = path
# 			if isroot:
# 				s['root'] = path
# 			__s._self = ConfSelf(**s)
#
# 	def __kwargs__(__s, **k):
#
# 		__s.__self__(self=k.pop('self', {}), path=k.pop('path', Path()), isroot=k.pop('isroot', False))
# 		super().__kwargs__(**k)
#
#
#
#
#
from dataclasses import dataclass,field
class First:
	sub:int
	level : int=1 #assigning value here makes it a class variable?

	def __init__(s,*a):
		if len(a)>1:
			s.sub=a[1]
		if len(a)>0:
			s.level+=a[0]

@dataclass
class notFirst:
	sub:int
	level : int=field(default=1)



spacing=0, 10, 40, 50, 80, 90, 120, 130, 160, 170, 200, 210, 240, 250
def printf(v,e,c=[0],d='-'):
	string ='\x1b[2A\x1b[G'+ d * 250 + '\n'
	string += '\x1b[{x}G{v}\x1b[{x}G({e})'.format(v=v, e=e, x='{}')
	print(string.format(*spacing[c[0]*5:]),end ='')
	c+=[1]
	c[0]=sum(c)%2
string=''
w=10
F1 = First()
printf(F1.level,1)
First.level=10
printf(F1.level,10)
F2 = First(1)
printf(F2.level,11)
First.level=20
printf(F1.level,20)
printf(F2.level,11)

F2 = First() #two should nt matter
printf(F1.sub,1)
First.level+=2
printf(3,3)
F2.level+=1 		#makes it an instalce variable
printf(3,4)
First.level+=10
printf(13,4)
F2.level+=100
printf(113,4)
First.level='help'
lprint(113,51)
F1.level='helping'
lprint(113,51)
First=notFirst
F1 = First('test')
F2 = First('ikkel',2) #two should nt matter
lprint(1,2,d='#')
First.level+=2
lprint(3,50)
F2.level+=1 		#makes it an instalce variable
lprint(3,51)
First.level='help'
lprint(13,51)
F1.level+=100
lprint(113,51)
F1.level='help'
lprint(113,51)

F1 = notFirst('test',2)
F2 = notFirst('ikkel',2,3) #two should nt matter
sprint(1,1)
notFirst.sub+=2
sprint(3,3)
F2.sub+=1 		#makes it an instalce variable
sprint(3,4)
notFirst.sub+=10
sprint(13,4)
F1.sub+=100
sprint(113,4)
# sprint(2,2)
# First.sub+=3
# sprint(5,5)
# F1.sub+=4
# First.sub+=230
# string=''
# string+='\x1b[{x}G{v}\x1b[{x}G({e})'.format(v=F1.level,e= 10.0    ,x='{}')
# string+='\x1b[{x}G{v}\x1b[{x}G({e})'.format(v=F2.level,e= 101    ,x='{}')
#
# string+='\x1b[{x}G{v}\x1b[{x}G({e})'.format(v=F1.sub,e= 23.4    ,x='{}')
# string+='\x1b[{x}G{v}\x1b[{x}G({e})'.format(v=F2.sub,e= 232    ,x='{}')
# print(string.format(*spacing))
# string='\n\n'

# F1 = notFirst('test')
# F2 = notFirst('ikkel',4) #two should nt matter
# string+='\x1b[{x}G{v}\x1b[{x}G({e})'.format(v=F1.level,e= 1    ,x='{}')
# string+='\x1b[{x}G{v}\x1b[{x}G({e})'.format(v=F2.level,e= 1    ,x='{}')
#
# string+='\x1b[{x}G{v}\x1b[{x}G({e})'.format(v=F1.sub,e= 2    ,x='{}')
# string+='\x1b[{x}G{v}\x1b[{x}G({e})'.format(v=F2.sub,e= 2    ,x='{}')
# print(string.format(*spacing))
#
# notFirst.level=10
# notFirst.sub=23
# F1.level=10.0  		#makes it an instalce variable
# F1.sub=23.4 			#makes it an instalce variable
# string=''
# string+='\x1b[{x}G{v}\x1b[{x}G({e})'.format(v=F1.level,e= 10.0    ,x='{}')
# string+='\x1b[{x}G{v}\x1b[{x}G({e})'.format(v=F2.level,e= 10    ,x='{}')
#
# string+='\x1b[{x}G{v}\x1b[{x}G({e})'.format(v=F1.sub,e= 23.4    ,x='{}')
# string+='\x1b[{x}G{v}\x1b[{x}G({e})'.format(v=F2.sub,e= 23    ,x='{}')
# print(string.format(*spacing))
# string+='\n'
# notFirst.level=101
# notFirst.sub=232
# string=''
# string+='\x1b[{x}G{v}\x1b[{x}G({e})'.format(v=F1.level,e= 10.0    ,x='{}')
# string+='\x1b[{x}G{v}\x1b[{x}G({e})'.format(v=F2.level,e= 101    ,x='{}')
#
# string+='\x1b[{x}G{v}\x1b[{x}G({e})'.format(v=F1.sub,e= 23.4    ,x='{}')
# string+='\x1b[{x}G{v}\x1b[{x}G({e})'.format(v=F2.sub,e= 232    ,x='{}')
# print(string.format(*spacing))