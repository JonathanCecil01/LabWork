import sys
submissions = {}
submissions =[]
'''
for i in range(0, 2):
    submission = input()
    listsub = submission.split(" ")
    submissions.append([listsub[0],int(listsub[1]), int(listsub[2]), listsub[3]])
'''
submissions = [['1', 2, 10, 'I'], ['3',1 , 11, 'C'], ['1', 2, 19, 'R'], ['1', 2, 21, 'C'], ['1', 1, 25, 'C']]
team = {}
team = dict(team)
p_time = {}
p_time = dict(p_time)
for i in submissions:
    team[i[0]] = 0
    p_time[i[1]] = 9999
    
for i in submissions:
    if i[3]=='C':
        team[i[0]]+=1
        if i[2]<p_time[i[1]]:
            p_time[i[1]] = i[2]
print(team, p_time)
scoreboard = {}
scoreboard = dict(scoreboard)

for i in submissions:
    if i[3]=='C' or i[3]=='I':
        scoreboard[i[0]] = [0, 0]

for i in submissions:
    if i[3]=='C':
        scoreboard[i[0]][0]+=1
        scoreboard[i[0]][1]+= i[2]-p_time[i[1]]
    elif i[3]=='I':
        scoreboard[i[0]][1]+=20
    
print(scoreboard)
for i in scoreboard:
    print(i, scoreboard[i])
         
        



       
        
