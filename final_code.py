from tkinter import * 
from tkinter.ttk import *
import pandas as pd
from test import mvp_calculation
from test import predict_score
from test import covariance_calculation
from tkinter import messagebox 
from functools import partial

global players,Matches,BattingAvg,BattingSR,NumHundreds,NumFifties,BowlingAvg,BowlingSR,Economy,Balls,Fourwicketshaul,Fivewicketshaul
global MVP_RCB
global PBT
global PBW
global PEX
global main
global tc
#defining Requirement points
BARP=400
BORP=330
ERP=310
#reading the dataset
df=pd.read_csv('data.csv')
players=df.Name.tolist()
Matches=df.Mat.tolist()
BattingAvg=df.AvgBat.tolist()
BattingSR=df.SRBat.tolist()
NumHundreds=df.Hundreds.tolist()
NumFifties=df.Fifties.tolist()
BowlingAvg=df.AvgBowl.tolist()
BowlingSR=df.SRBowl.tolist()
Economy=df.Eco.tolist()
Balls=df.Balls.tolist()
Fourwicketshaul=df.Fourw.tolist()
Fivewicketshaul=df.Fivew.tolist()

#pre calculated values of MVP,PBT,PBW,PEX
MVP_RCB=[2.079, 1.188, 2.001, 2.051, 1.962, 1.852, 1.924, 0.629, 1.618, 0.14, 2.135, 1.746, 1.892, 0.648, 1.605, 1.203, 1.528, 1.766, 2.157]
PBT=[6.671, 3.628, 6.708, 6.008, 6.383, 6.759, 6.033, 2.078, 5.724, 0.43, 6.889, 5.398, 5.857, 1.553, 5.528, 3.601, 4.869, 5.097, 6.35]
PBW=[5.71, 7.567, 5.525, 0, 6.604, 4.328, 0, 6.488, 5.915, 5.549, 0, 0, 0, 6.197, 6.279, 0, 5.784, 0, 0]
PEX=[9.41, 6.974, 6.469, 6.805, 8.066, 1.008, 2.268, 2.268, 2.521, 0.756, 0.504, 2.857, 3.025, 7.646, 3.865, 3.193, 7.226, 6.637, 6.805]
tt=[('All-Rounder', 'A+'), ('Bowler', 'A+'), ('All-Rounder', 'A'), ('Batsman', 'C'), ('All-Rounder', 'A+'), ('All-Rounder', 'C'), ('Batsman', 'C'), ('Bowler', 'C'), ('All-Rounder', 'C'), ('Bowler', 'E'), ('Batsman', 'B'), ('Batsman', 'D'), ('Batsman', 'D'), ('Bowler', 'C'), ('All-Rounder', 'B'), ('Batsman', 'F'), ('All-Rounder', 'B'), ('Batsman', 'D'), ('Batsman', 'B')]

global bought_players
bought_players=[]
main = Tk() 
main.geometry("970x280") 
main.title("Auction for IPL Players")

