#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tkinter as tk


# In[2]:


import fnmatch


# In[3]:


import os


# In[4]:


from pygame import mixer


# In[5]:


canvas =  tk.Tk()


# In[6]:


canvas.title("******  DIVYANSHU Jamloki MUSIC PLAYER  *******")


# In[7]:


canvas.geometry("600x800")


# In[8]:


canvas.config(bg='black')


# In[9]:


rootpath = "C:\\Users\91807\Music"


# In[10]:


pattern = "*.mp3"


# In[11]:


mixer.init()


# In[12]:


def  select():
    label.config(text = listBox.get('anchor'))
    mixer.music.load(rootpath + "\\" + listBox.get("anchor") )
    mixer.music.play() 


# In[13]:


def stop():
    mixer.music.stop()
    listBox.select_clear('active')


# In[14]:


def play_next( ):
    next_song =  listBox.curselection()
    next_song= next_song[0] + 1
    next_song_name = listBox.get(next_song)
    label.config(text = next_song_name)
   

    mixer.music.load(rootpath +"\\"  +  next_song_name )
    mixer.music.play()
   
    listBox.select_clear(0,'end')
    listBox.activate(next_song)
    listBox.select_set(next_song)
    
    


# In[15]:


def play_prev( ):
    next_song =  listBox.curselection()
    next_song= next_song[0] - 1
    next_song_name = listBox.get(next_song)
    label.config(text = next_song_name )
    mixer.music.load(rootpath +"\\"  +  next_song_name )
    mixer.music.play()
    listBox.select_clear(0,'end')
    listBox.activate(next_song)
    listBox.select_set(next_song)
    


# In[16]:


def pause_song():
    if pauseButton["text"] == "Pause":
        mixer.music.pause()
        pauseButton["text"] == "Play"
            
    else:         
        mixer.music.unpause()
        pauseButton["text"]="Pause"
         
            


# In[17]:


listBox = tk.Listbox(canvas,fg = "cyan",bg='black',width=100,font = ("poppins",14))


# In[18]:


listBox.pack(padx = 15 ,pady=15)


# In[19]:


for root,dirs,files in os.walk(rootpath):
    for filename in fnmatch.filter(files,pattern):
        listBox.insert('end',filename)


# In[20]:


label = tk.Label(canvas, text = ' ', fg = "yellow",bg='black',font = ("poppins",14))
label.pack(pady=15)


# In[21]:


top = tk.Frame(canvas,bg = "black")
top.pack(padx =10,pady = 15 ,anchor = 'center')


# In[22]:


prevButton= tk.Button(canvas,text='PREV',command =  play_prev )
prevButton.pack(pady=15, in_= top, side ='left')


# In[23]:


stopButton= tk.Button(canvas,text='STOP',command = stop)
stopButton.pack(pady=15,in_ = top, side ='left')


# In[24]:


playButton= tk.Button(canvas,text='PLAY',command = select)
playButton.pack(pady=15,in_ = top, side ='left')


# In[25]:


pauseButton= tk.Button(canvas,text='PAUSE',command= pause_song)
pauseButton.pack(pady=15,in_ = top, side ='left')


# In[26]:


nextButton= tk.Button(canvas,text='NEXT',command =  play_next )
nextButton.pack(pady=15,in_ = top, side ='left')


# In[27]:


canvas.mainloop()


# In[ ]:





# In[ ]:





# In[ ]:




