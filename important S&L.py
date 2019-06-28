from graphics import *
import random
player1=0
player2=0
ladders = {1:38,4:14,9:31,21:42,28:84,36:44,51:67,54:71}
snakes = {98:8,95:72,64:31,62:24,56:21,49:33,48:26,16:6}
win = GraphWin("Snakes And Ladders", 1280,720)



def main(win):
    win.setCoords(0,0,10,12)
    gameboard(win)
def gameboard(win):
    text=Text(Point(5,11),"SNAKES AND LADDERS")
    text.setSize(35)
    text.setFill("cyan")
    text.setStyle("italic")
    text.setFace("arial")
    text.draw(win)

    
    for i in range(0,11):
        horizontal=Line(Point(0,i),Point(10,i))
        horizontal.draw(win)
        vertical=Line(Point(i,0),Point(i,10))
        vertical.draw(win)
    number=1
    for i in range (0,10):
        if(i%2==0):
            for j in range(0,10):
                text=Text(Point(j+0.5,i+0.5),number)
                number=number+1
                text.draw(win)
        else:
            for j in range(9,-1,-1):
                text=Text(Point(j+0.5,i+0.5),number)
                number=number+1
                text.draw(win)

    for key,values in snakes.items():
            x=(key)%10
            y=int((key)/10)
            if(y%2==0):
                if(x==0):
                    x=10
                s1=Point(x-0.5,y+0.5)
            else:
                x=11-x
                s1=Point(x-0.5,y+0.5)
                
            x=(values)%10
            y=int((values)/10)
            if(y%2==0):
                if(x==0):
                    x=10
                s2=Point(x-0.5,y+0.5)
            else:
                x=11-x
                s2=Point(x-0.5,y+0.5)
            snake=Line(s1,s2)
            snake.setWidth(3)
            snake.setFill("Red")
            snake.draw(win)
    for key,values in ladders.items():
            x=(key)%10
            y=int((key)/10)
            if(y%2==0):
                if(x==0):
                    x=10
                l1=Point(x-0.5,y+0.5)
            else:
                x=11-x
                l1=Point(x-0.5,y+0.5)
                
            x=(values)%10
            y=int((values)/10)
            if(y%2==0):
                if(x==0):
                    x=10
                l2=Point(x-0.5,y+0.5)
            else:
                x=11-x
                l2=Point(x-0.5,y+0.5)
            ladder=Line(l1,l2)
            ladder.setWidth(3)
            ladder.setFill("blue")
            ladder.draw(win)

                
def roll_dice(r):
    win2=GraphWin("Rolling of Dice",200,200)
    d=random.randint(1,6)
    dice=Text(Point(100,100),d)
    dice.draw(win2)
    win2.getMouse()
    win2.close()
    return(d+r)


def check_for_snakes_and_ladders(n,snakes,ladders):

	if (n in ladders):
		print ("Its a ladder,Climb up")
		n = ladders[n]
	elif (n in snakes):
		print ("Its a snake!!,Come down")
		n = snakes[n]
	return(n)


main(win)
x11=0
y11=0
x22=0
y22=0
pawn1=Text(Point(x11,y11),"A")
pawn2=Text(Point(x22,y22),"B")
pawn1.setFace("arial")
pawn1.setStyle("bold")
pawn1.setSize(18)
pawn2.setFace("arial")
pawn2.setStyle("bold")
pawn2.setSize(18)
pawn1.draw(win)
pawn2.draw(win) 
while(player1 < 100 or player2 < 100):
           

            print("Its turn of player1\n")
            player1 = roll_dice(player1)
            player1 = check_for_snakes_and_ladders(player1,snakes,ladders)
            print("Current status of Player1:",player1,"and Player2:",player2)
            

            
            x1=(player1)%10
            y1=int((player1)/10)
            if(y1%2==0):
                if(x1==0):
                    x1=10
                    y1=y1-1
                pawn1.move((x1-0.5)-x11,(y1+0.5)-y11)
            else:
                x1=11-x1
                pawn1.move((x1-0.5)-x11,(y1+0.5)-y11)               
            win.getMouse()            
            if (player1 > 99):
                    win3=GraphWin("winner",320,480)
                    win3.setCoords(0,0,1,1)
                    winner=Text(Point(0.5,0.5),"WINNER ""A"" ")
                    winner.setSize(35)
                    winner.draw()
                    win3.getmouse()
                    win3.close()
                    win.close()                                                                         #winners condition
                    print ("Winner of the game is player1")
                    
                    break

            print ("Its turn of player2\n")
            player2 = roll_dice(player2)
            player2 = check_for_snakes_and_ladders(player2,snakes,ladders)
            print ("Current status of Player1:",player1," and Player2:",player2)

            x2=player2%10
            y2=int(player2/10)
            if(y2%2==0):
                if(x2==0):
                    x2=10
                    y2=y2-1
                pawn2.move((x2-0.5)-x22,(y2+0.5)-y22)
            else:
                x2=11-x2
                pawn2.move((x2-0.5)-x22,(y2+0.5)-y22)
            win.getMouse()
            
            if (player2 > 99):
                    win3=GraphWin("winner",320,480)
                    win3.setCoords(0,0,1,1)
                    winner=Text(Point(0.5,0.5),"WINNER ""B"" ")
                    winner.setSize(35)
                    winner.draw()
                    win3.getmouse()
                    win3.close()                
                    win.close()                                                                             #winners condition
                    print ("Winner of the game is player2")
                    break
                
            x11=x1-0.5
            y11=y1+0.5
            x22=x2-0.5
            y22=y2+0.5
           
