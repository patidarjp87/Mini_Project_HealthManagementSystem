print("Program to make software which collect information of gym of three people")
def getdate():
    import datetime
    return datetime.datetime.now()
choice=input('what do you want to do lock or retrieve..?')
if choice.lower()=='lock':
 p=input('what do you want to lock...diet information of exercise information')
 if p.lower()=='diet':   
    n=input('whom diet information do you want to lock select any one from jp,hp,op')
    info=input('Enter information')
    if n=='jp':
        f=open('f1.txt','a')
        k=str(getdate())+' '+ info
        f.write(k)
        f.close()
    elif n=='hp':
        f=open('f2.txt','a')
        k=str(getdate())+ ' '+info
        f.write(k)
        f.close()
    elif n=='op':
        f=open('f3.txt','a')
        k=str(getdate())+' '+ info
        f.write(k)
        f.close()
    else:
        print('Error:InvalidName')
 elif p.lower()=='exercise':
     n=input('whom exercise information do you want to lock select any one from jp,hp,op')
     info=input('Enter information')
     if n=='jp':
        f=open('f11.txt','a')
        k=str(getdate())+' '+info
        f.write(k)
        f.close()
     elif n=='hp':
        f=open('f22.txt','a')
        k=str(getdate())+' '+ info
        f.write(k)
        f.close()
     elif n=='op':
        f=open('f33.txt','a')
        k=str(getdate())+' '+ info
        f.write(k)
        f.close()
     else:
        print('Error:InvalidName')
 else:
      print('Error:InvalidInformation')
elif choice.lower()=='retrieve':
  p=input('what do you want to retrieve...diet information of exercise information')
  if p.lower()=='diet':   
    n=input('whom diet information do you want to retrieve select any one from jp,hp,op')
    if n=='jp':
        try:
         f=open('f1.txt','r')
         print(f.read())
         f.close()
        except:
            print('File is Empty')
    elif n=='hp':
        try:
         f=open('f2.txt','r')
         print(f.read())
         f.close()
        except:
            print('File is Empty')
    elif n=='op':
        try:
         f=open('f3.txt','r')
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
         f=open('f11.txt','r')
         print(f.read())
         f.close()
        except:
            print('File is Empty')
      elif n=='hp':
        try:
         f=open('f22.txt','r')
         print(f.read())
         f.close()
        except:
            print('File is Empty')
      elif n=='op':
        try:
         f=open('f33.txt','r')
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

