import math
import turtle
import time

Level=0.5
fps=120
fps=1/fps
turtle.tracer(False)
ComScore=turtle.Turtle()
ComScore.shapesize(0.0001,0.00001)
PlayerScore=turtle.Turtle()
PlayerScore.shapesize(0.0001,0.00001)
def distance(x1,y1,x2,y2):
    x=abs(x1-x2)
    y=abs(y1-y2)
    return math.sqrt(x*x+y*y)
class Ball:
    def __init__(self,x,y,r=1,color="red"):
        self.x=x
        self.y=y
        self.r=r
        self.dx=0
        self.dy=0
        self.draw=turtle.Turtle()
        self.draw.shape("circle")
        self.draw.shapesize(r,r)
        self.draw.color(color)
        self.draw.up()
        
        

    def SetPos(self,x,y):
        self.dx=x-self.x
        self.dy=y-self.y
        self.dx/=10
        self.dy/=10

        if self.dx**2+self.dy**2>30**2:
            temp=math.sqrt(self.dx**2+self.dy**2)
            self.dx=self.dx/temp*30
            self.dy=self.dy/temp*30
      
            
        print('Setpos',x,y)
    def ReSet(self,x,y):
        self.x=x
        self.y=y
        self.dx=0
        self.dy=0

        
    def SetPower(self,dx,dy):
        self.dx=dx
        self.dy=dy

    def AddPower(self,dx,dy):
        self.dx+=dx
        self.dy+=dy

    def Move(self):
        self.x+=self.dx
        self.y+=self.dy

    def Slow(self,spd):
        dis=math.sqrt(self.dx**2+self.dy**2)
        dis_t=dis-spd
        if dis_t<=0:
            self.dx=0
            self.dy=0
        else :
            self.dx=self.dx/dis*dis_t
            self.dy=self.dy/dis*dis_t




def angle(x1,y1,x2,y2):
    x=abs(x1-x2)
    y=abs(y1-y2)
    t=0
    if x==0:
        if y1<y2:
            return math.degrees(math.atan(float('inf'))),5
        else:
            return math.degrees(math.atan(float('inf'))),7
        
    if y==0:
        if x1<x2:
            t=6
        else:
            t=8
    else :
        if x1<x2 and y1<y2 :
            t=1
        elif x1>x2 and y1<y2 :
            t=2
        elif x1>x2 and y1>y2:
            t=3
        elif x1<x2 and y1>y2:
            t=4
    return math.degrees(math.atan(y/x)),t

Map=turtle.Turtle()
Map.up()
Map.setpos(-420,420)
Map.down()
Map.fd(840)
Map.right(90)
Map.fd(840)
Map.right(90)
Map.fd(840)
Map.right(90)
Map.fd(840)
Map.right(90)
Map.up()
Map.setpos(-420,0)
Map.down()
Map.fd(840)
Map.shapesize(0.0001,0.00001)
ComScore.up()
ComScore.setpos(-100,400)
ComScore.down()
ComScore.color("red")
ComScore.fd(200)
ComScore.up()
ComScore.setpos(-60,200)
ComScore.pensize(10)
PlayerScore.up()
PlayerScore.setpos(-100,-400)
PlayerScore.down()
PlayerScore.color("blue")
PlayerScore.fd(200)
PlayerScore.up()
PlayerScore.setpos(-60,-200)
PlayerScore.pensize(10)
def ScoreAdd(obj):
    obj.fd(10)
    obj.down()
    obj.fd(10)
    obj.up()
    obj.fd(10)



