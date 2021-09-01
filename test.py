import pandas as pd 
df=pd.read_csv('data.csv')
#l=list(df[0])
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
'''
t=len(players)
PBT=[]
PBW=[]
PEX=[]
for i in range(t):
	pbt= ((BattingAvg[i]*0.3)+ (BattingSR[i]*0.4) + NumHundreds[i] +(NumFifties[i]*0.2))/10
	pbt=round(pbt,3)
	PBT.append(pbt)

	if Balls[i]>100:
		pbw=((300/BowlingAvg[i]) + (200/BowlingSR[i]) + (300/Economy[i]) + (Fourwicketshaul[i]*0.1)+ Fivewicketshaul[i]*0.1)/10
		pbw=round(pbw,3)
		PBW.append(pbw)
	else:
		pbw=0
		PBW.append(0)

	pex=Matches[i]/11.9022
	pex=round(pex,3)
	PEX.append(pex)

print(PBT)
print(PBW)
print(PEX)
'''

PBT=[6.671, 3.628, 6.708, 6.008, 6.383, 6.759, 6.033, 1.363, 2.078, 5.724, 0.43, 6.889, 5.398, 5.857, 1.553, 5.528, 3.601, 4.869, 5.097, 6.35]
PBW=[5.71, 7.567, 5.525, 0, 6.604, 4.328, 0, 4.992, 6.488, 5.915, 5.549, 0, 0, 0, 6.197, 6.279, 0, 5.784, 0, 0]

PEX=[9.41, 6.974, 6.469, 6.805, 8.066, 1.008, 2.268, 1.092, 2.268, 2.521, 0.756, 0.504, 2.857, 3.025, 7.646, 3.865, 3.193, 7.226, 6.637, 6.805]

def mvp_calculation(barp,borp,erp,pbt,pbw,pex):
	trp=barp+borp+erp
	if pbw==0:
		mvp = (8*pbt*(barp/trp)+(erp/trp)*pex)/10
	else:
		if pbt/pbw>=2:
			mvp = (((7*pbt*(barp/trp))+(2*pbw*(borp/trp))+(pex*(erp/trp)))/10)
		else:
			if pbw/pbt>=2:
				mvp = (((7*pbw*(borp/trp))+(2*pbt*(barp/trp))+(pex*(erp/trp)))/10)
			else:
				mvp = (((9*pbw*(borp/trp))+(9*pbt*(barp/trp))+(2*pex*(erp/trp)))/20)
				
	return round(mvp,3)


def tcp_calculation(pbt,pbw,pex):
	if pbw==0:
		TCP = (8*pbt + 1*pbw + pex)/10
	elif pbt/pbw>=2:
		TCP = (7*pbt + 2*pbw + pex)/10
	elif pbw/pbt>=2:
		TCP = (2*pbt + 7*pbw + pex)/10
	else:
		TCP = (9*pbt + 9*pbw + 2*pex)/20

	return TCP
	

def determine_class(TCP):
	if TCP>=6.5:
		return 'A+'
	elif TCP>=6:
		return 'A'
	elif TCP>=5.5:
		return 'B'
	elif TCP>=5:
		return 'C'
	elif TCP>=4.5:
		return 'D'
	elif TCP>=4:
		return 'E'
	else:
		return 'F'

def classification(pbt,pbw,TCP):
	if pbw==0 or (pbt/pbw)>=4:
		
		player_type='Batsman'
		player_class=determine_class(TCP)
	elif (pbw/pbt)>=1.25:
		player_type='Bowler'
		player_class=determine_class(TCP)
		
	else:
			
		player_type='All-Rounder'
		player_class=determine_class(TCP)

	return player_type,player_class

def covariance_calculation(A,B):
	avg_A=sum(A)/len(A)
	avg_B=sum(B)/len(B)
	AB=[]
	for i in range(len(A)):
		ab=A[i]*B[i]
		AB.append(ab)
	avg_AB=sum(AB)/len(AB)
	return avg_AB-(avg_A*avg_B)

def predict_score(SR,Runs,Total_score,currentSR,currentRuns):
	X=sum(SR)/len(SR)
	Y=sum(Runs)/len(Runs)
	Z=sum(Total_score)/len(Total_score)
	R=[]
	S=[]
	T=[]
	den1=[]
	den2=[]
	for i in range(len(SR)):
		R.append(SR[i]-X)
		S.append(Runs[i]-Y)
		T.append(Total_score[i]-Z)
		den1.append((SR[i]-X)**2)
		den2.append((Runs[i]-Y)**2)

	RT=[]
	ST=[]
	for i in range(len(SR)):
		RT.append(R[i]*T[i])
		ST.append(S[i]*T[i])
	w1=round((sum(RT)/sum(den1)),5)
	w2=round((sum(ST)/sum(den2)),5)
	w0=round((Z-(w1*X)-(w2*Y)),5)
	predicted_score= w0+(w1*currentSR)+(w2*currentRuns)
	return predicted_score

