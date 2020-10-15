import random 
import json
from prettytable import PrettyTable
# importing colors
with open('./color.json') as colors:
	colors = json.load(colors)
# importing all the teams of IPL from teams.json file
with open('./teams.json') as teams:
	teams = json.load(teams)

# welcome
print(colors['blue'], '-----------------------INDIAN PREMIUM LEAUGE--------------------------------------------------------','\n')
print(colors['red'],"___________________________BY 'HIMANSHU NAGAR_______________________________________________________",'\n')
print(colors['green'],'\<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< PRESS ENTER TO CONTINUE>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>','\n')
# pressing enter as input 
enter=input()

# list of runs
runs=[1,2,3,4,6]
balls_option=['leg spin','googly','off spin','arm ball','bouncer','leg cutter','out swinger','reverse swing','yorker','slower ball']
out=['run out','caught and bold','stumped','caught','bowled']
shots_option=['cut','flick','step out and hit','cover drive','drive','stright drive','helicopter','pull']
opponent_team=['CSK','MI','RCB','KKR','DC','RR','SRH','KXIP']

print(colors['white'],'chosse your team \n')

# show all teams for seletion
for show_teams in teams:
	print(show_teams)

# slection of p1 and p2
player_1=input('chosse your team    ').upper()
print('\n')
opponent_team.remove(player_1)
player_2=random.choice(opponent_team)
print('\n','\n')

def printTeams(player,team,color):
	print("--",colors[color],player,"--")
	print()
	for teamMember in teams[player]:
		print(teamMember)
	print()
	print()

printTeams(player_1,teams,"blue")
print(colors['white'],"\tVS")
print('\n')
printTeams(player_2,teams,"red")

def p1Batting(p1,p2):
	# p1 is batting team and p2 is balling team
	p1_total=0
	players_data={}
	# wickets are 11 and wicktes are started from 1 because we have list of batsmen and we have to select striker and non-striker by index [0] and [1] then we have to increment wicket+=1
	wickets=1
	batting_team=teams[p1]
	bowling_team=teams[p2]
	striker=batting_team[wickets-1]
	non_striker=batting_team[wickets]
	score_of_striker=0
	score_of_NONstriker = 0
	# adding striker and non-striker data to players data dict
	players_data[striker] = score_of_striker
	players_data[non_striker] = score_of_NONstriker
	overs=0
	print('\n\n\n')
	print(colors['white'],'\n\t',f'{striker} and {non_striker} has came on felid')
	# total overs in a match
	for over in range(1):
		# choosing a bowler
		bowler=random.choice(bowling_team)
		if wickets==11:
			break
		for Balls in range(1,7):
			print( '\n',colors['cyan'],'_'*200,colors['white'],'\n')
			print('\t'f'{bowler} is on bolwing',f'{striker} is on strike')
			run = 0

			# batting scoreboard
			batting_scoreboard = PrettyTable(['batsman','score_of_striker'])
			batting_scoreboard.add_row([f'* {striker}', score_of_striker ])
			batting_scoreboard.add_row([non_striker, score_of_NONstriker ])
			print(batting_scoreboard)
			print()

			# p1 total score
			total_batting_score = PrettyTable(['Batting Team','Total Score','Wickets'])
			total_batting_score.add_row([p1,p1_total,wickets-1])
			print(total_batting_score)
			print()

			# bowling scoreBoard
			bowling_scoreboard = PrettyTable(['bowler','balls','over'])
			bowling_scoreboard.add_row([bowler,Balls-1,over])
			print(bowling_scoreboard)
			print()

			print('\n\n\t',f'{bowler} is ready to bowl')
			bowl=random.choice(balls_option)
			print('\n\n\t',f'{bowler} bowled {bowl}') 
			print('\n\n\t','select your shot     !!!!!!!!!!!!','\n\n',shots_option)
			shot=input().lower()
			if ((bowl=='bouncer' or bowl=='slower ball') and shot=='pull') \
				or ((bowl=='leg spin' or 'googly') and shot == 'flick') \
				or ((bowl=='arm ball' or bowl=='off spin') and (shot=='cover drive' or shot =='drive')) \
				or ((bowl=='leg cutter' or bowl=='out swinger') and shot=='stright drive') or (bowl=='yorker' and shot=='helicopter'): # \ is used for multi-line if statements
				run=random.choice(runs)
				print('\t','yeaahhhhooo !!!!!!!!!!!!!''\n','perfect shot','\n\t',f'you hit {run}')
				score_of_striker+=run
				p1_total+=run
				players_data[striker] = score_of_striker

			else:
				print('\n\n','Opps you played a wrong shot   ')
				w_o=random.choice(out)
				print(w_o)
				print(f'{striker} is {w_o} at {score_of_striker} by {bowler}')
				players_data[str(striker)]=score_of_striker
				wickets+=1
				striker=batting_team[wickets]
				score_of_striker=0

			if run%2==0:
				pass
			if run%2!=0:
				score_of_striker,score_of_NONstriker = score_of_NONstriker , score_of_striker
				non_striker,striker=striker,non_striker

		print(f'{striker} at {score_of_striker} ',f'\n{bowler} has completed his over')
		print('\n','\n','\n','\n')
	return p1_total



