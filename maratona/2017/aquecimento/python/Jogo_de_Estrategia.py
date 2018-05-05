
#input
players_rounds = input()

all_rounds = input()
all_rounds = all_rounds.split ()

#players
J = int(players_rounds.split ()[0])
#rounds
R = int(players_rounds.split ()[1])

#players scores
players = [0] * J

#contols the better score
score = 0

#winner
winner = 0

#for each player
for j in range(len(players)):
    #count his score
    score_j = 0
    for i in range(j,(R*J), J):
        score_j = score_j + int(all_rounds[i])
    
    #if the score of player j is better then
    #the previous j, then update the winner
    if score_j >= score:
        score = score_j
        winner = j
    
#printing the weinner
print (winner+1)