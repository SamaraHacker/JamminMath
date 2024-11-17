import pygame
import turtle as t
from mathFunctions import basicProblem
import time
import webbrowser


#Puts lock image on jam types and unlocks when they are removed
def Unlock(lockedIcon):
    threshold = 10
    screen.blit(pygame.transform.scale2x(lockedIcon), (605, 15))
    screen.blit(pygame.transform.scale2x(lockedIcon), (605, 115))
    screen.blit(pygame.transform.scale2x(lockedIcon), (605, 215))
    screen.blit(pygame.transform.scale2x(lockedIcon), (605, 315))
    screen.blit(pygame.transform.scale2x(lockedIcon), (605, 415))
    screen.blit(pygame.transform.scale2x(lockedIcon), (605, 515))

    upgradeBtn1.unlocked = True
    grapeConveyor.unlocked = True
    if upgradeBtn1.level > threshold:
        upgradeBtn2.unlocked = True
        apricotConveyor.unlocked = True
    if upgradeBtn2.level > threshold:
       upgradeBtn3.unlocked = True
       appleConveyor.unlocked = True
    if upgradeBtn3.level > threshold:
       upgradeBtn4.unlocked = True
       blueberryConveyor.unlocked = True
    if upgradeBtn4.level > threshold:
       upgradeBtn5.unlocked = True
       blackberryConveyor.unlocked = True
    if upgradeBtn5.level > threshold:
        upgradeBtn6.unlocked = True
        roseConveyor.unlocked = True
       
#Handles the math window where the equation outputs
class mathWindow:
    def __init__(self):
        self.mathWindow = pygame.Rect(0, 0, 600, 600)
        self.window_font = pygame.font.Font(None, 25)
        self.answerSubmitted = True
        self.helpButton = pygame.Rect(490, 30, 100, 50)

    def windowPopup(self, mathType, level):#doesnt work
        self.answerSubmitted= False
        self.mathType = mathType

        self.init=basicProblem(mathType, int(level/5))#mathType, difficulty
        self.ans = basicProblem.executeProblem(self.init)

        self.eqn = self.ans[0]#basicProblem(mathType, int(level/5)
        self.ans = self.ans[1]
        self.refresh()

    def getHelp(self, mathType):#Enters videos
        if mathType == 0:#add
            webbrowser.open("https://www.youtube.com/watch?v=1KxEXKKBndk")
        elif mathType == 1:#sub
            webbrowser.open("https://www.youtube.com/watch?v=N2UWPVldcQs")
        elif mathType == 2:#mult
            webbrowser.open("https://www.youtube.com/watch?v=RkwoTtljLU4")
        elif mathType == 3:#div
            webbrowser.open("https://www.youtube.com/watch?v=6Fy2G4yo2T4")
        elif mathType == 4:#pow
            webbrowser.open("https://www.youtube.com/watch?v=uRu3atMemPw")
        elif mathType == 5:#root
            webbrowser.open("https://www.youtube.com/watch?v=-VAqyuNW_ss")
        

    def refresh(self):
        pygame.draw.rect(screen, "#ffffff", self.mathWindow)
        pygame.draw.rect(screen, "#0000ff", self.helpButton)
        self.helpBtnLbl2 = self.window_font.render("Video", True, "#c3c3c3")
        screen.blit(self.helpBtnLbl2, (515, 47))
        self.helpBtnLbl = self.window_font.render("Need Help?", True, "#000000")
        screen.blit(self.helpBtnLbl, (495, 10))

        self.mouse_pos = pygame.mouse.get_pos()
        if self.helpButton.collidepoint(self.mouse_pos):
            if pygame.mouse.get_pressed()[0]:
                self.getHelp(self.mathType)
                time.sleep(1)


        self.problemDeclaration = text_font.render(f"Solve: {self.eqn}", True, "#000000")
        screen.blit(self.problemDeclaration, (200, 125))
        self.secLine = self.window_font.render("(Round to nearest whole number if applicable)", True, "#000000")
        if self.mathType == 3:
            screen.blit(self.secLine, (115, 175))
        
