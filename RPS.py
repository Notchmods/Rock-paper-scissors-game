import random
Score = 0
Enemyscore=0
while(True):
 RPS = input("Rock, Paper or Scissors?")
 if(RPS =="Scissors"):
     algorithm = random.randint(0,2)
     if(algorithm == 2):
         print("Your opponents has chosen paper, you win")
         Score = Score+1
         print(Score,"-",Enemyscore)
     if(algorithm == 0):
         print("Your opponents has chosen scissors, you draw")
         print(Score,"-",Enemyscore)
     if(algorithm == 1):
        print("Your opponents has chosen rock, you lose")
        Enemyscore= Enemyscore+1
        print(Score,"-",Enemyscore)
 if(RPS =="Paper"):
     algorithm = random.randint(0,2)
     if(algorithm == 2):
         print("Your opponents has chosen paper, you draw")
         print(Score,"-",Enemyscore)
     if(algorithm == 0):
         print("Your opponents has chosen scissors, you lose")
         Enemyscore= Enemyscore+1
         print(Score,"-",Enemyscore)
     if(algorithm == 1):
        print("Your opponents has chosen rock, you win")
        Score = Score+1
        print(Score,"-",Enemyscore)
 if(RPS =="Rock"):
     algorithm = random.randint(0,2)
     if(algorithm == 2):
         print("Your opponents has chosen paper, you lose")
         Enemyscore= Enemyscore+1
         print(Score,"-",Enemyscore)
     if(algorithm == 0):
         print("Your opponents has chosen scissors, you win")
         Score = Score+1
         print(Score,"-",Enemyscore)
     if(algorithm == 1):
         print("Your opponents has chosen rock, you draw")
         print(Score,"-",Enemyscore)

