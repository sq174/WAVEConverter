# -*- coding: utf-8 -*-

import tkinter
from tkinter import *
import logging
import datetime
import time
import re
import sys, os.path

d = datetime.datetime.today()
LOG_FILENAME = d.strftime("log/%Y%m%d.log")
tk = tkinter.Tk()
tk.title('WAVEConverter')

entry_buffer = StringVar()
entry_buffer.set("")

def select_files():
    entry_buffer.set(filedialog.askopenfilenames(filetypes = [('CUE Files', ('.cue'))],
                                              initialdir = 'D:/temp', 
                                              title = "ファイル選択"))
def convert_files():
    logging.basicConfig(filename = LOG_FILENAME,
                        level = logging.DEBUG)
    logger = logging.getLogger('Logger')
    logger.debug('begin convert')
    ##########################ここから#############################
    filenames = entry_buffer.get().strip('{}').split('} {')
    
    
    
#LabelFrame:ファイル選択
f0 = LabelFrame(tk, text = 'ファイル選択', labelanchor = NW)
#Entry:ファイル名を表示
e = Entry(f0, textvariable = entry_buffer, borderwidth = 2)
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
           command = convert_files)
a.pack(padx = 10, side = LEFT, anchor = CENTER)
#Button:閉じる
"""
a = Button(f1, text = '閉じる', width = 5,
           command = lambda : sys.exit())
a.pack(padx = 10, side = LEFT, anchor = CENTER)
"""
f1.pack(padx = 10, pady = 10, anchor =  CENTER, expand = True, fill = Y)

tk.mainloop()





    
