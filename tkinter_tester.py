# -*- coding: utf-8 -*-

import tkinter
from tkinter import *

tk = tkinter.Tk()
tk.title('WAVEConverter')
filenames = StringVar()
filenames.set("")

def select_files():
    filenames.set(filedialog.askopenfilenames(filetypes = [('CUE Files', ('.cue'))],
                                              initialdir = 'D:/temp', 
                                              title = "ファイル選択"))

#LabelFrame:ファイル選択
f0 = LabelFrame(tk, text = 'ファイル選択', labelanchor = NW)
#Entry:ファイル名を表示
e = Entry(f0, textvariable = filenames, borderwidth = 2)
e.pack(padx = 5, pady = 5, side = LEFT, expand = True, fill = X)
#Button:ファイル選択ダイアログを開く
a = Button(f0, text = '...', width = 5, 
           command = select_files)
a.pack(padx = 5, pady = 5, side = LEFT)
f0.pack(padx = 10, pady = 10, expand = True, fill = X)

#Frame:ボタン含
f1 = Frame(tk)
#Button:変換開始
a = Button(f1, text = '変換', width = 5,
           command = select_files)
a.pack(padx = 10, side = LEFT, anchor = CENTER)
#Button:閉じる
a = Button(f1, text = '閉じる', width = 5,
           command = sys.exit)
a.pack(padx = 10, side = LEFT, anchor = CENTER)
f1.pack(padx = 10, pady = 10, anchor =  CENTER, expand = True, fill = Y)

tk.mainloop()




    
