import urllib2
import json
import datetime

cur_date=datetime.datetime.now()

def compare_lists(list1,list2):
    c=0
    for i in list1:
        if i in list2:
            c+=1
    return c
nums=[] 
for i in range (10):
    x=int(input("Eisagetai arithmo: \n")) 
    nums.insert(i,x)
    i+=1
print(nums)
EpitHmeras=[] 
Hmerominia=[] 
for i in range(31):
    cur_date= cur_date - datetime.timedelta(days=1)
    date_str= cur_date.strftime("%d-%m-%Y")
    Hmerominia.insert(i,date_str)
    url='http://applications.opap.gr/DrawsRestServices/kino/drawDate/%s.json'%date_str
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    data = response.read()
    data=json.loads(data)
    draws= data['draws']['draw']
    r=[]
    for d in draws:
        tmp=d["results"]
        r.append(compare_lists(nums,tmp))
    EpitHmeras.insert(i,0)
    for j in range(180): 
        if r[j] > 4: 
            EpitHmeras[i] = EpitHmeras[i] + 1
epituxies = 0
for i in range(30):
    if EpitHmeras[i] > EpitHmeras[i+1]:
        epituxies = EpitHmeras[i]
        PayDay = i
print 20*"-"
print("Oi perissoteres epituxies pou simiothikan einai: "),epituxies
print("H hmera tou mhna pou simiothikan oi epituxies autes einai: "),Hmerominia[PayDay]