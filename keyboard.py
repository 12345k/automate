import pyHook
import pythoncom
import sys

words=[]
pos=[]
time=[]
def left_down(event):
    print "left click"
    print event.Position
    print event.Time
    words.append("left click")
    pos.append(event.Position)
    time.append(event.Time)

    return True  # if return false, the event will not be passed on to other programs.
    # The cursor will appear freeze


def right_down(event):
    print "right click"
    print event.Position
    print event.Time
    words.append("right click")
    pos.append(event.Position)
    time.append(event.Time)
    return True


def middle_down(event):
    print "middle click"
    print event.Position
    print event.Time
    words.append("middle click")
    pos.append(event.Position)
    time.append(event.Time)
    return True


def OnKeyboardEvent(event):
    if (chr(event.Ascii) == "q"):

        f = open("text.txt", "w+")
        for i in range(len(words)):
            f.write("%s  - " % words[i])
            f.write("%s  - " % str(pos[i]))
            f.write("%d \n" % time[i])
        f.close()

        print "quit"
        sys.exit()
    else:
        print chr(event.Ascii)
        print event.Time
        words.append(chr(event.Ascii))
        pos.append("0")
        time.append(event.Time)
    return True


hm = pyHook.HookManager()

# hook mouse
hm.SubscribeMouseLeftDown(left_down)
hm.SubscribeMouseRightDown(right_down)
hm.SubscribeMouseMiddleDown(middle_down)
hm.HookMouse()

# hook keyboard
hm.KeyDown = OnKeyboardEvent  # watch for all keyboard events
hm.HookKeyboard()

pythoncom.PumpMessages()

hm.UnhookMouse()
hm.UnHookKeyboard()
