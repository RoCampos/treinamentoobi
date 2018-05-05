

# https://olimpiada.ic.unicamp.br/pratique/p1/2016/f1/tacos-bilhar/

N = int(input ())
cues = list(map(int,input().split()))

cues_size = [0] * 1000000

count = 0
for t in range(N):
	if cues_size[cues[t]] == 0:
		count += 2
		cues_size[cues[t]]=1
	else:
		cues_size[cues[t]] = 0

print (count)