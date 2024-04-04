import random
ismlar=[]
raqamlar=[]
ismvaraqam=[]
a=input('5 ta isim kiriting\n').split()
b=input("5ta telefon raqam kiriting\n").split(' ')
d=input("telefon raqam kiriting\n")
for i in a:
    if i.isalpha():
        ismlar.append(i)
    else:
        print("ERROR")
for l in b:
    if l.isdigit():
        raqamlar.append(l)
    else:
        print("ERROR")
for k in raqamlar:
    if k == d:
        ismvaraqam.append(k)
    else:
        print("ERROR")
c=random.choice(ismlar)
ismvaraqam.append(c)
print(raqamlar)
print(ismlar)
print(ismvaraqam)