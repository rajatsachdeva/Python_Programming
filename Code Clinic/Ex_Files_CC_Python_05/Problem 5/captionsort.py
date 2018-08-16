#!/usr/bin/python3
# captionsort.py by Barron Stone
# This is an exercise file from Python Code Clinic on lynda.com

import os
import shutil
import subprocess
from tkinter import *
from tkinter import ttk, filedialog, messagebox

__version__ = '0.2.1'

class CaptionSort:
    
    def __init__(self, master):        
        self.master = master      
        self.master.title('Sort Images by Exif Caption')
        self.master.resizable(False, False)
        
        self.main_frame = ttk.Frame(self.master)
        self.main_frame.pack(padx = 5, pady = 5)
        
        ttk.Label(self.main_frame, text = 'Source Directory:').grid(row = 0, column = 0, sticky = 'w')        
        self.src_entry = ttk.Entry(self.main_frame, width = 54)
        self.src_entry.grid(row = 1, column = 0, sticky = 'e')
        self.src_entry.insert(0, '.\\images')            
        ttk.Button(self.main_frame, text = 'Browse...',
                   command = self.browse_src_callback).grid(row = 1, column = 1, sticky = 'w')
        
        ttk.Label(self.main_frame, text = 'Destination Directory:').grid(row = 2, column = 0, sticky = 'w')   
        self.dest_entry = ttk.Entry(self.main_frame, width = 54)
        self.dest_entry.grid(row = 3, column = 0, sticky = 'e')
        self.dest_entry.insert(0, '.\\sorted')        
        ttk.Button(self.main_frame, text = 'Browse...',
                   command = self.browse_dest_callback).grid(row = 3, column = 1, sticky = 'w')
        
        self.copy_var = IntVar()
        self.copy_var.set(1)
        ttk.Checkbutton(self.main_frame, text = 'Copy Files',
                        variable = self.copy_var).grid(row = 4, column = 0, columnspan = 2)
              
        ttk.Button(self.main_frame, text = 'Sort Images',
                   command = self.sort_callback).grid(row = 5, column = 0, columnspan = 2)
    
    def browse_src_callback(self):
        path = filedialog.askdirectory(initialdir = self.src_entry.get())
        self.src_entry.delete(0, END)
        self.src_entry.insert(0, path)
        
    def browse_dest_callback(self):
        path = filedialog.askdirectory(initialdir = self.dest_entry.get())
        self.dest_entry.delete(0, END)
        self.dest_entry.insert(0, path)
    
    def sort_callback(self):                  
        image_paths = [] # list of all image files in directory
        for dirpath, dirnames, filenames in os.walk(self.src_entry.get()):          
            for file in filenames:
                if file.endswith(('.jpg', '.png')):
                    image_paths.append(os.path.join(dirpath, file))
 
        sort_dirs = {} # create dictionary of empty lists for keys A-Z
        for key in range(ord('A'), ord('Z')+1):
            sort_dirs[chr(key)] = []

        for path in image_paths:            
            if path.endswith('.jpg'):
                tag = '-Caption-Abstract'
            elif path.endswith('.png'):
                tag = '-Description'
            try: # use ExifTool from http://www.sno.phy.queensu.ca/~phil/exiftool/
                output = subprocess.check_output(['.\\exiftool.exe', tag, path])
                caption = output.decode(encoding = 'utf_8')[34:].rstrip()
            except:
                print('Error getting Exif data for ' + path)
            else:
                print('Caption found for {} - {}'.format(path, caption))
                if caption:
                    try: # will fail if caption does not begin with a letter
                        sort_dirs[caption[0].upper()].append(path)
                    except:
                        print('Error sorting {} - Caption begins with {}'.format(path, caption[0]))

        sorted_count = 0
        for key in sort_dirs.keys():
            if sort_dirs[key]:
                key_path = os.path.join(self.dest_entry.get(), key)
                if not os.path.exists(key_path):
                    try:
                        os.makedirs(key_path)
                    except os.error as e:
                        print(str(e))
                for file in sort_dirs[key]:
                    if self.copy_var.get():
                        try:                  
                            shutil.copy(file, os.path.join(key_path, file.split('\\')[-1]))                            
                        except IOError as e: # occurs is destination is not writable
                            print(str(e))
                        else:
                            print('Copied {} to {}'.format(file, key_path))
                            sorted_count += 1
                    else:
                        try:                  
                            shutil.move(file, os.path.join(key_path, file.split('\\')[-1]))
                        except IOError as e: # occurs is destination is not writable
                            print(str(e))
                        else:
                            print('Moved {} to {}'.format(file, key_path))
                            sorted_count += 1
        
        messagebox.showinfo(title = 'Image Sort Completed',
                            message = 'Done!\nSorted {} files'.format(sorted_count))     

def main():    
    root = Tk()
    gui = CaptionSort(root)
    root.mainloop()

if __name__ == "__main__": main()