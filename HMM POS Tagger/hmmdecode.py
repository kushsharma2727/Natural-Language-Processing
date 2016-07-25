from collections import defaultdict
import sys
import math

dict1=defaultdict()
dict2=defaultdict()

dict3=defaultdict()
dict4=defaultdict()

def insert(strline):
    if(strline.__contains__("Emission Probability")):
        arr=strline.split(" ")
        word=arr[2]
        tag=arr[3]
        if word not in dict1:
            dict1[word]={}
            dict1[word][tag]=float(arr[4])
        else:
            dict1[word][tag]=float(arr[4])
    elif(strline.__contains__("Transition Probability")):
        arr2=strline.split(" ")
        word2=arr2[2]
        tag2=arr2[3]
        if word2 not in dict2:
            dict2[word2]={}
            dict2[word2][tag2]=float(arr2[4])
        else:
            dict2[word2][tag2]=float(arr2[4])

def getMaxProb(i,v,token,dict3):
    maximum=-sys.maxint-1
    arg=''
    for k in dict3.get(i-1):
            if dict1.has_key(token):
                temp=dict1.get(token)
                if v in temp:
                    sum=dict3[i-1][k]+math.log(dict2[k][v])+math.log(dict1[token][v])
                    if maximum<sum:
                        maximum=sum
                        arg=k
                else:
                    sum=dict3[i-1][k]+math.log(dict2[k][v])
                    if maximum<(sum):
                        maximum=sum
                        arg=k
            else:
                sum=dict3[i-1][k]+math.log(dict2[k][v])
                if maximum<(sum):
                    maximum=sum
                    arg=k
    res=str(maximum)+" "+arg
    return res

def mostProbable(i,dict3):
    m=-sys.maxint-1
    t=''
    for k in dict3.get(i):
            if m<dict3[i][k]:
                m=dict3[i][k]
                t=k
    return t

def tag(line):
    start='##'
    tokens=line.split(' ')
    i=0
    dict3={}
    dict4={}
    for token in tokens:
        dict3[i]={}
        dict4[i]={}
        if i==0:
            if dict1.has_key(token):
                for k in dict1.get(token):
                    dict3[0][k]=math.log(float(dict2[start][k]))+math.log(float(dict1[token][k]))
            else:
                for k in dict2:
                    if k!='##':
                        dict3[0][k]=math.log(float(dict2[start][k]))
        else:
            if dict1.has_key(token):
                for k in dict1.get(token):
                    arr=getMaxProb(i,k,token,dict3)
                    res=arr.split(" ")
                    dict3[i][k]=float(res[0])
                    dict4[i][k]=res[1]
            else:
                for k in dict2:
                    if k!='##':
                        arr=getMaxProb(i,k,token,dict3)
                        res=arr.split(" ")
                        dict3[i][k]=float(res[0])
                        dict4[i][k]=res[1]
        i+=1

    j=0
    list1=[]
    for token in tokens:
        list1.append(token+"/"+mostProbable(j,dict3)+" ")
        j+=1

    return (''.join(list1))


def main():
    handle1 = open("hmmmodel.txt","r")
    while True:
        strline = handle1.readline()
        if not strline:
            break
        strline = strline.strip()
        insert(strline)
    handle1.close()
    handle2=open(sys.argv[1],"r")
    list2=[]
    while True:
        line = handle2.readline()
        if not line:
            break
        line = line.strip()
        list2.append(str(tag(line)))
    handle3=open("hmmoutput.txt","w")
    handle3.write('\n'.join(list2))
    handle3.close()
    handle2.close()

if __name__ == '__main__':
    main()