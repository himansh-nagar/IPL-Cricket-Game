import random 
# from batbowl import innings,innings_2
# from batbowl import innings_2
# variabless



print('\u001b[34m-----------------------INDIAN PREMIUM LEAUGE--------------------------------------------------------','\n')
print("\u001b[31m___________________________BY 'HIMANSHU NAGAR_______________________________________________________",'\n')
print('\u001b[34m<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< PRESS ENTER TO CONTINUE>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>','\n')
enter=input()



runs=[1,2,3,4,6]

balls_option=['leg spin','googly','off spin','arm ball','bouncer','leg cutter','out swinger','reverse swing','yorker','slower ball']
out=['run out','caught and bold','stumped','caught','bowled']

shots_option=['cut','flick','step out and hit','cover drive','drive','stright drive','helicopter','pull']

print('\u001b[32;1mchosse your team ','\n')

# teams

opponent_team=['CSK','MI','RCB','KKR','DC','RR','SRH','KXIP']
teams={'CSK':['MS Dhoni', 'Josh Hazlewood' ,'Kedar Jadhav', 'Harbhajan Singh', 'Piyush Chawla', 'Ambati Rayudu', 'Suresh Raina', 'Imran Tahir','Deepak Chahar', 'Faf du Plessis', 'Shardul Thakur'],
	   'MI':['Rohit Sharma','surya kumar yadav','chris lynn','Quinton de kock','kieron pollard','krunal pandya','ishan kishan','hardik pandya','trent boult','jasprit bumrah','rahul Chahar'],
	   'RCB':['Virat Kohli','AB de Villiers','aron finch','moeen ali','parthiv patel','shivam dube','washinton sunder','chris morris','umesh yadav','mohammed siraj','dale steyn'],
	   'KKR':['andre russell','dinesh kartik','kuldeep yadav','nitesh rana','rinku singh','shivam mavi','shubman gill','sunil narine','pat cummins','Eoin morgan','prasidh krishna'],
	   'DC':['Shreyas Iyer','Prithvi Shaw', 'Ajinkya Rahane', 'Shikhar Dhawan', 'Jason Roy','Ishant Sharma', 'Amit Mishra','R Ashwin', 'Marcus Stoinis', 'Chris Woakes', 'Rishabh Pant'],
	   'RR':['Steve Smith', 'Robin Uthappa', 'David Miller', 'Ankit Rajpoot', 'Mayank Markande', 'Jofra Archer', 'Shreyas Gopal', 'Varun Aaron', 'Jaydev Unadkat', 'Ben Stokes','Jos Buttler'],
	   'SRH':['kane williamson','david warner','manish pandey','Virat Singh', 'Priyam Garg', 'Abdul Samad', 'Bhuvneshwar Kumar', 'Khaleel Ahmed', 'Sandeep Sharma', 'Siddharth Kaul', 'Billy Stanlake'],
	   'KXIP':['Chris Gayle', 'Mayank Agarwal', 'Karun Nair', 'Sarfaraz Khan', 'Mandeep Singh', 'Sheldon Cottrell', 'Ishan Porel', 'Ravi Bishnoi', 'Mohammed Shami','KL Rahul','Glenn Maxwell'],
	   }
keys=teams.keys()
for keys in teams:
	print(keys)


player_1=input('chosse your team    ').upper()
opponent_team.remove(player_1)
player_2=random.choice(opponent_team)
print('\n','\n','\t','\t','\u001b[31;1m',player_1,'\n','\t','\t','VS','\n','\t','\t',player_2)
print('\n','\n')
print('\t','\t','\u001b[34;1mYOUR TEAM')
for player in teams[player_1]:
	print('\t',player)
print()
print()
print('\t','\t','\u001b[31;1mOPPONENT TEAM')
for player2 in teams[player_2]:
	print('\t',player2)


