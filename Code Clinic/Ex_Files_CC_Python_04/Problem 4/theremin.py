#!/usr/bin/python3
# theremin.py by Barron Stone
# This is an exercise file from Python Code Clinic on lynda.com

import numpy as np
from tkinter import *
from tkinter import ttk
from pygame import sndarray, mixer

__version__ = '0.4.3'

class Theremin:
    
    def __init__(self, master):
        self.prev = None # previous mouse location (for drawing)
        self.sound = None # sound array to play
        self.sound_on = False # sound state flag
    
        master.attributes('-fullscreen', True)
        
        self.canvas = Canvas(master, background = 'black')
        self.canvas.pack(fill = BOTH, expand = True)
        self.canvas.create_text(master.winfo_screenwidth()//2, master.winfo_screenheight(), anchor = 's',
                                text = "Press 'Esc' to Quit.", font = ('Helvetica', 32, 'bold'), fill = 'white')
        
        master.bind('<Motion>', self.mouse_move)
        master.bind('<ButtonPress>', self.mouse_down)
        master.bind('<ButtonRelease>', self.mouse_up)
        master.bind('<Escape>', lambda e: master.destroy())
            
        mixer.init(22050, -16, 1) # 22050 Hz, 16-bit, Mono
                
    def mouse_move(self, event):        
        if self.sound_on:
            new_sound = sndarray.make_sound(self.sine_wave(self.calc_freq(event.y)))
            new_sound.set_volume(self.calc_volume(event.x))
            new_sound.play(-1)
            self.sound.stop()
            self.sound = new_sound
     
        R = int(255 * event.x / self.canvas.winfo_width() * (self.canvas.winfo_height() - (event.y + 1)) / self.canvas.winfo_height()) 
        B = int(255 * event.x / self.canvas.winfo_width() * (event.y + 1) / self.canvas.winfo_height())         
        self.canvas.config(background = '#{:02x}50{:02x}'.format(R, B)) # set green to 0x50 for "pizzazz"
               
        if self.prev: # draw line if mouse is down
            self.canvas.create_line(self.prev.x, self.prev.y,
                                    event.x, event.y, width = 10,
                                    fill = '#{:02x}88{:02x}'.format(R, B))
            self.prev = event
        
    def mouse_down(self, event):
        self.prev = event       
        self.sound_on = True
        self.sound = sndarray.make_sound(self.sine_wave(self.calc_freq(event.y)))
        self.sound.set_volume(self.calc_volume(event.x))
        self.sound.play(-1)      
        
    def mouse_up(self, event):        
        self.prev = None
        self.canvas.delete('all')
        self.canvas.create_text(self.canvas.winfo_width()//2, self.canvas.winfo_height(), anchor = 's',
                                text = "Press 'Esc' to Quit.", font = ('Helvetica', 32, 'bold'), fill = 'white')
        self.sound_on = False
        self.sound.stop()
        
    def calc_freq(self, y_pos): # calculate frequency of "piano key" at y_pos     
        pkey = 88 * (self.canvas.winfo_height() - (y_pos + 1)) / self.canvas.winfo_height() + 1
        return 440 * 2**((pkey - 49)/12) # 440Hz is key #49 on a piano
    
    def calc_volume(self, x_pos):
        return x_pos / self.canvas.winfo_width()

    def sine_wave(self, frequency = 440.0, samplerate = 22050):
        samples = samplerate / frequency
        return (32767 * np.sin(np.arange(int(samples)) * (2 * np.pi) / samples)).astype(np.int16)
    
def main():
    root = Tk()
    gui = Theremin(root)
    root.mainloop()
    
if __name__ == "__main__": main()