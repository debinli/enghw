# -*- coding: cp936 -*-

import sys
import re
import random
import speech
import time
from Tkinter import *
import tkMessageBox

    
#speech.say("hello")
#speech.say("你好")

root = Tk()
root.title(u"英语听写")
root.geometry()
debug = 0

lb1 = Label(root, text=u'单词')
#lb1.pack(side=LEFT)
lb1.grid(row=1,column=0)
lb2 = Label(root, text=u'句子')
#lb2.pack(side=LEFT)
lb2.grid(row=2)
#lb3 = Label(root, text=u'随机')
#lb3.grid(row=3)


unit_name = ["one","two","three","four","five","six"]
cb_var1 = []
cb_var2 = []
for i in range(6):
    var = IntVar()
    cb_var1.append(var)
    cb_w  = Checkbutton(root,text=unit_name[i],variable=cb_var1[i])
    cb_w.grid(row=1,column=i+1) 
    #cb_var.append(var)
    #cb.pack()

for i in range(6):
    var = IntVar()
    cb_var2.append(var)
    cb_s  = Checkbutton(root,text=unit_name[i],variable=cb_var2[i])
    cb_s.grid(row=2,column=i+1) 

rand_sel = IntVar()
cb_r  = Checkbutton(root,text=u'随机',variable=rand_sel)
cb_r.grid(row=3,column=1)

def get_values():
    word_list =[]
    sentence_list =[]
    for i in range(6):
        word_list.append(cb_var1[i].get())
        sentence_list.append(cb_var2[i].get())
    random_sel= (rand_sel.get())

    print word_list
    print sentence_list
    print random_sel
    return word_list,sentence_list,random_sel



def open_file(filename):
    units = []
    words = []
    with open(filename, 'r') as f:
        for line in f:
            if re.match('unit',line.strip()):
                if len(units) > 1:
                    words.append(units)
                units = []
            else:
                units.append(line.strip())
                #print line.strip()
        words.append(units) # last one unit
    f.close()
    return words

def flat_words(words,word_sel):
    flat_words=[]
    idx = 0
    for i in words:
        # only selected word
        if word_sel[idx] == 1:
            #print "UNIT"+str(idx+1)+" SEL"
            for j in i:
                flat_words.append(j)
        else:
            #print "UNIT"+str(idx+1)+ " NOT SEL"
            pass
        idx = idx + 1
            
    return flat_words


def printhello():
    t.insert('1.0', "hello\n")

def listen(word_sentence,word_sel,rand_sel):
    
    words = []
    flats = []
    rand_sel  = 1

    if (word_sentence == "word"):
        word_file = "c:/Python27/words.txt"
        last_word = "最后一个单词"
    elif (word_sentence == "sentence"):
        word_file = "c:/Python27/sentences.txt"
        last_word = "最后一个句子"
    
    words = open_file(word_file)
    flats = flat_words(words,word_sel)

    if rand_sel == 1:
        random.shuffle(flats)
        
    for i in range(len(flats)):
        word = flats[i]
        print word
        if debug == 0 :
            if i ==(len(flats) - 1):
                speech.say(last_word)
            
            speech.say(word)
            tkMessageBox.showinfo("info",unicode(word,'cp936').encode('utf-8'))
        

    #tkMessageBox.showinfo("info",word)
    return



def listen_english():
    print u"==== 选项筛选 ===="
    word_sel,sentence_sel,rand_sel=get_values()
    #print sentence_sel
    t0 = time.time()
    print u"==== 单词听写 ===="
    listen("word",word_sel,rand_sel)
    print u"==== 句子听写 ===="
    listen("sentence",sentence_sel,rand_sel)
    print u"==== 听写结束 ===="
    t1 = time.time()
    delta = round((t1-t0)/60,2)
    print delta
    if debug == 0 :
        word="听写结束"
        speech.say(word)
        word='总共用时：'+str(delta)+'分钟'
        tkMessageBox.showinfo("info",unicode(word,'cp936').encode('utf-8'))
    
    return



#bt1= Button(root, text=u"听写开始", command = get_values)
bt1= Button(root, text=u"听写开始", command = listen_english)
#bt1.pack()
bt1.grid(row=4)

root.mainloop()



#if __name__ == "__main__":
#    words = open_file("c:/Python27/words.txt")
#    flat_words = flat_words(words)
    #print flat_words
#    for word in flat_words:
#        print word
        
