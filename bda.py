import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


data=pd.read_csv("facebook.csv")
#print(data)

#print(data.tail(10))

# No of male/female user

dg=data['gender']
lg=dg.tolist()

male_gender=lg.count("male")
female_gender=lg.count("female")


gender=['male','female']
cgender=[male_gender,female_gender]
plt.bar(gender,cgender,label="gender")
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
plt.bar(lc,la,label="count")
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

# who got more likes 

d1=data[data.age<15]
#print(d1['userid'])

age_15=data['userid']
print(len(age_15))

# filter by city
dc=data['city']
lcity=dc['city'].tolist()
print(lcity)

"""lc=list()


la=list()
for i in range(0,100):
	lc.append(i)
	la.append(l1.count(i))
	#print(i,l1.count(i),sep=" ")
#print(lc,la)

x=np.arange(len(la))
plt.bar(lc,la,label="count")
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


# filter by mobile user

# filter by windows user

# filter by most likes
 