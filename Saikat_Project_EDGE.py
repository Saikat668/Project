import tkinter as tk
from datetime import datetime

def update_time():
    now = datetime.now()
    
    # Format time (HH:MM:SS)
    current_time = now.strftime("%H:%M:%S")
    time_label.config(text=current_time)
    
    # Format date (Month Day, Year)
    current_date = now.strftime("%B %d, %Y")
    date_label.config(text=current_date)
    
    # Format day (e.g., Saturday)
    current_day = now.strftime("%A")
    day_label.config(text=current_day)
    
    # Update every 1 second (1000ms)
    root.after(1000, update_time)

# Create the main window
root = tk.Tk()
root.title("Smart Watch")
root.geometry("300x200")
root.configure(bg="black")

# Time Label (Big Font)
time_label = tk.Label(
    root, 
    font=("Arial", 40), 
    fg="cyan", 
    bg="black"
)
time_label.pack(pady=10)

# Date Label (Medium Font)
date_label = tk.Label(
    root, 
    font=("Arial", 20), 
    fg="white", 
    bg="black"
)
date_label.pack()

# Day Label (Medium Font)
day_label = tk.Label(
    root, 
    font=("Arial", 20), 
    fg="white", 
    bg="black"
)
day_label.pack()

# Start the clock
update_time()

# Run the app
root.mainloop()