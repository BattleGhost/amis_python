x=[]
y=[]
isError = False
for i in range(8):
    a,b = [int(e) for e in input("Введіть координати(x,y) - ").split()]
    x.append(a)
    y.append(b)
for i in range(8):
    for j in range(8):
        if i!=j:
            if abs(x[i]-x[j])==abs(y[i]-y[j]) or x[i]==x[j] or y[i]==y[j]:
                print("YES")
                isError= True
                break
        if exitflag: break            
else: print("NO")