def innings():
	list_of_balls=[]
	p1_total=0
	# batting_team,bowling_team=player_1,player_2
	player_run={}
	wickets=1
	all_batsmen=teams[player_1]
	bowling_team=teams[player_2]
	# all_batsmen=iter([batting_team])
	striker=all_batsmen[wickets-1]
	non_striker=all_batsmen[wickets]
	score_of_player=0
	overs=0
	print('\n','\n','\n')
	print('\n','\t',f'\u001b[47m{striker} and {non_striker} has came on felid')
	for over in range(5):
		bowler=random.choice(bowling_team)
		if over==5 or wickets==10:
			break
		print('\t'f'\u001b[47m{bowler} is on bolwing',f'{striker} is on strike')
		for Balls in range(1,7):
			print('\n','\n','\t',f'\u001b[47m{bowler} has came to bowl')
			run=random.choice(runs)
			bowl=random.choice(balls_option)
			print('\n','\n','\t',f'\u001b[41;1m{bowler} bowled {bowl}')
			print('\n','\n','\t','select your shot     !!!!!!!!!!!!','\n','\n',shots_option)
			shot=input().lower()
			if (bowl=='bouncer' or bowl=='slower ball') and shot=='pull':
				print('\t','\u001b[44;1myeaahhhhooo !!!!!!!!!!!!!''\n','perfect shot','\n','\t',f'you hit {run}')
				score_of_player+=run
			elif (bowl=='leg spin' or 'googly') and shot == 'flick':
				print('\t','\u001b[44;1myeaahhhhooo !!!!!!!!!!!!!''\n','perfect shot','\n','\t',f'you hit {run}')
				score_of_player+=run

			elif (bowl=='arm ball' or bowl=='off spin') and (shot=='cover drive' or shot =='drive'):
				print('\t','\u001b[44;1myeaahhhhooo !!!!!!!!!!!!!''\n','perfect shot','\n','\t',f'you hit {run}')
				score_of_player+=run

			elif (bowl=='leg cutter' or bowl=='out swinger') and shot=='stright drive':
				print('\t','\u001b[44;1myeaahhhhooo !!!!!!!!!!!!!''\n','perfect shot','\n','\t',f'you hit {run}')
				score_of_player+=run
			elif bowl=='yorker' and shot=='helicopter':
				print('\t','\u001b[47;1myeaahhhhooo !!!!!!!!!!!!!''\n','perfect shot','\n','\t',f'{player_2} has hit {run}')
				score_of_player+=run
			else:
				print('\n','\n','\u001b[41;1mopps you played a wrong shot   ')
				wickets+=1
				
				w_o=random.choice(out)
				print(w_o)
				print(f'\u001b[41;1m{striker} is out at {score_of_player} by {bowler}')
				striker=all_batsmen[wickets-1]
				player_run[str(striker)]=score_of_player
				score_of_player=0
				p1_total+=score_of_player
			if run%2==0:
				pass
			if run%2!=0:
				non_striker,striker=striker,non_striker
			list_of_balls.append(run)
		print(f'{striker} and {non_striker} are playing')
		print(f'\u001b[32;1m{striker} at {score_of_player} ',f'{bowler} has completed his over')
		print('\n','\n','\n','\n')
	over+=1
	print(player_run)

def innings_2():
	list_of_balls=[]
	p2_total=0
	# batting_team,bowling_team=player_1,player_2
	player_run={}
	wickets=1
	all_batsmen=teams[player_2]
	bowling_team=teams[player_1]
	# all_batsmen=iter([batting_team])
	striker=all_batsmen[wickets-1]
	non_striker=all_batsmen[wickets]
	list_of_played_batsmen=[]

	score_of_player=0
	overs=0
	
	print('\n','\n','\n')
	print('\n','\t',f'\u001b[34;1m{striker} and {non_striker} has came on felid')
	for over in range(5):
		bowler=random.choice(bowling_team)
		batmens=random.choice(all_batsmen)
		batmen=batmens
		if over==5 or wickets==10:
			break
		if batmens in list_of_played_batsmen:
			continue
		print('\t'f'\u001b[34;1m{bowler} is on bolwing',f'{striker} is on strike')
		for Balls in range(1,7):
			print('\n','\n','\t',f'\u001b[33;1m{bowler}  are going to bowl')
			print('\n','\n','\t','\u001b[37mselect your ball     !!!!!!!!!!!!','\n','\n',balls_option)
			bowl=input().lower()
			# print('\n','\n','\t',f'{bowler} has came to bowl')
			run=random.choice(runs)
			shot=random.choice(shots_option)
			
			if (bowl=='bouncer' or bowl=='slower ball') and shot=='pull':
				print('\t','\u001b[47;1myeaahhhhooo !!!!!!!!!!!!!''\n','perfect shot','\n','\t',f'you hit {run}')
				score_of_player+=run
			elif (bowl=='leg spin' or 'googly') and shot == 'flick':
				print('\t','\u001b[47;1myeaahhhhooo !!!!!!!!!!!!!''\n','perfect shot','\n','\t',f'{batmen} has hit {run}')
				score_of_player+=run
			elif (bowl=='arm ball' or bowl=='off spin') and (shot=='cover drive' or shot =='drive'):
				print('\t','\u001b[47;1myeaahhhhooo !!!!!!!!!!!!!''\n','perfect shot','\n','\t',f'{batmen} has hit {run}')
				score_of_player+=run
			elif (bowl=='leg cutter' or bowl=='out swinger') and shot=='stright drive':
				print('\t','\u001b[47;1myeaahhhhooo !!!!!!!!!!!!!''\n','perfect shot','\n','\t',f'{batmen} has hit {run}')
				score_of_player+=run
			elif bowl=='yorker' and shot=='helicopter':
				print('\t','\u001b[47;1myeaahhhhooo !!!!!!!!!!!!!''\n','perfect shot','\n','\t',f'{batmen} has hit {run}')
				score_of_player+=run
			else:
				print('\n','\n',f'\u001b[41;1mopps opponent_player has played a wrong shot   ')
				wickets+=1
				w_o=random.choice(out)
				print(w_o)
				print(f'\u001b[41;1m{striker} is out at {score_of_player} by {bowler}')
				striker=all_batsmen[wickets-1]
				player_run[str(striker)]=score_of_player
				score_of_player=0
				batmens=random.choice(all_batsmen)
				list_of_played_batsmen.append(batmens)
				# p2_total+=score_of_player
			if run%2==0:
				pass
			if run%2!=0:
				non_striker,striker=striker,non_striker
			list_of_balls.append(run)

		print(f'\u001b[32;1m{striker} at {score_of_player} ',f'{bowler} has completed his over')
		print(f'{striker} and {non_striker} are playing')
		print('\n','\n','\n','\n')
	over+=1
	print(player_run)	



