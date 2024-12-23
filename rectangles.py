
#Rectangles using OOP concept
#import and initialize pygame 
import pygame
pygame.init()

#set dimensions of the screen
screen=pygame.display.set_mode((1200,800))


#Colors
#screen fil

#creating a Rectangle class
class drawrec():
    #initializd/constucter
    def __init__(self,colour,dimensens):
        print("nathan")
        self.rec_surface=screen
        self.rec_colour=colour
        self.rec_dimen=dimensens
        #function to draw rectagal
    def rec(self):
        self.nathan=pygame.draw.rect(self.rec_surface,self.rec_colour,self.rec_dimen)
#creating Instances   
bluerec=drawrec("red",(100,100,100,75)) 
bluerec.rec()

yellowrec=drawrec("yellow",(200,200,150,100))
yellowrec.rec()
#accessing methods 
#Display update to reflect the things on screeen






















pygame.display.update()
input()