import pyautogui
import os
import time
path = (os.path.dirname(os.path.abspath(__file__)))
path=path.capitalize()
path=(path.replace('\\', '\\\\'))
path=(path+"\\\\")
print (path)
c=0
def kar(img):
            a=0
            addval=((path)+str(img)+".PNG")
            while a<1:
                try:
                    
                    x,y = pyautogui.locateCenterOnScreen(addval,confidence=0.8,grayscale=True)
                    pyautogui.click(x,y)
                    print(x,y)
                    a=30
                except:
                        print("**image name** |"+str(img)+ "| **No of Try** |" +str(a)+"|")
                        a=a+1
                else:
                    a=a+1
                    print ("succes "+str(img))

def passw(img):
            a=0
            addval=((path)+str(img)+".PNG")
            while a<1:
                try:
                    
                    x,y = pyautogui.locateCenterOnScreen(addval,confidence=0.9,grayscale=True)
                    pyautogui.click(x,y)
                    print(x,y)
                    a=30
                except:
                        print("**image name** |"+str(img)+ "| **No of Try** |" +str(a)+"|")
                        a=a+1
                else:
                    a=a+1
                    c=2
                    print ("succes "+str(img))  
                    return c       


while True:
        kar("edit")
        kar("nextblue")
        kar("nokids")
        kar("nextblue")
        kar("nextblue")
        kar("nextblue")
        kar("public")
        kar("save")
        kar("CLOSE")
        pyautogui.scroll(-100)
        
        c = passw("pass")
        if c == 2:
            break   


