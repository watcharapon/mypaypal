import sys
import time
import requests
from datetime import datetime, timedelta

yesterday = datetime.today()-timedelta(days=1)
date_from =  yesterday.strftime("%Y-%m-01")

records=[]

port='81'
ip_address='49.231.197.187'
url_download='form/Download'

# connect to machine
url = "http://%s%s/%s" % (ip_address,(port and ":"+str(port) or ""),url_download)
print( 'url',url)
user='1019'
password='1019'
date_to = time.strftime("%Y-%m-%d")

# param needs to query
args=sys.argv
limit=int(args[1])
rank=range(1,limit)
post_data={
    'sdate':date_from,
    'edate':date_to,
    'period':0,
    'uid':[rank],
    #'uid':[range(1,500)],
    }

r = requests.post(url, post_data, auth=(user, password))

# get data
res = r.content

res = res.decode('tis-620') # this is fix encoding

print('res ', res)

records = []
count=0
for r in res.split('\r\n'):
    count+=1
    l = r.split('\t')
    if len(l)!=5:
        continue
    code = l[0]

    dt = l[2]

print("range ", rank)
print("total ", count)