global SR,Runs,Total_score
SR=[['RohitSharma',122.71,135,40,121.95,80,20,114.7,168.57,100,233.33,113.33],['LasithMalinga',34.89,0,35,100,50,0,0,21,42.9,0,100],['KieronPolard',136.06,200,130,121,111,131.7,110,250,111.9,75,120],['AmbatiRaydu',88.61,110,102,100,130,90.7,111,123.4,119,0,0],['HarbhajanSingh',68.67,100,170,100,69,72,75.7,0,0,0,100],['CoreyAnderson',103.67,113,131,90.7,112,160,200,130,100,0,0],['AdityaTare',117.57,100,101,0,100,200,140,120,90.7,124,200],['JoshHazlewood',17.66,0,100,21,31,24.6,0,0,0,0,0],['MercgantDeLange',55.4,67,56,100,100,131,0,0,50,50,0],['PawanSuyal',29.3,50,36,58,0,0,0,0,49,100,0],['ShreyasGopal',50,100,46,49,43,50,100,100,0,0,12],['LendlSimmons',111.66,111,120,131,50,100,50,110,113.6,200,131],['AaronFinch',105.1,100,120,0,90,87,131,150,111,112,150],['PragyanOjha',28.3,0,40,12,40,31,69,41,50,0,0],['McClenaghan',52.1,50,50,0,0,110,100,80,31,0,100],['UnmuktChand',121.8,100,200,90,121,131,50,90,105,131,200],['VinayKumar',1030.3,150.7,130,200,87.6,90,131,0,0,141,100],['ParthivPatel',90.7,100,131,111,113,121,100,131,0,100,0],['AidenBizzard',115.36,200,0,0,121,105.6,100,200,131,116,180]]
Runs=[['RohitSharma',26,27,2,50,4,1,39,59,19,14,51],['LasithMalinga',4.5,0,1,3,7,0,0,13,20,0,1],['KieronPolard',37.3,30,45,56,8,9,65,31,29,49,51],['AmbatiRaydu',33.6,21,35,40,75,29,31,45,60,0,0],['HarbhajanSingh',9,3,5,9,15,16,21,0,0,0,21],['CoreyAnderson',31.4,51,49,34,12,34,71,42,21,0,0],['AdityaTare',22.4,21,30,0,5,16,36,42,33,27,14],['JoshHazlewood',1.3,0,1,5,4,3,0,0,0,0,0],['MercgantDeLange',5.6,12,14,10,9,8,0,0,2,1,0],['PawanSuyal',6,2,8,7,0,0,0,0,12,31,0],['ShreyasGopal',5.2,13,12,1,4,5,7,9,0,0,1],['LendlSimmons',34.1,53,43,31,16,23,5,51,20,29,70],['AaronFinch',46.8,72,43,0,23,26,45,53,69,67,70],['PragyanOjha',3.5,0,8,1,2,4,6,7,7,0,0],['McClenaghan',6.9,2,1,0,0,13,20,12,9,0,12],['UnmuktChand',32.7,68,27,12,40,48,7,8,38,29,50],['VinayKumar',13.7,21,15,16,18,19,21,0,0,12,15],['ParthivPatel',32.6,23,45,69,31,72,43,33,0,10,0],['AidenBizzard',24.5,15,0,0,41,23,13,10,33,21,89]]
Total_score=[['RohitSharma',156.86,122,115,141,125,157,170,187,157,160,141],['LasithMalinga',153.2,167,142,210,31,154,147,169,131,201,180],['KieronPolard',158.2,168,171,131,127,145,178,156,134,182,190],['AmbatiRaydu',153.5,160,153,142,131,156,176,180,200,121,116],['HarbhajanSingh',153.5,160,153,142,131,156,176,180,200,121,116],['CoreyAnderson',153.5,160,153,142,131,156,176,180,200,121,116],['AdityaTare',153.5,160,153,142,131,156,176,180,200,121,116],['JoshHazlewood',164.1,116,157,180,131,178,165,190,200,201,123],['MercgantDeLange',164.1,116,157,180,131,178,165,190,200,201,123],['PawanSuyal',157.7,123,201,200,190,165,171,131,141,133,122],['ShreyasGopal',162.8,210,123,145,165,176,139,158,190,123,199],['LendlSimmons',168.4,159,160,200,148,167,120,220,159,171,180],['AaronFinch',164.1,116,157,180,131,178,165,190,200,201,123],['PragyanOjha',168.4,159,160,200,148,167,120,220,159,171,180],['McClenaghan',164.1,116,157,180,131,178,165,190,200,201,123],['UnmuktChand',161,168,165,171,185,135,189,142,168,154,133],['VinayKumar',150.1,131,126,189,121,151,146,180,191,131,135],['ParthivPatel',164.8,200,138,190,154,168,171,170,162,145,150],['AidenBizzard',161,168,165,171,185,135,189,142,168,154,133]]