# if p1 bowls then exceuts this function
def p1Bowling(p1,p2):
	# p1 is batting team and p2 is balling team
	p2_total=0
	players_data={}
	# wickets are 11 and wicktes are started from 1 because we have list of batsmen and we have to select striker and non-striker by index [0] and [1] then we have to increment wicket+=1
	wickets=1
	batting_team=teams[p2]
	bowling_team=teams[p1]
	striker=batting_team[wickets-1]
	non_striker=batting_team[wickets]
	score_of_striker=0
	score_of_NONstriker = 0
	# adding striker and non-striker data to players data dict
	players_data[striker] = score_of_striker
	players_data[non_striker] = score_of_NONstriker
	overs=0
	print('\n\n\n')
	print(colors['white'],'\n\t',f'{striker} and {non_striker} has came on felid')
	# total overs in a match
	for over in range(1):
		# choosing a bowler
		bowler=random.choice(bowling_team)
		if wickets==11:
			break
		for Balls in range(1,7):
			print( '\n',colors['cyan'],'_'*200,colors['white'],'\n')
			print('\t'f'{bowler} is on bolwing',f'{striker} is on strike')
			run = 0

			# batting scoreboard
			batting_scoreboard = PrettyTable(['batsman','score_of_striker'])
			batting_scoreboard.add_row([f'* {striker}', score_of_striker ])
			batting_scoreboard.add_row([non_striker, score_of_NONstriker ])
			print(batting_scoreboard)
			print()

			# p2 total score
			total_batting_score = PrettyTable(['Batting Team','Total Score','Wickets'])
			total_batting_score.add_row([p2,p2_total,wickets-1])
			print(total_batting_score)
			print()

			# bowling scoreBoard
			bowling_scoreboard = PrettyTable(['bowler','balls','over'])
			bowling_scoreboard.add_row([bowler,Balls-1,over])
			print(bowling_scoreboard)
			print()

			print('\n\n\t',f'{bowler} is ready to bowl')
			shot=random.choice(shots_option)
			print('\n\n\t','select your ball ->','\n\n',balls_option)
			bowl=input().lower()
			print('\n\n\t',f'{bowler} bowled {bowl}') 
			if ((bowl=='bouncer' or bowl=='slower ball') and shot=='pull') \
				or ((bowl=='leg spin' or 'googly') and shot == 'flick') \
				or ((bowl=='arm ball' or bowl=='off spin') and (shot=='cover drive' or shot =='drive')) \
				or ((bowl=='leg cutter' or bowl=='out swinger') and shot=='stright drive') or (bowl=='yorker' and shot=='helicopter'): # \ is used for multi-line if statements
				run=random.choice(runs)
				print('\t','yeaahhhhooo !!!!!!!!!!!!!''\n','perfect shot','\n\t',f'CPU hits {run}')
				score_of_striker+=run
				p2_total+=run
				players_data[striker] = score_of_striker

			else:
				print('\n\n','Opps CPU played a wrong shot   ')
				w_o=random.choice(out)
				print(w_o)
				print(f'{striker} is {w_o} at {score_of_striker} by {bowler}')
				players_data[str(striker)]=score_of_striker
				wickets+=1
				striker=batting_team[wickets]
				score_of_striker=0
			if run%2==0:
				pass
			if run%2!=0:
				score_of_striker,score_of_NONstriker = score_of_NONstriker , score_of_striker
				non_striker,striker=striker,non_striker

		print(f'{striker} at {score_of_striker} ',f'\n{bowler} has completed his over')
		print('\n','\n','\n','\n')
	return p2_total