PlayerPoint=0
ComputerPoint=0
Balllist=[]
Balllist.append(Ball(0,-200,2,'red'))
Balllist.append(Ball(0,200,2,'blue'))
Balllist.append(Ball(0,0,2,'yellow'))
while PlayerPoint<=4 and ComputerPoint<=4:

    Time=0
    Balllist[0].ReSet(0,-200)
    Balllist[1].ReSet(0,200)
    Balllist[2].ReSet(0,0)
    while(True):
        if abs(Balllist[2].y-400)<10 and -100<Balllist[2].x<100:
            ScoreAdd(PlayerScore)
            PlayerPoint+=1
            break
        if abs(Balllist[2].y-(-400))<10 and -100<Balllist[2].x<100:
            ScoreAdd(ComScore)
            ComputerPoint+=1
            break
      

        for i in range(len(Balllist)):
            for j in range(len(Balllist)):
                if not i==j:
                    if distance(Balllist[i].x,Balllist[i].y,Balllist[j].x,Balllist[j].y)<(Balllist[0].r+Balllist[j].r)*10:
                        collangle,t=angle(Balllist[i].x,Balllist[i].y,Balllist[j].x,Balllist[j].y)
                        dx=0
                        dy=0
                        if t>=5 :
                            if t==5:
                                dy=Balllist[i].dy
                                dy*=-1
                                
                            elif t==6:
                                dx=Balllist[i].dx
                                dx*=-1
                            
                            elif t==7:
                                dy=Balllist[i].dy
                            elif t==8:
                                dy=Balllist[i].dx
                            
                                
                        else:
                            power=math.sqrt(Balllist[i].dx**2+Balllist[i].dy**2)
                            power*=math.cos(math.radians(collangle))
                            dx=power*math.cos(math.radians(collangle))
                            dy=power*math.sin(math.radians(collangle))
                            if t==2 or t==3:
                                dx*=-1
                            if t==3 or t==4:
                                dy*=-1
                        
                        Balllist[j].AddPower(dx,dy)



        if distance(Balllist[2].x,Balllist[2].y,Balllist[1].x,Balllist[1].y)<(Balllist[2].r+Balllist[1].r)*10:
            
            collangle,t=angle(Balllist[2].x,Balllist[2].y,Balllist[1].x,Balllist[1].y)
            power=math.sqrt(Balllist[2].dx**2+Balllist[2].dy**2)
            power*=math.cos(math.radians(collangle))
            dx=power*math.cos(math.radians(collangle))
            dy=power*math.sin(math.radians(collangle))
            if t==2 or t==3 :
                dx*=-1
            if t==3 or t==4:
                dy*=-1
            Balllist[1].AddPower(dx,dy)
            
            
        for temp in Balllist:
            temp.Move()
            if not -400<temp.x<400:
                temp.dx*=-1
                temp.Move()
            temp.draw.setpos(temp.x,temp.y)

                
        if not -400< Balllist[0].y<0:
            Balllist[0].dy*=-1
            Balllist[0].Move()
        if not -400< Balllist[2].y<400:
            Balllist[2].dy*=-1
            Balllist[2].Move()
        if not 0< Balllist[1].y<400:
            Balllist[1].dy*=-1
            Balllist[1].Move()
        
        for temp in Balllist:
            temp.Slow(0.4)
        turtle.onscreenclick(Balllist[0].SetPos)
        
        Time+=fps    
        time.sleep(fps)
        turtle.update()
        
        if Time > Level :
            Time=0
            
            if Balllist[2].y>=0:
                if distance(Balllist[2].x,Balllist[2].y,Balllist[1].x,Balllist[1].y)<=100:
                    temp=distance(Balllist[2].x,Balllist[2].y,Balllist[1].x,Balllist[1].y)
                    
                    tx=Balllist[1].x-Balllist[2].x
                    ty=Balllist[1].y-Balllist[2].y
                    tx=tx/temp*300
                    ty=ty/temp*300
                    Balllist[1].SetPos(Balllist[1].x-tx,Balllist[1].y-ty)
                elif Balllist[1].y<=Balllist[2].y:
                    if Balllist[1].x>Balllist[2].x:
                        Balllist[1].SetPos(Balllist[2].x+40,Balllist[2].y+20)
                    else:
                        Balllist[1].SetPos(Balllist[2].x-40,Balllist[2].y+20)
                        
                    
                else :
                    Balllist[1].SetPos(Balllist[2].x,Balllist[2].y)
        


