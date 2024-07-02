import random
i=1
s=0
while(i!=0):
    
    i=int(input("1-continue\n2-exit\nenter="))
    if i==0:
          break
    print("\n")
    r=random.randint(1,6)
    match(r):
        case 1:
            print("[   ]\n[ . ]\n[   ]")
        case 2:
            print("[.  ]\n[   ]\n[  .]")
        case 3:
            print("[ . ]\n[ . ]\n[ . ]")
        case 4:
            print("[. .]\n[   ]\n[. .]")
        case 5:
            print("[. .]\n[ . ]\n[. .]")
        case 6:
            print("[. .]\n[. .]\n[. .]")
        

