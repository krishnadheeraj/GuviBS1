n=int(input())
if(n%4==0):
  print('yes')
elif(n%100==0 and n%400==0):
  print('yes')
else:
  print('no')
