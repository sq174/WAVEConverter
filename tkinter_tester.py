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

#ファイル選択のフレーム
f = LabelFrame(tk, text = 'ファイル選択', labelanchor = NW)
#ファイル名を表示するエントリー
e = Entry(f, textvariable = filenames, borderwidth = 2)
e.pack(padx = 5, pady = 5, side = LEFT, expand = True, fill = X)
#ファイル選択ダイアログを開くボタン
a = Button(f, text = '...', width = 5, font = (20), 
           command = select_files)
a.pack(padx = 5, pady = 5, side = LEFT)
f.pack(padx = 10, pady = 10, expand = True, fill = X)
#ボタンを含むフレーム

tk.mainloop()




    
