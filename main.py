import tkinter as tk

root = tk.Tk()

root.geometry("1280x720")
label1 =tk.Label(root,text="初めてのアコム",font=("Arial",30))
label2 =tk.Label(root,text="初めてのアコム",font=("Arial",30))
label3 =tk.Label(root,text="初めてのアコム",font=("Arial",30))
label4 =tk.Label(root,text="初めてのアコム",font=("Arial",30))

label5 =tk.Label(root,text="初めてのアコム",font=("Arial",20))
label6 =tk.Label(root,text="初めてのアコム",font=("Arial",20))
label7 =tk.Label(root,text="初めてのアコム",font=("Arial",20))
label8 =tk.Label(root,text="初めてのアコム",font=("Arial",20))

label9 =tk.Label(root,text="初めてのアコム",font=("Arial",10))
label10 =tk.Label(root,text="初めてのアコム",font=("Arial",10))
label11 =tk.Label(root,text="初めてのアコム",font=("Arial",10))
label12 =tk.Label(root,text="初めてのアコム",font=("Arial",10))

def button_click():
    text = entry.get()
    print(text)
button = tk.Button(root,text="ボタンだよ",font=("Arial",30),command=button_click)
#commandはラムダ式でもかける、()はつけない
button.pack()


entry = tk.Entry(root,font=("Arial",10),)
entry.pack()


# label1.pack()
# label2.pack()

# label1.grid(row=0,column=0)
# label2.grid(row=0,column=1)
# label3.grid(row=2,column=2)
# label4.grid(row=0,column=3)


label1.place(x=20,y=20)
label2.place(x=90,y=90)
label3.place(x=150,y=150)
label4.place(x=210,y=210)

label5.place(x=260,y=260)
label6.place(x=370,y=370)
label7.place(x=480,y=480)
label8.place(x=590,y=590)

label9.place(x=700,y=700)
label10.place(x=901,y=901)
label11.place(x=1202,y=1202)
label12.place(x=2203,y=2203)






root.mainloop()





"""
pack
grid
place


Pack 縦並び
上から順番に
5 pack
4 pack
3 pack
2 pack
1 pack
パックした順に表示される

grid(row,colum) 横並び
ウィンドウの画面を、グリッド状に

    colum
    0,0 1,0 2,0 
row 0,1 1,1 2,1
    0,2 1,2 2,2

place(y,x)
厳密に自由度高く置くことができる





"""