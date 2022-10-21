num=int(input())
a = []
totalnum = 0
totalscore = 0
for i in range(num):
  row = input().split(" ")
  #totalnum += int(row[0])
  #for k in range(1,len(row)):
    #totalscore+=int(row[k])
  a.append(row)
#average = totalscore/totalnum

result = []
for k in a:
  total = 0
  count = 0
  for j in range(1,len(k)):
    total += int(k[j])
  average = total/int(k[0])
  for f in range(1, len(k)):  
    if(int(k[f])>average):
      count+=1
  ratio = count/int(k[0]) * 100
  result.append(ratio)
    
    
for m in result:
  print('{:.3f}'.format(m)+"%")
  