#Handles any button presses and updates Jam values
class BuyButton:
    def __init__(self, upgradeCost, scoreGiven, yLoc, image, mathType, name):
        self.yLoc = yLoc
        self.button = pygame.Rect(685, yLoc+50, 100, 40)
        self.button_color = "#101010"
        self.bgColor = "#e3e3e3"

        self.mathType = mathType
        self.name = name

        self.unlocked = False

        self.clicked = False
        self.upgrade_description=''
        self.scoreGiven = scoreGiven
        self.level = 0
        self.mps = 0
        self.buttonFont = pygame.font.Font(None, 25)
        self.cashFont = pygame.font.Font(None, 20)

        self.display_cost=0

        self.upgrade_cost = upgradeCost

        self.bg = pygame.Rect(600, yLoc, 200, 95)

        self.jamIcon = pygame.image.load(image)
        
    def onStart(self):
        pygame.draw.rect(screen, self.bgColor, self.bg)
        pygame.draw.rect(screen, self.button_color, self.button)
    
    def updateUi(self):
        self.upgrade_description = self.buttonFont.render(f"+{self.mps}$/sec", True, "#000000")
        self.display_cost = self.cashFont.render(f"Cost: {str(self.upgrade_cost*(1+self.level))}", True, "#ffffff")
        self.display_title = self.buttonFont.render(f"{self.name} Jam", True, "#000000")
        self.display_level = self.buttonFont.render(f"Level {self.level}", True, "#000000")
        screen.blit(self.display_level, (670, self.yLoc+30))
        screen.blit(self.display_title, (670, self.yLoc+10))
        screen.blit(self.upgrade_description, (605, self.yLoc+75))
        screen.blit(self.display_cost, (690, self.yLoc+60))
        if self.unlocked:
            screen.blit(pygame.transform.scale2x(self.jamIcon), (605, self.yLoc+5))

    
    def click_button(self):
        self.mouse_pos = pygame.mouse.get_pos()
        if self.button.collidepoint(self.mouse_pos):
            if pygame.mouse.get_pressed()[0]:
                self.clicked = True
            else:
                if self.clicked:
                    #enter math popup
                    if self.unlocked:
                        if game.money >= self.upgrade_cost*(self.level+1):
                            mathWindowPopup.windowPopup(self.mathType, self.level)
                
                    self.clicked = False
        
    def onCheckAnswer(self):
        #print(mathWindowPopup.ans, " | ", user_text)
        if str(int(mathWindowPopup.ans)) == user_text:
            returnStr = "Correct!"
            rtnColor = "#00c04b"
            pos = (225, 400)
            game.mps += self.scoreGiven
            self.mps += self.scoreGiven
            self.level += 1
            game.money-= self.upgrade_cost*self.level
        else:
            returnStr = "False"
            rtnColor = "#e60000"
            pos = (250, 400)
            game.money -= self.upgrade_cost*self.level*0.5
        outputFont = pygame.font.Font(None, 50)
        outputStr = outputFont.render(returnStr, True, rtnColor)
        if str(int(mathWindowPopup.ans)) != user_text:
            correctAnswer = outputFont.render("The answer is: "+str(int(mathWindowPopup.ans)), True, rtnColor)
        else:
            correctAnswer = outputFont.render("", True, rtnColor)
        screen.blit(correctAnswer, (160, 500))
        screen.blit(outputStr, pos)
        
        
        





    def render(self):
        self.click_button()
        
#Hangles conveyer animations
class Conveyers:
    def __init__(self, frame1, frame2, x, y):#bool, str, str, int, int
        self.frame1 = frame1
        self.frame2 = frame2
        self.location = (x, y)
        self.iterator = 0
        self.speed = 20
        self.unlocked = 0
        self.curFrame = "AnimationFrames/EmptyConveyer.png"
    
    def anim(self, run):
        self.iterator+=1
        if self.unlocked:
            if not run:
                self.curFrame="AnimationFrames/EmptyConveyer.png"
            elif self.iterator%self.speed==0:
                if self.curFrame == self.frame1:
                    self.curFrame = self.frame2
                else:
                    self.curFrame = self.frame1
            animFrame = pygame.image.load(self.curFrame)
            screen.blit(animFrame, (self.location)) 
       

#Handles images and important vars
class Game:
    def __init__(self):
        self.mps = 0
        self.money = 5
  
        self.game_font = pygame.font.Font(None, 15)
        
    
    def increaseMoney(self):
        #Divided by fps
        self.money+=self.mps/60


    def updateConveyers(self):
        #Runs animation based on what jams are unlocked/bought
        if upgradeBtn1.level == 0:
            #print(":C")
            grapeConveyor.anim(False)
        else:
            #print("huh")
            grapeConveyor.anim(True)
        if upgradeBtn2.unlocked:
            if upgradeBtn2.level == 0:
                apricotConveyor.anim(False)
            else:
                apricotConveyor.anim(True)
        if upgradeBtn3.unlocked:
            if upgradeBtn3.level == 0:
                appleConveyor.anim(False)
            else:
                appleConveyor.anim(True)
        if upgradeBtn4.unlocked:
            if upgradeBtn4.level == 0:
                blueberryConveyor.anim(False)
            else:
                blueberryConveyor.anim(True)
        if upgradeBtn5.unlocked:
            if upgradeBtn5.level == 0:
                blackberryConveyor.anim(False)
            else:
                blackberryConveyor.anim(True)
        if upgradeBtn6.unlocked:
            if upgradeBtn6.level == 0:
                roseConveyor.anim(False)
            else:
                roseConveyor.anim(True)
        


    def draw_score(self):
        self.display_score = scoreFont.render(f"Money: {str(int(self.money))}", True, "#000000")
        screen.blit(self.display_score, (25,25))

    

    def render(self):
        background = pygame.image.load("Background.png")
        screen.blit(background, (0,0))

        self.updateConveyers() 

        storeIcon = pygame.image.load("Store.png")
        screen.blit(storeIcon, (50, 50))
        screen.blit(storeIcon, (50, 350))       

        self.draw_score()

