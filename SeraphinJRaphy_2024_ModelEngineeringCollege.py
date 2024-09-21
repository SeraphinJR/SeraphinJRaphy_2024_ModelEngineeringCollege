import pygame as py , sys
py.init()

#Making the background
root=py.display.set_mode((760,760))
root.fill((150,150,150))
py.display.set_caption('Pookalam')

#A couple of transparent surfaces
s=py.Surface((380,380),py.SRCALPHA)
s.fill((0,255,255,0))
extra=py.Surface((60,30),py.SRCALPHA)
extra.fill((0,255,255,0))

# One quadrant of designs
py.draw.circle(s,(255, 252, 53),(380,150),145)
py.draw.circle(s,(255, 252, 53),(150,380),145)
py.draw.circle(s,(255, 252, 53),(220,215),145)

py.draw.circle(s,(216, 112, 21),(380,150),125)
py.draw.circle(s,(216, 112, 21),(150,380),125)
py.draw.circle(s,(216, 112, 21),(220,215),125)

py.draw.circle(s,(216, 112, 156),(380,150),105)
py.draw.circle(s,(216, 112, 156),(150,380),105)
py.draw.circle(s,(216, 112, 156),(220,215),105)

py.draw.circle(s,(198, 82, 8),(180,180),30)
py.draw.circle(s,(255, 204, 0),(180,180),20)

py.draw.circle(s,(198, 82, 8),(380,90),30)
py.draw.circle(s,(255, 204, 0),(380,90),20)

py.draw.circle(s,(198, 82, 8),(90,380),30)
py.draw.circle(s,(255, 204, 0),(90,380),20)

py.draw.circle(s,(106, 46, 53),(380,380),250)


py.draw.circle(s,(216, 112, 21),(200,305),50)
py.draw.circle(s,(216, 112, 21),(310,200),50)

coords=[(180,380),(160,335),(200,315)],[(200,255),(200,315),(245,245)],[(260,195),(245,245),(310,200)],[(336,158),(310,200),(380,180)]

for i in coords:
    py.draw.polygon(s,(216, 112, 21),i)


py.draw.circle(s,(0, 180, 35),(380,380),200)
py.draw.circle(s,(255, 252, 53),(380,380),175)
py.draw.circle(s,(209, 5, 46),(380,380),150)
py.draw.circle(s,(97, 11, 24),(380,380),125)


p=(380,280),(280,380),(295,332),(330,295)

x,y=280,380
for i in p:
     py.draw.circle(s,(191, 92, 172),i,25)
     x+=25
     y-=25

py.draw.circle(s,(197, 192, 142),(380,380),100)
py.draw.circle(s,(75, 6, 5),(380,380),80)
py.draw.circle(s,(174, 26, 2),(350,380),30)
py.draw.circle(s,(174, 26, 2),(380,350),30)
py.draw.circle(s,(255,0,0),(380,380),20)
py.draw.polygon(s,(231, 189, 29),[(310,310),(350,340),(380,380),(340,350)])
py.draw.polygon(s,(112, 44, 84),[(280,380),(320,370),(380,380)])
py.draw.polygon(s,(112, 44, 84),[(380,280),(370,320),(380,380)])
py.draw.circle(s,(231, 189, 29),(380,380),5)

#Duplicating the quadrants
q3=py.transform.rotate(s,90)
q2=py.transform.rotate(s,180)
q1=py.transform.rotate(s,270)

#Displaying all the quadrants
root.blit(s,(0,0))
root.blit(q3,(0,380))
root.blit(q2,(380,380))
root.blit(q1,(380,0))

#Working on the face (minimalistic lol)
r1=py.Rect(260,540,235,125)
r2=py.Rect(305,415,150,75)
r3=py.Rect(318,400,125,75)

py.draw.circle(root,(216, 112, 156),(380,600),105)

py.draw.ellipse(root,(231, 189, 29),(345,380,75,50))
py.draw.ellipse(root,(0, 116, 0),r3)
py.draw.ellipse(root,(255, 116, 0),r2)

py.draw.ellipse(root,(255, 255, 255),(250,552,175,125))
py.draw.ellipse(root,(255, 255, 255),(330,552,175,125))
py.draw.ellipse(root,(255, 255, 255),(250,560,250,125))


py.draw.circle(root,(7, 125, 33),(380,530),100)
py.draw.ellipse(root,(7, 125, 33),r1)

py.draw.circle(root,(198, 82, 8),(470,501),25)
py.draw.circle(root,(255, 204, 0),(470,501),15)

py.draw.circle(root,(198, 82, 8),(470,537),20)
py.draw.circle(root,(255, 204, 0),(470,537),12)


py.draw.circle(root,(198, 82, 8),(290,501),25)
py.draw.circle(root,(255, 204, 0),(290,501),15)

py.draw.circle(root,(198, 82, 8),(290,537),20)
py.draw.circle(root,(255, 204, 0),(290,537),12)

py.draw.ellipse(extra,(180,0,0),(0,15,50,30))

py.display.flip()

#Making a way for the window to close
while True:
    for event in py.event.get():
            if event.type==py.QUIT:
                py.quit() 
                sys.exit()
