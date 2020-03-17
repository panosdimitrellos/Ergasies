import random
def arithmos_zevgariwn(lista_arithmwn):
  flag=False
  for i in range(0,29):
    y=29
    z=i+1
    while (z<y):
      if lista_arithmwn[i]+lista_arithmwn[y]+lista_arithmwn[z]==0:
        print lista_arithmwn[i],lista_arithmwn[y],lista_arithmwn[z]
        z+=1
        y-=1
        flag=True
      elif lista_arithmwn[i]+lista_arithmwn[y]+lista_arithmwn[z]<0:
        z+=1
      else:
        y-=1
      
  if flag==False:
    print "Den uparxei triada pou na kanei 0!" 

lista_arithmwn=[]
for i in range(30):
  lista_arithmwn.append(random.randint(-29,29))
lista_arithmwn.sort()
print lista_arithmwn
arithmos_zevgariwn(lista_arithmwn)
