r=int(input("Enter row: "))
c=int(input("Enter column: "))
m=[]
for i in range(r):
	l=[]
	for j in range(c):
		v=int(input())
		l.append(v)
	m.append(l)
print("\n\n")
m1=[]
s=0
for i in range(r):
	l1=[]
	for j in range(s+1):
		l1.append(m[i][j])
	m1.append(l1)
	s+=1
print(m1)