def gui(nav):
	
	t=len(players)
	#defining the headings
	h1 = Label(main, text = "Player Name", font = 'mincho 28 bold')
	h2 = Label(main, text = "MVP Scores", font = 'mincho 28 bold')
	barp="Batting Requirement = " + str(BARP)
	borp="Bowling Requirement = " + str(BORP)
	erp="Experience Requirement = " + str(ERP)
	h3 = Label(main, text = barp,font = 'mincho 20 ',foreground='blue')
	h4 = Label(main, text = borp,font = 'mincho 20 ',foreground='blue')
	h5 = Label(main, text = erp,font = 'mincho 20 ',foreground='blue')
	#placing the headings
	h1.grid(row = 0, column = 0, padx = 5) 
	h2.place(x=250,y=0) 
	h3.place(x=500,y=100) 
	h4.place(x=500,y=150) 
	h5.place(x=500,y=200) 
	#first iteration
	if nav==0:
		#defining the player names
		for i in range(t):
			if i ==0:
				globals()['p'+str(i)]=Label(main, text = players[i], foreground = 'Red', font='mincho 18 ')
			else:
				globals()['p'+str(i)]=Label(main, text = players[i],font='mincho 18 ')
		#defining the MVP scores
		for i in range(t):
			if i ==0:
				globals()['mvp_'+str(i)]=Label(main, text = MVP_RCB[i], foreground = 'Red',font='mincho 18')
			else:
				globals()['mvp_'+str(i)]=Label(main, text = MVP_RCB[i],font='mincho 18 ')
		
		x1=30
		y1=50
		#placing the above defined labels
		for i in range(t):

			globals()['p'+str(i)].place(x=x1,y=y1)
			y1=y1+40
		x2=300
		y2=50
		for i in range(t):
			globals()['mvp_'+str(i)].place(x=x2,y=y2)
			y2=y2+40
	#any iteration apart from 1st
	if nav==1:
		for i in range(20):
			if i<t:
				globals()['p'+str(i)].config(text = players[i])
			if i==t:
				globals()['p'+str(i)].destroy()

		for i in range(20):
			if i <t:
				globals()['mvp_'+str(i)].config( text = MVP_RCB[i])
			if i==t:
				globals()['mvp_'+str(i)].destroy()
		
		x1=30
		y1=50
		for i in range(20):

			globals()['p'+str(i)].place(x=x1,y=y1)
			y1=y1+40
		x2=300
		y2=50
		for i in range(20):
			globals()['mvp_'+str(i)].place(x=x2,y=y2)
			y2=y2+40
	
	#defining and placing images
	img = PhotoImage(file = "rcb_gui.png") 
	img1 = img.subsample(2, 2) 
	Label(main, image = img1).place(x=1000,y=100)
	#button styles and placement
	sto1 = Style()
	sto2 = Style()
	sto3=Style()
	sto4=Style()
	sto1.configure('W.TButton', font= ('Arial', 20), foreground='Black') 
	sto2.configure('X.TButton', font= ('Arial', 20), foreground='Red') 
	sto3.configure('M.TButton', font= ('Arial', 20), foreground='Green')
	sto4.configure('N.TButton', font= ('Arial', 20), foreground='Blue')
	b1 = Button(main, text = "View Stats", style = 'W.TButton', command = partial(openstats,main))
	b2 = Button(main, text = "Ignore Player", style = 'X.TButton',command= partial(ignore,main))
	b3= Button(main, text = "Buy Player", style = 'M.TButton',command= partial(buy,main))
	b4= Button(main, text = "View Bought Players", style = 'N.TButton',command= partial(bought,main))
	b1.place(x=600,y=600)
	b2.place(x=1100,y=600)
	b3.place(x=850,y=600)
	b4.place(x=850,y=800)
	mainloop()  
	
