
#entrada

jogadas=input()

pontos=input()
pontos = pontos.split ()

#players
J = int(jogadas.split ()[0])
#rounds
R = int(jogadas.split ()[1])

#players points
jogadores = [0] * J

#contols the better score
soma = 0

#winner
vencedor = 0

#for each player
for j in range(len(jogadores)):
    
    #count his score
    soma_j = 0
    for i in range(j,(R*J), J):
        soma_j = soma_j + int(pontos[i])
    
    #if the score of player j is better then
    #the previous j, then update the winner
    if soma_j >= soma:
        soma = soma_j
        vencedor = j
    
#printing the weinner
print (vencedor+1)