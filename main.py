import pyautogui
import os
import glob
path = (os.path.dirname(os.path.abspath(__file__)))
path=path.capitalize()
path=(path.replace('\\', '\\\\'))
path=(path+"\\\\")
print (path)
c=0
def kar(img):
            a=0
            addval=((path)+str(img))
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

file = glob.glob("*.PNG")
while True:
        for i in file:
            kar(i)
        pyautogui.scroll(-100)