#function to predict average score of team
def predictscore(bt):
	name=[]
	for i in bought_players:
		name.append(i[0])

	sr_pred=[]
	sr_avg=[]
	runs_pred=[]
	runs_avg=[]
	total_pred=[]
	total_avg=[]
	for i in name:
		for j in SR:
			if i==j[0]:
				sr_pred.append(j[1:11])
				sr_avg.append(j[11])
		for j in Runs:
			if i==j[0]:
				runs_pred.append(j[1:11])
				runs_avg.append(j[11])
		for j in Total_score:
			if i==j[0]:
				total_pred.append(j[1:11])
				total_avg.append(j[11])
	predicted=[]
	for i in range(len(name)):
		predss= predict_score(sr_pred[i],runs_pred[i],total_pred[i],sr_avg[i],runs_avg[i])
		predicted.append(predss)
	
	fine_predict=round(sum(predicted)/len(predicted),3)
	mng1=Label(bt, text = 'Predicted score = '+ str(fine_predict),font='mincho 18 ', foreground='red')
	mng1.place(x=10,y=500)

#function to view all bought players
def bought(main):
	bt = Toplevel(main) 
	bt.title("Bought Players") 
	bt.geometry("1000x600")
	llt1=Label(bt, text = 'Player Name',font='mincho 18 ', foreground='red')
	llt2=Label(bt, text = 'Player type',font='mincho 18 ', foreground='red')
	llt3=Label(bt, text = 'Player Class',font='mincho 18 ', foreground='red')
	llt1.place(x=10,y=30)
	llt2.place(x=350,y=30)
	llt3.place(x=660,y=30)
	for i in range(len(bought_players)):
		globals()['bplayer'+str(i)]=Label(bt, text = bought_players[i][0],font='mincho 18 ')

	for i in range(len(bought_players)):
		globals()['btype'+str(i)]=Label(bt, text = bought_players[i][1][0],font='mincho 18 ')

	for i in range(len(bought_players)):
		globals()['bclass'+str(i)]=Label(bt, text = bought_players[i][1][1],font='mincho 18 ')

	x1=10
	y1=70
	for i in range(len(bought_players)):
		globals()['bplayer'+str(i)].place(x=x1,y=y1)
		y1=y1+30

	x2=350
	y2=70
	for i in range(len(bought_players)):
		globals()['btype'+str(i)].place(x=x2,y=y2)
		y2=y2+30

	x3=700
	y3=70
	for i in range(len(bought_players)):
		globals()['bclass'+str(i)].place(x=x3,y=y3)
		y3=y3+30

	sto2 = Style()
	sto2.configure('X.TButton', font= ('Arial', 20), foreground='Green') 
	b2 = Button(bt, text = "Predict Average score", style = 'X.TButton',command= partial(predictscore,bt))
	b2.place(x=350,y=400)

#function to buy a players
def buy(main):
	
	global BARP
	global BORP
	global ERP
	#changing the requirement points after buying
	BARP = round(BARP-PBT[0],3)
	BORP = round(BORP-PBW[0],3)
	ERP = round(ERP-PEX[0],3)
	bought_players.append([players[0],tt[0]])
	#altering the dataset
	del players[0]
	del MVP_RCB[0]
	del tt[0]
	del PBT[0]
	del PBW[0]
	del PEX[0]
	del Matches[0]
	del BattingAvg[0]
	del BattingSR[0]
	del NumHundreds[0]
	del NumFifties[0]
	del BowlingAvg[0]
	del BowlingSR[0]
	del Economy[0]
	del Balls[0]
	del Fourwicketshaul[0]
	del Fivewicketshaul[0]
	#mvp calculation after buying
	for i in range(len(players)):
		MVP_RCB[i]=mvp_calculation(BARP,BORP,ERP,PBT[i],PBW[i],PEX[i])
	gui(1)

#function to calculate covariance of players	
def cov(stats):
	name=[]
	for i in bought_players:
		name.append(i[0])
	for i in Runs:
		if players[0]==i[0]:
			A=i[2:]
	
	B_all=[]
	for i in name:
		for j in Runs:
			if i==j[0]:
				B_all.append(j[2:])
	
	cov_scores=[]
	
	for i in range(len(name)):
		corr=round(covariance_calculation(A,B_all[i]),3)
		cov_scores.append(corr)
	
	for i in range(len(cov_scores)):
		string=players[0]+' - '+name[i]+' : '+str(cov_scores[i])
		globals()['vvr'+str(i)]=Label(stats,text=string,font='mincho 18 ',foreground='Red')

	yi=100
	xi=500
	for i in range(len(cov_scores)):
		globals()['vvr'+str(i)].place(x=xi,y=yi)
		yi=yi+30
	