#SR=[['RohitSharma',122.71,135,40,121.95,80,20,114.7,168.57,100,233.33,113.33],['LasithMalinga',34.89,0,35,100,50,0,0,21,42.9,0,100],['KieronPolard',136.06,200,130,121,111,131.7,110,250,111.9,75,120].['AmbatiRaydu',88.61,110,102,100,130,90.7,111,123.4,119,0,0],['HarbhajanSingh',68.67,100,170,100,69,72,75.7,0,0,0,100],['CoreyAnderson',103.67,113,131,90.7,112,160,200,130,100,0,0],['AdityaTare',117.57,100,101,0,100,200,140,120,90.7,124,200],['JoshHazlewood',17.66,0,100,21,31,24.6,0,0,0,0,0],['MercgantDeLange',55.4,67,56,100,100,131,0,0,50,50,0],['PawanSuyal',29.3,50,36,58,0,0,0,0,49,100,0],['ShreyasGopal',50,100,46,49,43,50,100,100,0,0,12],['LendlSimmons',111.66,111,120,131,50,100,50,110,113.6,200,131],['AaronFinch',105.1,100,120,0,90,87,131,150,111,112,150],['PragyanOjha',28.3,0,40,12,40,31,69,41,50,0,0],['McClenaghan',52.1,50,50,0,0,110,100,80,31,0,100],['UnmuktChand',121.8,100,200,90,121,131,50,90,105,131,200],['VinayKumar',1030.3,150.7,130,200,87.6,90,131,0,0,141,100],['ParthivPatel',90.7,100,131,111,113,121,100,131,0,100,0],['AidenBizzard',115.36,200,0,0,121,105.6,100,200,131,116,180]]
#Runs=[['RohitSharma',26,27,2,50,4,1,39,59,19,14,51],['LasithMalinga',4.5,0,1,3,7,0,0,13,20,0,1],['KieronPolard',37.3,30,45,56,8,9,65,31,29,49,51].['AmbatiRaydu',33.6,21,35,40,75,29,31,45,60,0,0],['HarbhajanSingh',9,3,5,9,15,16,21,0,0,0,21],['CoreyAnderson',31.4,51,49,34,12,34,71,42,21,0,0],['AdityaTare',22.4,21,30,0,5,16,36,42,33,27,14],['JoshHazlewood',1.3,0,1,5,4,3,0,0,0,0,0],['MercgantDeLange',5.6,12,14,10,9,8,0,0,2,1,0],['PawanSuyal',6,2,8,7,0,0,0,0,12,31,0],['ShreyasGopal',5.2,13,12,1,4,5,7,9,0,0,1],['LendlSimmons',34.1,53,43,31,16,23,5,51,20,29,70],['AaronFinch',46.8,72,43,0,23,26,45,53,69,67,70],['PragyanOjha',3.5,0,8,1,2,4,6,7,7,0,0],['McClenaghan',6.9,2,1,0,0,13,20,12,9,0,12],['UnmuktChand',32.7,68,27,12,40,48,7,8,38,29,50],['VinayKumar',13.7,21,15,16,18,19,21,0,0,12,15],['ParthivPatel',32.6,23,45,69,31,72,43,33,0,10,0],['AidenBizzard',24.5,15,0,0,41,23,13,10,33,21,89]]
#Total_score=[['RohitSharma',156.86,122,115,141,125,157,170,187,157,160,141],['LasithMalinga',153.2,167,142,210,31,154,147,169,131,201,180],['KieronPolard',158.2,168,171,131,127,145,178,156,134,182,190].['AmbatiRaydu',153.5,160,153,142,131,156,176,180,200,121,116],['HarbhajanSingh',153.5,160,153,142,131,156,176,180,200,121,116],['CoreyAnderson',153.5,160,153,142,131,156,176,180,200,121,116],['AdityaTare',153.5,160,153,142,131,156,176,180,200,121,116],['JoshHazlewood',164.1,116,157,180,131,178,165,190,200,201,123],['MercgantDeLange',164.1,116,157,180,131,178,165,190,200,201,123],['PawanSuyal',157.7,123,201,200,190,165,171,131,141,133,122],['ShreyasGopal',162.8,210,123,145,165,176,139,158,190,123,199],['LendlSimmons',168.4,159,160,200,148,167,120,220,159,171,180],['AaronFinch',164.1,116,157,180,131,178,165,190,200,201,123],['PragyanOjha',168.4,159,160,200,148,167,120,220,159,171,180],['McClenaghan',164.1,116,157,180,131,178,165,190,200,201,123],['UnmuktChand',161,168,165,171,185,135,189,142,168,154,133],['VinayKumar',150.1,131,126,189,121,151,146,180,191,131,135],['ParthivPatel',164.8,200,138,190,154,168,171,170,162,145,150],['AidenBizzard',161,168,165,171,185,135,189,142,168,154,133]]


MVP_RCB=[]
MVP_CSK=[]
MVP_MI=[]

TCP=[6.512, 6.72, 6.152, 5.487, 6.651, 5.09, 5.053, 3.876, 5.184, 5.49, 4.046, 5.562, 4.604, 4.988, 5.413, 5.7, 3.2, 5.516, 4.741, 5.76]
tt=[]
for i in range(len(players)):
	mvp=mvp_calculation(400,330,310,PBT[i],PBW[i],PEX[i])

	MVP_RCB.append(mvp)
	

	#mvp_CSK=mvp_calculation(13,10,9,PBT[i],PBW[i],PEX[i])
	#mvp_MI=mvp_calculation(22,19,16,PBT[i],PBW[i],PEX[i])
	
	#MVP_CSK.append(mvp_CSK)
	#MVP_MI.append(mvp_MI)




'''
MVP_RCB=[1.672, 0.962, 1.601, 1.641, 1.575, 1.467, 1.527, 0.322, 0.505, 1.287, 0.114, 1.688, 1.388, 1.504, 0.536, 1.281, 0.96, 1.23, 1.415, 1.724]
MVP_CSK=[2.164, 1.231, 2.092, 2.144, 2.045, 1.952, 2.025, 0.421, 0.657, 1.7, 0.145, 2.253, 1.835, 1.989, 0.659, 1.683, 1.26, 1.59, 1.843, 2.255]
MVP_MI=[2.069, 1.18, 1.996, 2.046, 1.954, 1.857, 1.926, 0.401, 0.627, 1.619, 0.139, 2.141, 1.747, 1.893, 0.636, 1.604, 1.202, 1.52, 1.76, 2.152]
'''