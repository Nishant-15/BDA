import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


data=pd.read_csv("facebook.csv", encoding= 'unicode_escape')
#print(data)

#print(data.tail(10))

# No of male/female user

dg=data['gender']
lg=dg.tolist()

male_gender=lg.count("male")
female_gender=lg.count("female")


gender=['male','female']
cgender=[male_gender,female_gender]
plt.bar(gender,cgender,color=['orange','blue','green','yellow','red'],align = 'center',label="gender")
plt.title("Number of users")
plt.xlabel('Genders')
plt.ylabel('count')
plt.legend(shadow=True)
plt.show()


d1=data[data.age>12]
l1=d1['age'].tolist()
lc=list()
la=list()
for i in range(0,100):
	lc.append(i)
	la.append(l1.count(i))
	#print(i,l1.count(i),sep=" ")
#print(lc,la)

x=np.arange(len(la))
plt.bar(lc,la,label="count",color=['orange','blue','green','yellow','red'],align = 'center')
plt.xticks(x,lc,label="Age")
plt.title("Age Classification")
plt.xlabel('age')
plt.ylabel('count')
plt.legend(shadow=True)
N=120
plt.gca().margins(x=0)
plt.gcf().canvas.draw()
tl = plt.gca().get_xticklabels()
maxsize = max([t.get_window_extent().width for t in tl])
m = 0.2 # inch margin
s = maxsize/plt.gcf().dpi*N+2*m
margin = m/plt.gcf().get_size_inches()[0]

plt.gcf().subplots_adjust(left=margin, right=1.-margin)
plt.gcf().set_size_inches(s, plt.gcf().get_size_inches()[1])
plt.show()

d1=data[data.age<15]
#print(d1['userid'])

age_15=data['userid']
print(len(age_15))

# filter by city
dc=data['city'].tolist()
sdc=set(dc)
loc=[]
sdc=list(sdc)
for i in sdc:
	loc.append(dc.count(i))
x=np.arange(len(loc))
plt.plot(sdc,loc,label="city")
plt.xticks(x,sdc,rotation=90,label="city")
plt.title("City wise Classification")
plt.xlabel('city')
plt.ylabel('count')
plt.show()

"""lc=list()


la=list()
for i in range(0,100):
	lc.append(i)
	la.append(l1.count(i))
	#print(i,l1.count(i),sep=" ")
#print(lc,la)

x=np.arange(len(la))
plt.bar(lc,la,label="count",color=['orange','blue','green','yellow','red'],align = 'center')
plt.xticks(x,lc,label="Age")
plt.title("Age Classification")
plt.xlabel('age')
plt.ylabel('count')
plt.legend(shadow=True)
N=120
plt.gca().margins(x=0)
plt.gcf().canvas.draw()
tl = plt.gca().get_xticklabels()
maxsize = max([t.get_window_extent().width for t in tl])
m = 0.2 # inch margin
s = maxsize/plt.gcf().dpi*N+2*m
margin = m/plt.gcf().get_size_inches()[0]

plt.gcf().subplots_adjust(left=margin, right=1.-margin)
plt.gcf().set_size_inches(s, plt.gcf().get_size_inches()[1])
plt.show()"""


# top five users with maximum friends
dc=data['friend_count'].tolist()
dc.sort(reverse=True)
maxfc=[]
uid=['2090699',
'1660276',
'1926655',
'1685573',
'1386477'
]
for i in range(5):
	maxfc.append(max(dc))
	dc.remove(max(dc))


	
x=np.arange(len(maxfc))
plt.plot(uid,maxfc,label="likes")
plt.xticks(x,uid,rotation=90,label="uid")
plt.title("top five user with maximum friends")
plt.xlabel('UserId')
plt.ylabel('count')
plt.show()

# filter by windows user

# filter by most likes
dc=data['likes_received'].tolist()
dc.sort(reverse=True)
maxfc=[]
uid=['1674584',
'1441676',
'1715925',
'2063006',
'1053087'
]
for i in range(5):
	maxfc.append(max(dc))
	dc.remove(max(dc))


	
x=np.arange(len(maxfc))
plt.bar(uid,maxfc,label="Likes count",color=['orange','blue','green','yellow','red'],align = 'center')
plt.xticks(x,uid,rotation=90,label="User Id")
plt.title("top five user with maximum likes")
plt.xlabel('UserId')
plt.ylabel('count')
plt.legend(shadow=True)
plt.show() 

"""
#fake acount detection

dc=d1=data[data.age>85]
l1=d1['age'].tolist()
lc=list()
la=list()
print(len(l1))"""
