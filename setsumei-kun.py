import tkinter as tk
import tkinter.filedialog
import tkinter.messagebox
import os

from tkinter import BOTH, END, LEFT
from tkinter import ttk, DISABLED
from os.path import expanduser

app = tk.Tk()
app.resizable(True, True)

app.title("商品説明くん")
app.geometry('430x500')

TitleLabel = tk.Label(text="商品説明くん", font=("Helvetica", 20))
TitleLabel.place(x=10, y=10)

T1=[]
T2=[]

scrollbar=[]

def makeSetsumei ():
    
    app2=tk.Tk()
    app2.title("PC用説明文")
    app3=tk.Tk()
    app3.title("SP用説明文")

    PCData="<table border=\"1\">\n  <tbody>"
    SPData=""

    for i in range(len(T1)):

        TitleTmp=T1[i].get('1.0', END)
        MainTextTmp=T2[i].get('1.0', END)

        bgcolor=bgbox.get('1.0', END)
        color=cobox.get('1.0', END)

        bgcolor=bgcolor.replace("\n", "")
        color=color.replace("\n", "")

        Title=TitleTmp.replace("\n", "")
        MainText=MainTextTmp.replace("\n", "<br>")

        if(TitleTmp!="\n" or MainTextTmp!="\n"):
            PC="\n<tr>\n    <td width=\"116\" align=\"center\" bgcolor=\"" + bgcolor \
            + "\"><font face=\"メイリオ\" color=\"" + color + "\">"+ Title \
            + "</font></td>\n      <td width=\"358\">\n        <br>	"+ MainText \
            + "<br>\n      </td>\n    </tr>\n"

            PCData=PCData+PC
            SP="【"+Title+"】"+ MainText + "\n"
            SPData=SPData+SP
    
    PCText=tk.Text(app2)
    PCText.pack()
    PCText.insert(tk.END, PCData+"</tbody>\n</table>")

    SPText=tk.Text(app3)
    SPText.pack()
    SPText.insert(tk.END, SPData)

    app2.mainloop()
    app3.mainloop()

coLabel = tk.Label(text="背景色　　　　文字色", font=("Helvetica", 10))
coLabel.place(x=250, y=10)

bgbox=tk.Text(app, height=1, width=7)
bgbox.place(x=250, y=40)
cobox=tk.Text(app, height=1, width=7)
cobox.place(x=350, y=40)

bgbox.insert(END, "#0000ff")
cobox.insert(END, "#ffffff")

for i in range (7):
    T1.append(tk.Text(app, height=2, width=6))
    T1[i].place(x=10, y=50*i+100)
    
    T2.append(tk.Text(app, height=2, width=45))
    T2[i].place(x=90, y=50*i+100)

for i in range (7, 14):
    T1.append(tk.Text(app, height=2, width=6))
    T1[i].place(x=500, y=50*(i-7)+100)
    
    T2.append(tk.Text(app, height=2, width=45))
    T2[i].place(x=590, y=50*(i-7)+100)

T1[i].insert(END, "広告文責")
T2[i].insert(END, "株式会社エナジー 0242-85-7380\n登録販売者　山内和也")

createButton = tk.Button(text="  生成  ", font=("Helvetica", 15), command=makeSetsumei)
createButton.place(x=180, y=450)

app.mainloop()