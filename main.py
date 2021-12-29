from yt_stats import YTstats
from tqdm import tqdm
import config as config
import requests
import json
import tkinter as tk
from tkinter import font, Button
import time

#"C5MGI-HPSnw"

def showViewers(videoid):
    req = "https://www.googleapis.com/youtube/v3/videos?id="+videoid+"&key="+config.API_KEY+"&part=liveStreamingDetails"
    response = requests.get(req)
    data = response.json()
    json_str = json.dumps(data)
    resp = json.loads(json_str)
    viewers = 0
    for keys, values in resp.items():
        if keys == "items":
            for word in values:
                for char, vals in word.items():
                    if char ==  "liveStreamingDetails":
                        for i, j in vals.items():
                            if i == "concurrentViewers":
                                viewers = str(j)
                                print(viewers)                           
                        return viewers
class Viewers(tk.Tk):
    """
    Frame object holdig all pages
    Controller of pages: fonts 
    """
    def __init__(self):
        # Shared title font
        super().__init__()
        self.textfont = font.Font(family = 'Gadugi', size=25)
        self.title("ViewCount")
        self.configure(bg="#F0F0F0", pady=10)
        self.startup()
        self.vids = []
    
    def startup(self):
        self.centre_window()
        self.start_label = tk.Label(self, text="Enter video id: ", font=self.textfont, bg="#F0F0F0", fg="#af1a40", highlightcolor="#0e6556")
        self.start_label.pack()
        self.entry_id = tk.Entry(self, font=self.textfont, bg="#F0F0F0", fg="#af1a40", highlightcolor="#0e6556")
        self.entry_id.pack()
        self.submitBut = Button(self, text="Submit", width=10, command=lambda : self.display_homepage())
        self.submitBut.pack()
        
    def display_homepage(self):
        self.vids.append(self.entry_id.get())
        self.start_label.destroy()
        self.entry_id.destroy()
        self.submitBut.destroy()
        self.views_label = tk.Label(self, font=self.textfont, bg="#F0F0F0", fg="#af1a40", highlightcolor="#0e6556")
        self.views_label.pack()
        self.corner_window()
        self.views_update()
    
    def views_update(self):
        videoid = self.vids[0]
        displayText = showViewers(videoid) 
        self.views_label.config(text = str(displayText)) # update the display
        self.after(1000, self.views_update)
    
    def corner_window(self, width=100, height=80):
        x = 0
        y = 0
        self.geometry('%dx%d+%d+%d' % (width, height, x, y))
        
    def centre_window(self, width=400, height=300):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = int((screen_width/2) - (width/2))
        y = int((screen_height/2) - (height/2))
        self.geometry('%dx%d+%d+%d' % (width, height, x, y))
    
    
if __name__ == "__main__":
    app = Viewers()
    app.mainloop()