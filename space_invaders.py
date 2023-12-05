#Space Invaders
#python 2.7.12 on Mac
# Thanks to Christian Thompson 
# Python Game Programming Tutorial: Space Invaders
# http://christianthompson.com/

import winsound
import turtle
import os
import math
import random

#Set up the screen

win = turtle.Screen()
win.bgcolor("black")
win.title("Space Invaders")
win.bgpic("space_invaders_background.gif")

#Register the graphics for the game
turtle.register_shape("invader.gif")
#turtle.register_shape("red_invader.gif")
turtle.register_shape("player.gif")

#Mavredakis graphics
turtle.register_shape("gameover.gif")
turtle.register_shape("red_invader.gif")

#Draw border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pensize(3)
border_pen.pendown()
for side in range(4):
  border_pen.fd(600)
  border_pen.lt(90)
border_pen.hideturtle()

#Set the score to 0
score = 100 #0 Modified by Mavredakis

#Draw the score on stage
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290,280)
scorestring = "Score: %s" %score
score_pen.write(scorestring, False, align="left", font = ("Arial", 14, "bold"))
score_pen.hideturtle()

#Create the player turtle
player = turtle.Turtle()
player.color("blue")
player.shape("player.gif")
player.speed(0)
player.penup()
player.setposition(0, -250)
player.setheading(90)

playerspeed = 15

#Choose number of enemies
#global number_of_enemies
number_of_enemies = 4 #5 Modified by Mavredakis
#Mavredakis for task 7
counter = number_of_enemies
gameover = turtle.Turtle()

#Create an empty list of enemies
enemiesList = []

#Add enemies to the list
#We need to create more turtle objects

for i in range(number_of_enemies):
  #Create the enemy
  enemiesList.append(turtle.Turtle())
  #enemyspeed = random.randint(1,10) #Added by Mavredakis

for enemy in enemiesList:
  #if greenKilled(True):
  #  enemy.color("red")
  #else:	
  enemy.color("green")#red Modified by Mavredakis
  #enemy.shape("invader.gif") #Modified by Mavredakis for part 5
  #enemy.speed(random.randint(1,3))
  enemy.speed(0)
  enemy.penup()
  x = random.randint(-200, 200)
  y = random.randint(100, 200)
  enemy.setposition(x, y)
  #enemyspeed = random.randint(1, 10) #Added by Mavredakis	
#Next line commented by Mavredakis
enemyspeed = 2 #random.randint(1, 10) #Added by Mavredakis #2

#Create the player's bullet
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.speed(0)
bullet.penup()
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

bulletspeed = 20

#Define bullet state
#we have 2 states:
#ready - ready to fire bullet
#fire - bullet is firing

bulletstate = "ready"


#Mavredakis - enemy_speed
def enemy_speed():
  es = random.randint(1, 3)
  return es  


#Move the player left and right

def move_left():
  x = player.xcor()
  x = x - playerspeed
  if x < -280:
    x = -280
  player.setx(x)

def move_right():
  x = player.xcor()
  x = x + playerspeed
  if x > 280:
    x = 280
  player.setx(x)

def fire_bullet():
  #Declare bulletstate as a global if it needs change
  global bulletstate
  #Mavredakis
  #Update the score - Mavredakis NOK
  #score = score - 1
  #scorestring = "Score: %s" %score
  #score_pen.clear()
  #score_pen.write(scorestring, False, align="left", font = ("Arial", 14, "bold"))
  if bulletstate == "ready":
    os.system("afplay laser.wav&")
    #for linux use os.system("aplay laser.wav&")
    #Move the bullet to just above the player
    x = player.xcor()
    y = player.ycor() + 10
    bullet.setposition(x,y)
    bullet.showturtle()
    bulletstate = "fire"
	#Update the score - Mavredakis OK
    global score
    score -= 1
    scorestring = "Score: %s" %score
    score_pen.clear()
    score_pen.write(scorestring, False, align="left", font = ("Arial", 14, "bold"))
    

def isCollision(t1,t2):
  distance = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(),2))
  if distance < 15:
    #Mavredakis for task 5
    #greenKilled(True)
    return True
  else:
    return False

