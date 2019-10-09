

# Task 1

# Input
x={  
   'Opt':"10",
   "Columns":"2",
   'Cells':'5',
   'Key' : 'Key 2',
   "Parameters":[  
      {  
         "Key1":"Value 1"
      },
      {  
         "Key 2":"Value 1, Value 2, Value 3, Value 4, Value 5, Value 6, Value 7, Value 8, Value 9, Value 10,Value 11, Value 12, Value 13, Value 14, Value 15, Value 16, Value 17, Value 18, Value 19, Value 20,"
      }
]
}


#a=input('please entry key')
opt=x['Opt']
col=x["Columns"]
key=x['Key']
para0=x["Parameters"][0]
para1=x["Parameters"][1]['Key 2'].split(',')
print(para1)
para1.remove('')
n=97
c=0

for i in para1:
    s=para1[c].split(' ')
    a={key+chr(n):para1[c]+', '+s[-2]+' '+str(int(s[-1])+int(opt))}
    n+=1
    c+=1
    print(a)



# User Opt value as the increment counter. i.e. here take every 10th value.
# Use columns as number of Values that need to be extracted. Since columns = 2, u take Value 1 and Value 11
# Since Key = Key 2 Use data from "Key 2"


#Expected output
#"Key 2a": "Value 1, Value 11",
#"Key 2b": "Value 2, Value 12"



# task 2
# call api : http://api.population.io:80/1.0/countries
# get input as one alphabetic letter: A / B / c
# list out only those countries starting with that letter.


import json,ast
import urllib.request

url='http://api.population.io:80/1.0/countries'

with urllib.request.urlopen(url) as url:
    s=url.read()

s=s.decode('utf-8')


ct=ast.literal_eval(s)
ct=ct['countries']
letter=input('entry a letter to find countries')

lst=[]
for c in ct:
    if letter==c[0]:
        lst.append(c)
        

print(lst)




