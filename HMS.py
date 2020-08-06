print("Program to make software which collect information of gym of three people")
def getdate():
    import datetime
    return datetime.datetime.now()
choice=input('what do you want to do lock or retrieve..?')
if choice.lower()=='lock':
 p=input('what do you want to lock...diet information or exercise information')
 if p.lower()=='diet':   
    n=input('whom diet information do you want to lock select any one from jp,hp,op')
    info=input('Enter information')
    if n=='jp':
        f=open('jpdiet.txt','a')
        k=str(getdate())+' '+ info
        f.write(k)
        f.close()
    elif n=='hp':
        f=open('hpdiet.txt','a')
        k=str(getdate())+ ' ' +info
        f.write(k)
        f.close()
    elif n=='op':
        f=open('opdiet.txt','a')
        k=str(getdate())+' '+ info
        f.write(k)
        f.close()
    else:
        print('Error:InvalidName')
 elif p.lower()=='exercise':
     n=input('whom exercise information do you want to lock select any one from jp,hp,op')
     info=input('Enter information')
     if n=='jp':
        f=open('jpexercise.txt','a')
        k=str(getdate())+' '+info
        f.write(k)
        f.close()
     elif n=='hp':
        f=open('hpexercise.txt','a')
        k=str(getdate())+' '+ info
        f.write(k)
        f.close()
     elif n=='op':
        f=open('opexercise.txt','a')
        k=str(getdate())+' '+ info
        f.write(k)
        f.close()
     else:
        print('Error:InvalidName')
 else:
      print('Error:InvalidInformation')
elif choice.lower()=='retrieve':
  p=input('what do you want to retrieve...diet information or exercise information')
  if p.lower()=='diet':   
    n=input('whom diet information do you want to retrieve select any one from jp,hp,op')
    if n=='jp':
        try:
         f=open('jpdiet.txt','r')
         print(f.read())
         f.close()
        except:
            print('File is Empty')
    elif n=='hp':
        try:
         f=open('hpdiet.txt','r')
         print(f.read())
         f.close()
        except:
            print('File is Empty')
    elif n=='op':
        try:
         f=open('opdiet.txt','r')
         print(f.read())
         f.close()
        except:
            print('File is Empty')
    else:
        print('Error:InvalidName')
  elif p.lower()=='exercise':
      n=input('whom exercise information do you want to retrieve select any one from jp,hp,op')
      if n=='jp':
        try:
         f=open('jpexercise.txt','r')
         print(f.read())
         f.close()
        except:
            print('File is Empty')
      elif n=='hp':
        try:
         f=open('hpexercise.txt','r')
         print(f.read())
         f.close()
        except:
            print('File is Empty')
      elif n=='op':
        try:
         f=open('opexercise.txt','r')
         print(f.read())
         f.close()
        except:
            print('File is Empty')
        
        
      else:
        print('Error:InvalidName')
  else:
      print('Error:InvalidInformation')
else:
    print('Error:InvalidChoice')

