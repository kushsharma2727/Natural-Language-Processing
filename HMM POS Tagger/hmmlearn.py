from __future__ import division
import sys
from collections import defaultdict

dict1=defaultdict()
dict2=defaultdict()
dict3=defaultdict()

dict4=defaultdict()
dict5=defaultdict()
dict6=defaultdict()

def str2example(strline):
	words = []
	tags = []
	tokens = strline.split(' ')
	length=len(tokens)
	i=0
	start='##'
	for token in tokens:
		token = token.split('/')
		e = len(token)
		if e == 2:
			words.append(token[0])
		else:
			words.append('/'.join(token[0:e-1]))
		tags.append(token[e-1])

		if i == 0:
			if start not in dict4:
				dict4[start]={}
				dict4[start][tags[i]]=1
			else:
				temp=dict4.get(start)
				if tags[i] not in temp:
					dict4[start][tags[i]]=1
				else:
					dict4[start][tags[i]]+=1
			if start not in dict5:
				dict5[start]=1
			else:
				dict5[start]+=1

		elif i<length:
			if tags[i-1] not in dict4:
				dict4[tags[i-1]]={}
				dict4[tags[i-1]][tags[i]]=1
			else:
				temp=dict4.get(tags[i-1])
				if tags[i] not in temp:
					dict4[tags[i-1]][tags[i]]=1
				else:
					dict4[tags[i-1]][tags[i]]+=1
			if tags[i-1] not in dict5:
				dict5[tags[i-1]]=1
			else:
				dict5[tags[i-1]]+=1

		if words[i] not in dict1:
			dict1[words[i]]={}
			dict1[words[i]][tags[i]]=1
		else:
			temp=dict1.get(words[i])
			if tags[i] not in temp:
				dict1[words[i]][tags[i]]=1
			else:
				dict1[words[i]][tags[i]]+=1

		if tags[i] not in dict2:
			dict2[tags[i]]=1
		else:
			dict2[tags[i]]+=1

		i+=1

def emission_prob():
	list1=[]
	for k in dict1:
		dict3[k]={}
		for v in dict2:
			temp=dict1.get(k)
			if v in temp:
				dict3[k][v]=float(dict1[k][v])/float(dict2[v])
				list1.append("Emission Probability "+k+" "+v+" "+str(dict3[k][v]))
	handle2=open("hmmmodel.txt","w")
	handle2.write('\n'.join(list1))
	handle2.close()

def transition_prob():
	list2=[]
	for k in dict4:
		dict6[k]={}
		for v in dict5:
			temp=dict4.get(k)
			if v not in temp:
				dict6[k][v]=float(1)/float(dict5[k]+len(dict5))
				list2.append("Transition Probability "+k+" "+v+" "+str(dict6[k][v]))
			else:
				dict6[k][v]=float(dict4[k][v])/float(dict5[k]+len(dict5))
				list2.append("Transition Probability "+k+" "+v+" "+str(dict6[k][v]))
	handle3=open("hmmmodel.txt","a")
	handle3.write('\n')
	handle3.write('\n'.join(list2))
	handle3.close()

def main():
	handle1 = open(sys.argv[1],"r")
	while True:
		strline = handle1.readline()
		if not strline:
			break
		strline = strline.strip()
		str2example(strline)
	emission_prob()
	transition_prob()
	handle1.close()

if __name__ == '__main__':
	main()