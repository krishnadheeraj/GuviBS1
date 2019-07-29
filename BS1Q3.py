a=input()
b=['a','e','i','o','u','A','E','I','O','U']
c=['!','@','#','$','%','&','*','^','(',')','[',']','{','}']
for i in c:
  if(a in c or a.isdigit()==True):
    print('invalid')
    break
  elif(a in b):
    print('Vowel')
    break
  else:
    print('Consonant')
    break
