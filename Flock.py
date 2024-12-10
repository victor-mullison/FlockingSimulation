import tkinter as tk
from tkinter import Scale, HORIZONTAL, VERTICAL
from Dependencies.Boid import Boid
from PIL import Image, ImageTk
import random

import sys
import os
def get_resource_path(relative_path):
    """
    Get the absolute path to a resource.
    Works for both development and PyInstaller's executable mode.
    """
    if hasattr(sys, '_MEIPASS'):
        # PyInstaller extracts files to a temporary directory in executable mode
        base_path = sys._MEIPASS
    else:
        # Development mode: use the current directory
        base_path = os.path.dirname(os.path.abspath(__file__))
    
    return os.path.join(base_path, relative_path)


root = tk.Tk()

root.title("Boids!")
root.geometry("500x600")

flock = []
image = Image.open(get_resource_path("Dependencies/Boid.png"))
image = image.resize((10,10))
sprite = ImageTk.PhotoImage(image) # Photoimage for png compatibility

for i in range(20):
    new_boid = Boid(root, image=sprite)
    flock.append(new_boid)
    new_boid.place(x=new_boid.position.x, y=new_boid.position.y)
    
    
def update_boids():
    for boid in flock:
        boid.set_multipliers(alignment.get(), cohesion.get(), separation.get())
        boid.edges()
        boid.flock(flock)
        boid.update()
        boid.place(x=boid.position.x, y=boid.position.y) # Update widget position
        
    root.after(10, update_boids)

def reset():
    alignment.set(40)
    cohesion.set(20)
    separation.set(30)
    for boid in flock:
        boid.position.x = random.randint(0,500)
        boid.position.y = random.randint(0,500)
    
alignment = Scale(root, from_=0, to=100, orient=HORIZONTAL)
alignment.set(40)
alignment.place(x=50,y=520)
al_label = tk.Label(root, text="Alignment")
al_label.place(x=70,y=560)

cohesion = Scale(root, from_=0, to=100, orient=HORIZONTAL)
cohesion.set(20)
cohesion.place(x=200,y=520)
co_label = tk.Label(root, text="Cohesion")
co_label.place(x=220,y=560)

separation = Scale(root, from_=0, to=100, orient=HORIZONTAL)
separation.set(30)
separation.place(x=350,y=520)
sep_label = tk.Label(root, text="Separation")
sep_label.place(x=360,y=560)

reset_button = tk.Button(root, text="@", command=reset)
reset_button.place(x=10,y=535)

update_boids()
root.mainloop()