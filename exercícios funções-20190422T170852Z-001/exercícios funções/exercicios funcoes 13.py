

def f13(a) :
  if (a>0):
    i = 1;
    j = 0;
    b = (a/2);
  while (i <= a):
    if (a % i==0):
        print ("É divisivel por ",i)
        i = i+1;
        j = j+1;
    if (i>=b):
        i = a;
        print ("É divisivel por" ,i)
        i = i+1;
        j = j+1;
    else:
        i = i+1;
  if(j==2):
    return True
  else:
    return False
