from tkinter import *
from tkinter.messagebox import *
import platform,os
root = Tk()
curstate = False
def processkey(event):
    global inp, output
    if event.keysym == 'BackSpace':
        inp = inp[0:len(inp)-1]
    elif event.keysym != 'Return':
        inp += event.char
    elif event.char == '':
        inp = inp[0:len(inp)-2]
    elif event.keysym == 'Return':
        output+='\n'+os.getcwd()+'>'+inp+'\n'
        if not inp[0:2] == 'cd' and not inp[0:3] == 'win':
            out = os.popen(inp)
            output+=out.read()
        elif inp[0:3] == 'win':
            output += 'Returning to windows. If you wish to disable DOS mode,\nremove program from startup'
            root.after(7000,root.destroy)
        else:
            os.chdir(inp[3:])
        inp=''
if platform.system() == 'Linux' or platform.system() == 'Darwin':
    showerror("Warning", 'Dos wrapper for windows was NOT made for linux or Mac os, please run it on an windows computer.')
root.title(f'Python')
h = root.winfo_screenheight()
w = root.winfo_screenwidth()
root.geometry(f'{w}x{h}+0+0')
root.overrideredirect(True)
output = 'Starting MS-DOS...\n\nHIMEM is testing extended memory...done.\n\nC:\\>C:\\Windows\\SMARTDRV.EXE /X'
C = Canvas(bg='#000000', highlightthickness=0)
C.pack(fill=BOTH, expand=True)
inp = ''
def update():
    global output
    C.delete('all')
    if curstate:
        C.create_text(1,1,fill="white",font=("@GulimChe", 14, "bold"),
            text=output.replace('\\', '/')+'\n'+os.getcwd().replace('\\', '/')+'>'+inp.replace('\\', '/')+'_', anchor="nw", tags="out")
    else:
        C.create_text(1,1,fill="white",font=("@GulimChe", 14, "bold"),
            text=output.replace('\\', '/')+'\n'+os.getcwd().replace('\\', '/')+'>'+inp.replace('\\', '/'), anchor="nw", tags="out")
    if C.bbox('out')[3] > C.winfo_height():
        output = '\n'.join(output.splitlines()[1:])
    root.after(100,update)
def updcur():
    global curstate
    curstate = not curstate
    root.after(300,updcur)
def fakeboot1():
    C.create_text(1,1,fill="white",font=("@GulimChe", 14, "bold"), text="Starting MS-DOS...\n\nHIMEM is testing extended memory...", anchor="nw")
    root.after(1500,fakeboot2)
def fakeboot2():
    C.delete('all')
    C.create_text(1,1,fill="white",font=("@GulimChe", 14, "bold"), text="Starting MS-DOS...\n\nHIMEM is testing extended memory...done.", anchor="nw")
    root.after(1500,fakeboot3)
def fakeboot3():
    C.delete('all')
    C.create_text(1,1,fill="white",font=("@GulimChe", 14, "bold"), text="Starting MS-DOS...\n\nHIMEM is testing extended memory...done.\n\nC:/>C:/Windows/SMARTDRV.EXE /X", anchor="nw")
    root.after(1500,update)
C.create_text(1,1,fill="white",font=("@GulimChe", 14, "bold"), text="Starting MS-DOS...", anchor="nw")
root.after(1500,fakeboot1)
updcur()
root.bind('<Key>', processkey)
root.mainloop()
