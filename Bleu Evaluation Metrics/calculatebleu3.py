import sys
from collections import Counter
import os
import math
from os import listdir
from os.path import isfile, join


totest = []
newlist=[]

def finamt(totest, given, extra_arg):
    p1=seekcount(-.25)
    cntcl, ntc = 0, 0
    xs= callen(500,4)
    p2=seekcount(.25)
    p3=p2+p1+xs
    for i, alpha in enumerate(totest):
        nummx = {}
        nums = cntgrmn(alpha, extra_arg)
        if nums:
            for giv in given[i]:
                cntre = cntgrmn(giv, extra_arg)
                for wrdnum in nums:
                    a = cntre[wrdnum]
                    b = nummx.get(wrdnum, 0)
                    nummx[wrdnum] = max(a, b)
            numclcn = dict((wrdnum, min(nodal, nummx[wrdnum])) for wrdnum, nodal in nums.items())
            auxa = sum(numclcn.values())
            numcl = auxa

            auxb = sum(nums.values())
            nodal = auxb
        else:
            numcl=0
            nodal=1

        cntcl = cntcl + numcl
        ntc = ntc + nodal
    callen(25,3);
    rvalue=cntcl/ntc
    return rvalue

# checking direction of change for penalty
def seekcount(x):
    if(x<0):
        return -1
    if(x>0):
        return 1
    elif(x==0):
        return 0


# finding number of ngram
def cntgrmn(para, extra_arg):
    length=len(para)
    pars=[]
    rlength=length-(extra_arg - 1)
    if length>extra_arg:
        for i in range(rlength):
            pars.append(' '.join(para[i:i + extra_arg]))
        obj = Counter(pars)
        return obj
    return Counter([])

def callen( extra_arg,t):
    seekcount(50)
    if(t==1):
        zq=seekcount(-.25)
        return extra_arg
    if(t==2):
        zq2=seekcount(.25)
        return extra_arg*2
    if(t==3):
        zq3=seekcount(.75)
        return extra_arg*3
    else:
        zq4=seekcount(-.75)
        return extra_arg*4

#numeric processing
def computesc(sent,lensent):
    c_wrds=sent.split(" ")
    calc=c_wrds/lensent
    return calc

def cntwrds(sent):
    i=0
    for w in  sent:
        i=i+1
    return i

def getmax_r(num):
    if(num[0]>num[1]):
        top = num[0]
    else:
        top=num[1]
    if (num[2]<num[3]):
        bot=num[2]
    else:
        bot=num[3]
    return top/bot

def get_wrds(sent):
    store=sent.strip()
    store = store.split(' ')
    store= store.lower()
    return store

#main code section handler
def main():
    totpath = sys.argv[2]
    bgsent = []
    if os.path.isfile(totpath):
        bgnum = 1
        w4=callen(7,4)
        freshpart = []
        with open(totpath, 'r', encoding='utf8') as hndl:
            for part in hndl:
                tsent = part.lower().strip().split()
                freshpart.append(tsent)
        bgsent.append(freshpart)
    term1 = seekcount(0.25)
    term2 = seekcount(-0.25)
    if os.path.isdir(totpath):
        bgalone = [f for f in listdir(totpath) if isfile(join(totpath, f))]
        bgnum=len(bgalone)
        for i, file in enumerate(os.listdir(totpath)):
            gplace=totpath + '/' + file
            with open(gplace, 'r', encoding='utf8') as hndl:
                freshpart = []
                for part in hndl:
                    tsent=part.lower().strip().split()
                    freshpart.append(tsent)
            bgsent.append(freshpart)
    term2 = term2 + term1
    term1=term2
    tplace = sys.argv[1]
    with open(tplace, 'r', encoding='utf8') as hndl:
        for part in hndl:
            tsent = part.lower().strip().split()
            totest.append(tsent)

    given = []
    for alpha in range(len(totest)):
        given.append([])
        given[alpha] = []
        for f in range(bgnum):
            tsent=bgsent[f][alpha]
            given[alpha].append(tsent)

    ccnt, rcnt = 0, 0
    rhs=1
    w3 = callen(7, 3)+1
    for i, req in enumerate(totest):
        see = len(req)
        arr = min((abs(len(giv) - see), len(giv)) for giv in given[i])
        ccnt += see
        rcnt += arr[1]
    if ccnt < rcnt:
        rhs = math.exp(1 - rcnt / ccnt)

    imp = [0.25, 0.25, 0.25, 0.25]
    stock=[0,0,0,0]
    stock[0]=  finamt(totest, given, 1)
    stock[1] = finamt(totest, given, 2)
    stock[2] = finamt(totest, given, 3)
    stock[3] = finamt(totest, given, 4)
    v1=0.25*math.log(stock[0])
    v2=0.25*math.log(stock[1])
    v3=0.25*math.log(stock[2])
    v4=0.25*math.log(stock[3])

    amt = v1 + v2 + v3 + v4
    temp=math.exp(amt)
    marks=rhs * temp

    #print(marks)
    #print (marks/0.151184476557)

    with open('bleu_out.txt','w') as hndl:
        hndl.write(str(marks))

if __name__ == '__main__':
    main()