#function to open stats of player
def openstats(main):  
	global stats
	stats = Toplevel(main) 
	stats.title("Player Stats") 
	stats.geometry("1000x600") 
	lbl1=Label(stats, text ='Name : '+str(players[0]),font='mincho 18 ', foreground = 'Red')
	lbl2=Label(stats, text ='PBT = '+ str(PBT[0]),font='mincho 18 ')
	lbl3=Label(stats, text ='PBW = '+str(PBW[0]),font='mincho 18 ')
	lbl4=Label(stats, text ='PEX = '+str(PEX[0]),font='mincho 18 ')
	lbl5=Label(stats, text ='Matches Played'+str(Matches[0]),font='mincho 18 ')
	lbl6=Label(stats, text ='Batting Average '+str(BattingAvg[0]),font='mincho 18 ')
	lbl7=Label(stats, text ='Batting Strike rate = '+ str(BattingSR[0]),font='mincho 18 ')
	lbl8=Label(stats, text ='Number of Hundreds = '+str(NumHundreds[0]),font='mincho 18 ')
	lbl9=Label(stats, text ='Number of Fifties = '+str(NumFifties[0]),font='mincho 18 ')
	lbl10=Label(stats, text ='Bowling Average = '+ str(BowlingAvg[0]),font='mincho 18 ')
	lbl11=Label(stats, text ='Bowling Strike Rate = '+ str(BowlingSR[0]),font='mincho 18 ')
	lbl12=Label(stats, text ='Economy = '+ str(Economy[0]),font='mincho 18 ')
	lbl13=Label(stats, text ='Number of Balls Bowled = '+ str(Balls[0]),font='mincho 18 ')
	lbl14=Label(stats, text ='Four Wikets haul = '+ str(Fourwicketshaul[0]),font='mincho 18 ')
	lbl15=Label(stats, text ='Five Wickets haul = '+ str(Fivewicketshaul[0]),font='mincho 18 ')
	lbl16=Label(stats, text= 'PLayer Type =  '+ str(tt[0][0]),font='mincho 18')
	lbl17=Label(stats, text= 'PLayer class =  '+ str(tt[0][1]),font='mincho 18')

	x1=20
	y1=20
	lbl1.place(x=x1,y=y1)
	lbl2.place(x=x1,y=50)
	lbl3.place(x=x1,y=80)
	lbl4.place(x=x1,y=110)
	lbl5.place(x=x1,y=140)
	lbl6.place(x=x1,y=170)
	lbl7.place(x=x1,y=200)
	lbl8.place(x=x1,y=230)
	lbl9.place(x=x1,y=260)
	lbl10.place(x=x1,y=290)
	lbl11.place(x=x1,y=320)
	lbl12.place(x=x1,y=350)
	lbl13.place(x=x1,y=380)
	lbl14.place(x=x1,y=410)
	lbl15.place(x=x1,y=440)
	lbl16.place(x=500,y=y1)
	lbl17.place(x=500,y=50)
	
	sto2 = Style()
	sto2.configure('X.TButton', font= ('Arial', 20), foreground='Green') 
	b2 = Button(stats, text = "See Covariance", style = 'X.TButton',command= partial(cov,stats))
	b2.place(x=550,y=550)


#function to ignore player
def ignore(main):
	#alter dataset
	del players[0]
	del MVP_RCB[0]
	del tt[0]
	del PBT[0]
	del PBW[0]
	del PEX[0]
	del Matches[0]
	del BattingAvg[0]
	del BattingSR[0]
	del NumHundreds[0]
	del NumFifties[0]
	del BowlingAvg[0]
	del BowlingSR[0]
	del Economy[0]
	del Balls[0]
	del Fourwicketshaul[0]
	del Fivewicketshaul[0]
	
	gui(1)
			

gui(0)