#Inits variables
pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

game = Game()

#Inits buttons/jam type interface
upgradeBtn1 = BuyButton(5, 2, 10, "grape.png", 0, "Grape")
upgradeBtn2 = BuyButton(70, 7, 110, "Apricot.png", 1, "Apricot")
upgradeBtn3 = BuyButton(250, 13, 210, "Apple.png", 2, "Apple")
upgradeBtn4 = BuyButton(700, 22, 310, "Blueberry.png", 3, "Blueberry")
upgradeBtn5 = BuyButton(2000, 28, 410, "Blackberry.png", 4, "Blackberry")
upgradeBtn6 = BuyButton(10000, 37, 510, "Rose.png", 5, "Rose")

#Inits conveyer images
grapeConveyor = Conveyers("AnimationFrames/GrapeConveyer1.png", "AnimationFrames/GrapeConveyer2.png", 340, 60)
apricotConveyor = Conveyers("AnimationFrames/ApricotConveyer1.png", "AnimationFrames/ApricotConveyer2.png", 340, 140)
appleConveyor = Conveyers("AnimationFrames/AppleConveyer1.png", "AnimationFrames/AppleConveyer2.png", 340, 220)
blueberryConveyor = Conveyers("AnimationFrames/BlueberryConveyer1.png", "AnimationFrames/BlueberryConveyer2.png", 340, 360)
blackberryConveyor = Conveyers("AnimationFrames/BlackberryConveyer1.png", "AnimationFrames/BlackberryConveyer2.png", 340, 440)
roseConveyor = Conveyers("AnimationFrames/RoseConveyer1.png", "AnimationFrames/RoseConveyer2.png", 340, 520)

#Inits math window popup
mathWindowPopup=mathWindow()

#Creates display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Jammin' Math")

#Inits text font
text_font = pygame.font.Font(None, 50)
scoreFont = pygame.font.Font(None, 25)

#Inits clock
clock = pygame.time.Clock()

#creates the locked images covering locked jams
lockedIcon = pygame.image.load("lock.png")

#Inits variables for while loop
run = True
needToStallToShowResult = False
user_text = ''

while run:

    if needToStallToShowResult:#Stalls to show incorrect or correct
        time.sleep(2)
        needToStallToShowResult = False
    if mathWindowPopup.answerSubmitted: #When you're not solving a math problem, following elements renders
        game.render()

        #OnStart should not be function name - runs continuously
        upgradeBtn1.onStart()
        upgradeBtn2.onStart()
        upgradeBtn3.onStart()
        upgradeBtn4.onStart()
        upgradeBtn5.onStart()
        upgradeBtn6.onStart()
        
        if not upgradeBtn6.unlocked:
            Unlock(lockedIcon)

        upgradeBtn1.updateUi()
        upgradeBtn2.updateUi()
        upgradeBtn3.updateUi()
        upgradeBtn4.updateUi()
        upgradeBtn5.updateUi()
        upgradeBtn6.updateUi()
        
        
    #Gets cursor position
    cursor = pygame.mouse.get_pos()

    #Checks if an event happens
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #If x is clicked, exits program
            run = False
        if event.type == pygame.KEYDOWN: #If a key is pressed
            if event.key == pygame.K_BACKSPACE: #If backspace is pressed, it deletes the previous character typed
                user_text = user_text[:-1]
            elif event.key == pygame.K_RETURN: #If enter is pressed
                if user_text != '': #If the input is not blank
                    if user_text.isnumeric() or user_text[0] == "-": #Checks if the number is numeric or negative
                        mathWindowPopup.answerSubmitted = True

                        #figure out which button was pressed
                        buttonList = [upgradeBtn1, upgradeBtn2, upgradeBtn3, upgradeBtn4, upgradeBtn5, upgradeBtn6]
                        buttonList[mathWindowPopup.mathType].onCheckAnswer()
                    
                    #Clears text
                    user_text = ""
                    needToStallToShowResult = True
            else:
                #When key is pressed in mathWindow, key is added to display string
                if not mathWindowPopup.answerSubmitted:
                    user_text += event.unicode

    if not mathWindowPopup.answerSubmitted: #If scurrently solving a math problem, show string
        input_label = scoreFont.render("Solution:", True, "#000000")
        mathWindowPopup.refresh()
    else: #Clears
        input_label = scoreFont.render("", True, "#000000")
    
    #Displays labels
    screen.blit(input_label, (255,300))
    input_surface = scoreFont.render(user_text, True, "#000000")
    screen.blit(input_surface, (290-len(user_text)*3,350))
    

    upgradeBtn1.render()
    upgradeBtn2.render()
    upgradeBtn3.render()
    upgradeBtn4.render()
    upgradeBtn5.render()
    upgradeBtn6.render()

    
    #Makes it 60 fps
    clock.tick(60)
    game.increaseMoney()

    pygame.display.update()

pygame.quit()