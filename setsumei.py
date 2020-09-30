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
app.geometry('600x800')

titleLabel = tk.Label(text="商品説明くん", font=("Helvetica", 20))
titleLabel.place(x=10, y=10)

T1=[]
T2=[]

bgcolor= "#ffffff"
color= "#000000"
def makeSetsumei ():
    
    app2=tk.Tk()
    app3=tk.Tk()

    pcdata="<table border=\"1\">\n<tbody>"
    smaphodata=""

    for i in range(len(T1)):

        titletmp=T1[i].get('1.0', END)
        honbuntmp=T2[i].get('1.0', END)

        bgcolor=bgbox.get('1.0', END)
        color=cobox.get('1.0', END)

        bgcolor=bgcolor.replace("\n", "")
        color=color.replace("\n", "")

        title=titletmp.replace("\n", "")
        honbun=honbuntmp.replace("\n", "<br>")

        if(titletmp!="\n" or honbuntmp!="\n"):
            pc="\n<tr>\n  <td width=\"116\" align=\"center\" bgcolor=\"" + bgcolor + "\"><font face=\"メイリオ\" color=\"" + color + "\">"+ title +"</font></td>\n  <td width=\"308\">\n  <br>	"+ honbun + "<br>\n  </td>\n  </tr>\n"
            pcdata=pcdata+pc
            smapho="【"+title+"】<br>"+ honbun + "\n"
            smaphodata=smaphodata+smapho
    
    pcText=tk.Text(app2)
    pcText.pack()
    pcText.insert(tk.END, pcdata+"</tbody>\n</table>")

    smaphoText=tk.Text(app3)
    smaphoText.pack()
    smaphoText.insert(tk.END, smaphodata)

    app2.mainloop()
    app3.mainloop()

coLabel = tk.Label(text="背景　　　　　文字", font=("Helvetica", 10))
coLabel.place(x=250, y=10)

bgbox=tk.Text(app, height=2, width=7)
bgbox.place(x=250, y=40)
cobox=tk.Text(app, height=2, width=7)
cobox.place(x=350, y=40)


for i in range (6):
    T1.append(tk.Text(app, height=4, width=6))
    T1[i].place(x=10, y=100*i+100)
    
    T2.append(tk.Text(app, height=4, width=70))
    T2[i].place(x=90, y=100*i+100)

for i in range (6, 12):
    T1.append(tk.Text(app, height=4, width=6))
    T1[i].place(x=620, y=100*(i-6)+100)
    
    T2.append(tk.Text(app, height=4, width=70))
    T2[i].place(x=710, y=100*(i-6)+100)

for i in range (12, 18):
    T1.append(tk.Text(app, height=4, width=6))
    T1[i].place(x=1230, y=100*(i-12)+100)
    
    T2.append(tk.Text(app, height=4, width=70))
    T2[i].place(x=1320, y=100*(i-12)+100)

createButton = tk.Button(text="  生成  ", font=("Helvetica", 15), command=makeSetsumei)
createButton.place(x=250, y=700)

app.mainloop()