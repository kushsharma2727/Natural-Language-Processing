from __future__ import division
from collections import defaultdict
import math
import os
import re
import sys

posdectSize = 0
negdectSize = 0
postruthSize = 0
negtruthSize = 0

fdictVec = open("nbmodel.txt", 'w')

posdectDict = defaultdict(int)
negdectDict = defaultdict(int)
postruthDict = defaultdict(int)
negtruthDict = defaultdict(int)

posdectDoc=0
postruthDoc=0
negdectDoc=0
negtruthDoc=0

dict1=defaultdict(int)
dict2=defaultdict(int)
dict3=defaultdict(int)
dict4=defaultdict(int)


x=set()

#path=os.getcwd()+"\op_spam_train"
for name_r, name_d, name_f in os.walk(sys.argv[1]):
    if len(name_d)==0:
        for f in name_f:
            if(name_r.__contains__("negative") and name_r.__contains__("deceptive")):
                negdectDoc += 1
            elif(name_r.__contains__("negative") and name_r.__contains__("truthful")):
                negtruthDoc +=1
            elif(name_r.__contains__("positive") and name_r.__contains__("deceptive")):
                posdectDoc +=1
            elif(name_r.__contains__("positive") and name_r.__contains__("truthful")):
                postruthDoc +=1



#path=os.getcwd()+"\op_spam_train"
for name_r, name_d, name_f in os.walk(sys.argv[1]):
    if len(name_d)==0:
        for f in name_f:
                     with open(os.path.join(name_r, f)) as info:
                         for para in info:
                             para=re.sub("[!?,.'\"-:;\n]", ' ', para)
                             st = para.split(" ")
                             if(name_r.__contains__("negative") and name_r.__contains__("deceptive")):
                                negdectSize += len(st)
                             elif(name_r.__contains__("negative") and name_r.__contains__("truthful")):
                                negtruthSize += len(st)
                             elif(name_r.__contains__("positive") and name_r.__contains__("deceptive")):
                                posdectSize += len(st)
                             elif(name_r.__contains__("positive") and name_r.__contains__("truthful")):
                                postruthSize += len(st)
                             for w in st:
                                if w is not '':
                                    w=w.lower()
                                    x.add(w)
                                    if(name_r.__contains__("negative") and name_r.__contains__("deceptive")):
                                        negdectDict[w] += 1
                                    elif(name_r.__contains__("negative") and name_r.__contains__("truthful")):
                                        negtruthDict[w] += 1
                                    elif(name_r.__contains__("positive") and name_r.__contains__("deceptive")):
                                        posdectDict[w] += 1
                                    elif(name_r.__contains__("positive") and name_r.__contains__("truthful")):
                                        postruthDict[w] += 1

def checklength1():
    size=0
    size1=len(x)
    size2=len(postruthDict)
    size3=len(negtruthDict)
    size4=len(postruthDict)
    size5=len(negtruthDict)


checklength1()

for word in x:
    if not postruthDict.has_key(word): postruthDict[word]=0
    if not negtruthDict.has_key(word): negtruthDict[word]=0
    if not posdectDict.has_key(word): posdectDict[word]=0
    if not negdectDict.has_key(word): negdectDict[word]=0


def checklength2():
    size=0
    size1=len(x)
    size2=len(postruthDict)
    size3=len(negtruthDict)
    size4=len(postruthDict)
    size5=len(negtruthDict)


checklength2()

logProbposdect = {}
logProbnegdect = {}
logProbpostruth = {}
logProbnegtruth = {}

for k in posdectDict:
    numerator =  posdectDict[k] + 1
    p = (numerator)/(posdectSize+len(x))
    logProbposdect[k] = p

for k in negdectDict:
    numerator = negdectDict[k] + 1
    p = (numerator)/(negdectSize+len(x))
    logProbnegdect[k] = p

for k in negtruthDict:
    numerator =  negtruthDict[k] + 1
    p = (numerator)/(negtruthSize+len(x))
    logProbnegtruth[k] = p

for k in postruthDict:
    numerator = postruthDict[k] + 1
    p = (numerator)/(postruthSize+len(x))
    logProbpostruth[k] = p


fdictVec.write("P.D.Prior "+str((posdectDoc+1)/(posdectDoc+negdectDoc+postruthDoc+negtruthDoc+1))+"\n")
fdictVec.write("N.D.Prior "+str((negdectDoc+1)/(posdectDoc+negdectDoc+postruthDoc+negtruthDoc+1))+"\n")
fdictVec.write("P.T.Prior "+str((postruthDoc+1)/(posdectDoc+negdectDoc+postruthDoc+negtruthDoc+1))+"\n")
fdictVec.write("N.T.Prior "+str((negtruthDoc+1)/(posdectDoc+negdectDoc+postruthDoc+negtruthDoc+1))+"\n")

fdictVec.write("Positive Deceptive Map")
fdictVec.write("\n")
for k in logProbposdect:
    fdictVec.write(k + " " + str(logProbposdect[k]) + "\n")
fdictVec.write("Negative Deceptive Map")
fdictVec.write("\n")
for k in logProbnegdect:
    fdictVec.write(k + " " + str(logProbnegdect[k]) + "\n")
fdictVec.write("Negative Truthful Map")
fdictVec.write("\n")
for k in logProbnegtruth:
    fdictVec.write(k + " " + str(logProbnegtruth[k]) + "\n")
fdictVec.write("Positive Truthful Map")
fdictVec.write("\n")
for k in logProbpostruth:
    fdictVec.write(k + " " + str(logProbpostruth[k]) + "\n")