#   TOSS 


print('\n','\n','\t','\t','\u001b[42;1mTOSS TIME ')
print('\n','\n','\t','\t',"\u001b[42;1mWhat's your call ?   ",'\n','\t','\u001b[42;1mchosse head or tail  ')
coins=['HEAD','TAILS']
coin=random.choice(coins)
p1_call = input().upper()
if p1_call==coin:
	print('\n','\n','\t','\t','\u001b[34;1myooo!!!!!!!!!!!!!','\n','\n','\t','\t','u001b[34;1mYOU WON THE TOSS')
	print('\n','\n','\t','\t','\u001b[44mWHAT YOU WANT TO CHOSSE BAT OR BOWL'    )
	bob=input().upper()
	if bob=='BAT':
		innings()
		print('\n','\n','\n','\n','\n','\t'," \u001b[40;1mINNINGS HAS BEEN OVER   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!",'\n',p1_total)
		

	if bob=='BOWL':
		print('\n','\n','\t',f'\u001b[44;1m{player_1} has chosen to bowl')
		innings_2()
	print('\n','\n','\n','\n','\n','\t',f'\u001b[37;1m{player_1} has scored {p1_total}','\n','\n','\n','\n','\n','\t',f'\u001b[37;1m{player_2} needs {p1_total} to win')
	print('\n','\n','\n','\n','\n','\t'," INNINGS HAS BEEN OVER   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!",'\n',p1_total)

		
	# print('\n','\n','\n','\n','\n','\t'," INNINGS HAS BEEN OVER   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!",'\n',p2_total)

if p1_call!=coin:
	print(f'\n','\t','\t','ohhh !!!!!!!!!!','\n','\t','\t','YOU LOSS THE TOSS ','\n','\t','\t',f'{player_2} has decided to bat frist')
	innings_2()
	print('\n','\n','\n','\n','\n','\t'," \u001b[37;1mINNINGS HAS BEEN OVER   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!",'\n',p2_total)
	print('\n','\n','\n','\n','\n','\t',f'{player_2} has scored {p2_total}','\n','\n','\n','\n','\n','\t',f'{player_2} needs {p2_total} to win')
	print('\n','\n','\n','\n','\n','\t'," \u001b[41;1mINNINGS HAS BEEN OVER   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!",'\n',p2_total)
	innings()
	print('\n','\n','\n','\n','\n','\t'," \u001b[37;1mINNINGS HAS BEEN OVER   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!",'\n',p1_total)





### winner ######
if p1_total>p2_total:
	print( '\u001b[41;1mmatch has been ended','\n','\n', f'\u001b[41;1m{player_1} has woned the match  !!!!!!!!!!!!!!!')
else:
	print( '\u001b[44;1mmatch has been ended','\n','\n', f'\u001b[44;1m{player_2} has woned the match  !!!!!!!!!!!!!!!')


print()
print()
print()
print()
print()