# #   TOSS 
print(colors['white'],'\n\n\t\t','TOSS TIME ')
print('\n\n\t',"What's your call ?   ",'\n\t\nchosse head or tail  ')
coins=['HEAD','TAILS']
bat_or_ball = ['BAT','BOWL']
coin=random.choice(coins)
p1_call = input().upper()
if p1_call == coin:
	print(colors['green'],'\n\n\t\t','!!!!!!!!!!!!!','\n\n\t\t','YOU WON THE TOSS')
	print(colors['white'],'\n\n\t\t','WHAT YOU WANT TO CHOSSE BAT OR BOWL'    )
	bob=input().upper()
	if bob==bat_or_ball[0]:
		print("you chose to ------",bat_or_ball[0],'\n')
		score_p1 = p1_ing_score = p1Batting(player_1,player_2)
		print('\n\n\t',"p1 Batting HAS BEEN OVER they scored -> -------",score_p1)
		print('\n\n\t',"CPU Batting NOW THEY HAVE TO SCORE  -> -------",score_p1+1)
		print('\<<<<<<<<< PRESS ENTER TO CONTINUE >>>>>>>>>','\n')
		# pressing enter as input 
		enter=input()
		score_p2 = p1Bowling(player_1,player_2)
		print('\n\n\t',"p2 Batting HAS BEEN OVER they scored -> -------",score_p2)
		
	elif bob==bat_or_ball[1]:
		print("you chose to ------",bat_or_ball[1],'\n')
		score_p2 = p1Bowling(player_1,player_2)
		print('\n\n\t',"CPU Batting HAS BEEN OVER they scored -> -------",score_p2)
		print('\n\n\t',"CPU BATTING HAS OVER! NOW YOU HAVE TO SCORE  -> -------",score_p2+1)
		print('\<<<<<<<<< PRESS ENTER TO CONTINUE >>>>>>>>>','\n')
		# pressing enter as input 
		enter=input()
		score_p1 = p1_ing_score = p1Batting(player_1,player_2)
		print('\n\n\t',"p1 Batting HAS BEEN OVER they scored -> -------",score_p1)

else:
	print(colors['red'],'\n\n\t\t','!!!!!!!!!!!!!','\n\n\t\t','YOU LOSS THE TOSS')
	score_p2 = p1Bowling(player_1,player_2)
	print('\n\n\t',"cpu Batting HAS BEEN OVER they scored -> -------",score_p2)
	print('\n\n\t',"CPU BATTING HAS OVER! NOW YOU HAVE TO SCORE  -> -------",score_p2+1)
	print('\<<<<<<<<< PRESS ENTER TO CONTINUE >>>>>>>>>','\n')
	# pressing enter as input 
	enter=input()
	score_p1 = p1_ing_score = p1Batting(player_1,player_2)
	print('\n\n\t',"p1 Batting HAS BEEN OVER they scored -> -------",score_p1)


# ### winner ######
if score_p1 > score_p2: print("p1 wins")
elif score_p1 < score_p2: print("CPU wins")
else: print("match tied")



