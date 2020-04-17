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
app.geometry('430x580')

titleLabel = tk.Label(text="商品説明くん", font=("Helvetica", 20))
titleLabel.place(x=130, y=10)

lasttitle="\n<tr>\n  <td width=\"154\" align=\"center\">広告文責"
lasttitles="【広告文責】"
lasthonbun=  "</td>\n  <td width=\"675\">\n  <br>株式会社エナジー<br>電話番号：0242-85-7380<br>登録販売者　山内和也<br>薬剤師　山内典子<br>\n  </td>\n  </tr>"
lasthonbuns="<br>株式会社エナジー<br>電話番号：0242-85-7380<br>登録販売者　山内和也<br>薬剤師　山内典子<br>"

T1=[]
T2=[]

pcdata = "<!DOCTYPE HTML>\n<style>\ntable {\n	border-collapse: collapse;\n}\ntd {\n	border: solid 1px;\n	padding: 0.5em;\n}\n</style>\n   <tbody>"
smaphodata=""

def makeSetsumei ():
    global pcdata
    global smaphodata

    app2=tk.Tk()
    app3=tk.Tk()

    for i in range(len(T1)):

        titletmp=T1[i].get('1.0', END)
        honbuntmp=T2[i].get('1.0', END)
        title=titletmp.replace("\n", "")
        honbun=honbuntmp.replace("\n", "<br>")

        if(titletmp!="\n" or honbuntmp!="\n"):
            pc="\n<tr>\n  <td width=\"154\" align=\"center\">"+ title +"</td>\n  <td width=\"675\">\n  <br>  "+ honbun + "\n  </td>\n  </tr>"
            pcdata=pcdata+pc
            smapho="【"+title+"】<br>"+ honbun + "\n"
            smaphodata=smaphodata+smapho
        
    pcdata=pcdata+lasttitle+lasthonbun
    smaphodata=smaphodata+lasttitles+lasthonbuns
    
    pcText=tk.Text(app2)
    pcText.pack()
    pcText.insert(tk.END, pcdata+"\n<tr>\n  <td width=\"154\" align=\"center\">"+ title +"</td>\n  <td width=\"675\">\n  <br>  "+ honbun + "\n  </td>\n  </tr>\n</tbody>")

    smaphoText=tk.Text(app3)
    smaphoText.pack()
    smaphoText.insert(tk.END, smaphodata)

    app2.mainloop()
    app3.mainloop()

for i in range (6):
    T1.append(tk.Text(app, height=2, width=6))
    T1[i].place(x=10, y=50*i+100)
    
    T2.append(tk.Text(app, height=2, width=45))
    T2[i].place(x=90, y=50*i+100)

def makeTextBox ():
    T1.append(tk.Text(app, height=2, width=6))
    T1[len(T1)-1].grid(column=0, row=len(T1)+4, padx=10, pady=10)
    
    T2.append(tk.Text(app, height=2, width=40))
    T2[len(T2)-1].grid(column=1, row=len(T2)+4, padx=10, pady=10)
    return

def deleteTextBox ():
    del T1[-1]
    
    del T2[-1]
    return
    
#plusButton = tk.Button(text="項目追加", command=makeTextBox)
#plusButton.grid(column=0, row=3, padx=10, pady=10, sticky=tk.W + tk.E)

#minusButton = tk.Button(text="項目削除", command=deleteTextBox)
#minusButton.grid(column=1, row=3, padx=10, pady=10, sticky=tk.W + tk.E)

createButton = tk.Button(text="  生成  ", font=(
    "Helvetica", 15), command=makeSetsumei)
createButton.place(x=170, y=500)

app.mainloop()