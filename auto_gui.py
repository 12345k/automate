import pyautogui
pyautogui.PAUSE=1
pyautogui.FAILSAFE=True
f= open("text.txt","r")
text= f.readlines()
# text=text.split()
for i in range(len(text)):
      a = text[i].split("-")
      if(a[0]=="left click  "):
          cor=a[1].split(",")
          x=int(cor[0].replace("(",""))
          y=int(cor[1].replace(")",""))
          time = int(a[-1])
          pyautogui.click(x,y,time)
      else:
          time = int(a[-1])
          pyautogui.typewrite('notepad',interval=time)

        # print(a[0])


