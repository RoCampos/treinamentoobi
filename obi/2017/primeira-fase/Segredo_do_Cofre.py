# https://olimpiada.ic.unicamp.br/pratique/p1/2017/f1/cofre/

#this solutions takes O(nˆ2) time

N, M = map(int, tuple(input().split()))

control_bar = list(map(int,input().split()))

moviments = list(map(int,input().split()))

count = [0] * 10

count[control_bar[0]] +=1

for i in range(1,len(moviments)):
	a = moviments[i-1]-1
	b = moviments[i]-1
	if a < b:
		for j in range(a+1, b+1):
			count[control_bar[j]] += 1
	else:
		for j in range(a-1, b-1,-1):
			count[control_bar[j]] += 1

print (' '.join(str(x) for x in count))