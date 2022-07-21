import requests
import os
import time
from tkinter import *

versiuneCurenta = 10
linkGit = 'https://raw.githubusercontent.com/turb0x/InterventioN/main/ver.json'
reqGit = requests.get(linkGit).json()
versiuneGit = int(reqGit["versions"]["launcher"])


f = open("C:/ProgramData/InterventioN/hwid.txt", "r")
hwid=f.read()
r = requests.get("https://raw.githubusercontent.com/turb0x/InterventioN/main/hwid.txt")


def cumpara():
    os.system("start http://intervention.atwebpages.com/")
    os.system("start https://steamcommunity.com/id/turb0golf/")
    sys.exit()


if hwid in r.text:
    time.sleep(0)
else:
    hwidgui = Tk()
    hwidgui.geometry("504x204")
    hwidgui.title("InterventioN Membership")
    hwidgui.iconbitmap("C:/ProgramData/InterventioN/icon.ico")
    hwidgui.resizable(False, False)
    positionRight = int(hwidgui.winfo_screenwidth() / 2.7)
    positionDown = int(hwidgui.winfo_screenheight() / 2.7)
    hwidgui.geometry("+{}+{}".format(positionRight, positionDown))
    bghwid = PhotoImage(file="C:/ProgramData/InterventioN/hwidclean.png")
    backgr = Label(hwidgui, image=bghwid)
    backgr.place(x=0, y=0)
    buthwid = PhotoImage(file="C:/ProgramData/InterventioN/butonhwid.png")
    play = Button(hwidgui, image=buthwid, borderwidth=0, highlightthickness=0, command=cumpara)
    play.place(x=138, y=137)
    hardwareid = Label(hwidgui, text=hwid, compound='center', fg='white', bg='#141414')
    hardwareid.place(x=132, y=117)
    hwidgui.mainloop()
    sys.exit()


def joaca():
    r = requests.get('https://www.dropbox.com/s/1wt0haakbbuwyi5/intvfinal.exe?dl=1', allow_redirects=True)
    open('C:/ProgramData/intv.exe', 'wb').write(r.content)
    os.startfile('C:/ProgramData/intv.exe')
    sys.exit()


def changelog():
    ws = Tk()
    ws.title('Changelog')
    ws.geometry('400x500')
    ws.config(bg='#141414')
    ws.iconbitmap("C:/ProgramData/InterventioN/icon.ico")
    ws.resizable(False, False)
    message = '''
------------InterventioN Launcher------------

17.10.2021 - v1.0
[ADDED] Gui
[ADDED] Check for updates
[REMOVED] Terminal interface
[REMOVED] Beta releases
[REMOVED] Mods
[REMOVED] Credits
Note: all features from mods and beta are now included in intv-final 


11.09.2021 - v0.4
[ADDED] HWID login
[REMOVED] User login


26.08.2021 - v0.3
[MODS] Radar hack
[MODS] Money hack
[MODS] Wallhack
[MODS] Quick CTRL


28.05.2021 - v0.2
[ADDED] Beta cheat releases
[ADDED] Mod menu
[ADDED] Credits menu
[MODS] Skin changer


10.05.2021 - v0.1.1
Note: Optimizations


12.01.2021 - v0.1
Note: Initial release
    '''

    frame = Frame(ws)
    text_box = Text(
        frame,
        height=30,
        width=45,
        wrap='word'
    )
    text_box.insert('end', message)
    text_box.pack(side=LEFT, expand=True)
    sb = Scrollbar(frame)
    sb.pack(side=RIGHT, fill=BOTH)
    text_box.config(yscrollcommand=sb.set)
    sb.config(command=text_box.yview)
    frame.pack(expand=True)
    frame.place(x=10, y=10, height=480, width=380)
    ws.mainloop()


def updater():
    r = requests.get('https://www.dropbox.com/s/dxdwn76z9oahu85/intervention-updater.exe?dl=1', allow_redirects=True)
    open('C:/ProgramData/InterventioN/intervention-updater.exe', 'wb').write(r.content)
    os.startfile('C:/ProgramData/InterventioN/intervention-updater.exe')
    sys.exit()


def settings():
    sett = Tk()
    sett.title('Settings')
    sett.geometry('300x85')
    sett.iconbitmap("C:/ProgramData/InterventioN/icon.ico")
    sett.resizable(False, False)
    sett.config(bg='#141414')
    username = Label(sett, text="Username: "+os.getlogin(), compound='center', fg='white', bg='#141414')
    username.place(x=0, y=0)
    hardwareid1 = Label(sett, text="HWID: "+hwid, compound='center', fg='white', bg='#141414')
    hardwareid1.place(x=0, y=20)
    status1 = Label(sett, text="Status: ", compound='center', fg='white', bg='#141414')
    status1.place(x=0, y=40)
    if int(versiuneGit) == versiuneCurenta:
        status2 = Label(sett, text="Updated", compound='center', fg='green', bg='#141414')
        status2.place(x=40, y=40)
    else:
        status2 = Label(sett, text="Outdated", compound='center', fg='red', bg='#141414')
        status2.place(x=40, y=40)
        update = Button(sett, text="Update", borderwidth=0, highlightthickness=0, command=updater)
        update.place(x=4, y=60)
    sett.mainloop()



root = Tk()
root.geometry("404x604")
root.title("InterventioN Launcher")
root.iconbitmap("C:/ProgramData/InterventioN/icon.ico")
root.resizable(False, False)
bg = PhotoImage(file="C:/ProgramData/InterventioN/backclean.png")
backgr = Label(root, image=bg)
backgr.place(x=0, y=0)
hardwareid = Label(root, text=hwid, compound='center', fg='white', bg='#141414')
hardwareid.place(x=85, y=580)


playbut = PhotoImage(file="C:/ProgramData/InterventioN/play.png")
play = Button(root, image=playbut, borderwidth=0, highlightthickness=0, command=joaca)
play.place(x=158, y=505)
changelogbut = PhotoImage(file="C:/ProgramData/InterventioN/changelog.png")
changelog = Button(root, image=changelogbut, borderwidth=0, highlightthickness=0, command=changelog)
changelog.place(x=14, y=573)
settingsbut = PhotoImage(file="C:/ProgramData/InterventioN/settings.png")
changelog = Button(root, image=settingsbut, borderwidth=0, highlightthickness=0, command=settings)
changelog.place(x=367, y=573)
root.mainloop()
