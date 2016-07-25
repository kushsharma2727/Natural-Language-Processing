from collections import defaultdict
import sys
import os
import math


global posdectDoc
posdectDoc=0
global negdectDoc
negdectDoc=0
global postruthDoc
postruthDoc=0
global negtruthDoc
negtruthDoc=0

#def make(f):
temp = {}
posdectDoc=0
negdectDoc=0
postruthDoc=0
negtruthDoc=0

global postruthProbs
postruthProbs = {}
global negtruthProbs
negtruthProbs = {}
global posdectProbs
posdectProbs = {}
global negdectProbs
negdectProbs = {}

dict1=defaultdict(int)
dict2=defaultdict(int)
dict3=defaultdict(int)
dict4=defaultdict(int)

d = open("nbmodel.txt",'r')
for l in d:
		if(l.__contains__("Positive Deceptive Map")): i = 1
		elif(l.__contains__("Negative Deceptive Map")): i = 2
		elif(l.__contains__("Positive Truthful Map")): i = 3
		elif(l.__contains__("Negative Truthful Map")): i = 4
		elif(l.__contains__("P.T.Prior")):
			kk=l.split(" ")
			postruthDoc+=float(kk[1].strip("\n"))
		elif(l.__contains__("N.T.Prior")):
			kk=l.split(" ")
			negtruthDoc+=float(kk[1].strip("\n"))
		elif(l.__contains__("P.D.Prior")):
			kk=l.split(" ")
			posdectDoc+=float(kk[1].strip("\n"))
		elif(l.__contains__("N.D.Prior")):
			kk=l.split(" ")
			negdectDoc+=float(kk[1].strip("\n"))
		else :
			arr = l.split(" ")
			if(i==1): posdectProbs[arr[0]] = arr[1]
			elif(i==2): negdectProbs[arr[0]] = arr[1]
			elif(i==3): postruthProbs[arr[0]] = arr[1]
			elif(i==4):	negtruthProbs[arr[0]] = arr[1]

def classify(basepath, f, postruthProbs,negtruthProbs,posdectProbs,negdectProbs,postruthDoc,negdectDoc,negtruthDoc,posdectDoc):
	toDiv = open(os.path.join(basepath,f),'r')
	postruthP = 0
	negtruthP = 0
	posdectP = 0
	negdectP = 0
	for para in toDiv:
		st = para.split(" ")

		for w in st:
			try:
				if(w in postruthProbs):
					postruthP = postruthP + math.log(float(postruthProbs[w].strip("\n")),10)
			except:
				pass

			try:
				if(w in negtruthProbs):
					negtruthP = negtruthP + math.log(float(negtruthProbs[w].strip("\n")),10)
			except:
				pass

			try:
				if(w in posdectProbs):
					posdectP = posdectP + math.log(float(posdectProbs[w].strip("\n")),10)
			except:
				pass

			try:
				if(w in negdectProbs):
					negdectP = negdectP + math.log(float(negdectProbs[w].strip("\n")),10)
			except:
				pass

	postruthP = postruthP + math.log (float(postruthDoc),10)
	negtruthP = negtruthP + math.log (float(negtruthDoc),10)
	posdectP = posdectP + math.log (float(posdectDoc),10)
	negdectP = negdectP + math.log (float(negdectDoc),10)

	if(postruthP>=negtruthP and postruthP>=posdectP and postruthP>=negdectP):
		return "Positive Truthful"
	elif(negtruthP>=postruthP and negtruthP>=posdectP and negtruthP>=negdectP):
		return "Negative Truthful"
	elif(posdectP>=negtruthP and posdectP>=postruthP and posdectP>=negdectP):
		return "Positive Deceptive"
	elif(negdectP>=negtruthP and negdectP>=posdectP and negdectP>=postruthP):
		return "Negative Deceptive"
	else:
		return "Positive Truthful"



#make("nbmodel.txt")
size1=0
size2=0
size3=0
size4=0

def checklength1():
	size=0
	size2=len(postruthProbs)
	size3=len(negtruthProbs)
	size4=len(postruthProbs)
	size5=len(negtruthProbs)


checklength1()

with open("nboutput.txt",'w') as fdict:
	#path="C:\Python27\op_spam_train\\negative_polarity\deceptive_from_MTurk\\fold1"
	for name_r, name_d, name_f in os.walk(sys.argv[1]):
		if len(name_d)==0:
			for f in name_f:
				if f.__contains__("LICENSE") or f.__contains__("README"): continue
				pn=classify(name_r,f,postruthProbs,negtruthProbs,posdectProbs,negdectProbs,postruthDoc,negdectDoc,negtruthDoc,posdectDoc)
				if(pn.__contains__("Positive") and pn.__contains__("Truthful")):
					fdict.write("truthful positive "+os.path.join(name_r,f)+"\n")
				elif(pn.__contains__("Positive") and pn.__contains__("Deceptive")):
					fdict.write("deceptive positive "+os.path.join(name_r,f)+"\n")
				elif(pn.__contains__("Negative") and pn.__contains__("Truthful")):
					fdict.write("truthful negative "+os.path.join(name_r,f)+"\n")
				elif(pn.__contains__("Negative") and pn.__contains__("Deceptive")):
					fdict.write("deceptive negative "+os.path.join(name_r,f)+"\n")