#Mavredakis for task 5
def greenKilled(value):
  if value == True:
    return True
  else:
    return False

#create keyboard bindings
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(fire_bullet, "space")


#Main game loop
while True:
  for enemy in enemiesList:
    #print(enemy)
    #This is a forever loop
    #Move the enemy
    x = enemy.xcor()
	#Mavredakis
    #enemyspeed = 2 #random.randint(1, 3)
    #if enemy == "<turtle.Turtle object at 0x00000269DBC60C40>":
    #  enemyspeed = random.randint(1, 10);
    #elif enemy == "<turtle.Turtle object at 0x00000269DBC60D90>":
    #  enemyspeed = random.randint(1, 3);
    #elif enemy == "<turtle.Turtle object at 0x00000269DBC60EE0>":
    #  enemyspeed = random.randint(1, 3);
    #elif enemyspeed == "<turtle.Turtle object at 0x00000269DBC61030>":
    #  enemyspeed = random.randint(1, 3);
	
    x = x + enemyspeed #enemy_speed() #random.randint(1, 10) #Added by Mavredakis #enemyspeed
	#Mavredakis
    #if (x < 280):
    enemy.setx(x)
	  
    #print(enemy.setx(x))

    #Move enemy back and down
    if enemy.xcor() > 280:
      enemyspeed =  enemyspeed * -1
	  #enemy_speed()
      y = enemy.ycor()
      y = y - 40
      enemy.sety(y)
    if enemy.xcor() < -280:
      enemyspeed = enemyspeed  * -1
      y = enemy.ycor()
      y = y - 40
      enemy.sety(y)

    #Check for collision between bullet and enemy
    if isCollision(bullet, enemy):
      os.system("afplay explosion.wav&")
      #for linux use os.system("aplay explosion.wav&") 
      #Reset the bullet
      bullet.hideturtle()
      bulletstate = "ready"
      bullet.setposition(0, -400)
	  
      #Mavredakis for task 6
      if enemy.color() == ('red', 'red'):
        score += 20
        enemy.hideturtle()
        #global counter	
        print(counter)		
        if counter == 1:
          #Game over
          gameover.setposition(0, 0)
          gameover.shape("gameover.gif")
          #TODO exit game
        else:
          counter -= 1
      else:		
        score += 10
	  #if enemy.color("green"):
	  #Mavredakis for task 5
      enemy.shape("red_invader.gif")
      enemy.color("red")
      #Reset the enemy
	  #Mavredakis
      for i in [1, 2]:
        x = random.randint(-200, 200)
        y = random.randint(100, 200)
        enemy.setposition(x, y)
      #x2 = random.randint(-50, 50)
      #y2 = random.randint(100, 200)
      #enemy.setposition(x2, y2)
      #Update the score
	  #Mavredakis for task 6
      #if enemy.color() == ('red', 'red'):
      #  score += 20
      #else:		
      #  score += 10
      #print(enemy.color())
      scorestring = "Score: %s" %score
      score_pen.clear()
      score_pen.write(scorestring, False, align="left", font = ("Arial", 14, "bold"))

    #Check for collision between enemy and player
    if isCollision(player, enemy):
      os.system("afplay explosion.wav&")
      #for linux use os.system("aplay explosion.wav&") 
      player.hideturtle()
      enemy.hideturtle()
      print("GAME OVER")
      break

  #Move the bullet only when bulletstate is "fire"
  if bulletstate == "fire":
    y = bullet.ycor()
    y = y + bulletspeed
    bullet.sety(y)
	#Update the score - Mavredakis
#    score_decreased = False
#    if score_decreased == False:
#      score -= 1
#      scorestring = "Score: %s" %score
#      score_pen.clear()
#      score_pen.write(scorestring, False, align="left", font = ("Arial", 14, "bold"))
#      score_decreased = True

  #Check to see if bullet has reached the top
  if bullet.ycor() > 275:
    bullet.hideturtle()
    bulletstate = "ready"






#delay = raw_input("Press enter to finish")