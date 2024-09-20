import tkinter as tk
from tkinter import filedialog, messagebox
import json
import os
import sys
import winshell

# File paths for config, batch, and icon
CONFIG_FILE = 'config.json'
BATCH_FILE = 'launch_gfn.bat'
ICON_PATH = os.path.join(os.path.dirname(__file__), 'ico', 'Geforce-Now-Logo.ico')  # Ensure this .ico file exists

# Function to save Client ID, create batch file, and generate a desktop shortcut
def save_and_generate_shortcut(client_id, gfn_path):
    """Saves the Client ID, creates the batch file, and generates the desktop shortcut."""
    if not client_id or not gfn_path:
        # Check: If Client ID or GeForce Now path is missing, show an error
        messagebox.showerror("Error", "Please enter the Discord Client ID and select GeForceNOW.exe.")
        return
    
    # Save Client ID and GeForce NOW path to the config file
    settings = {'client_id': client_id, 'gfn_path': gfn_path}
    with open(CONFIG_FILE, 'w') as file:
        json.dump(settings, file)
    
    # Create the batch file
    create_batch_file(gfn_path)
    
    # Create the desktop shortcut
    create_desktop_shortcut()
    
    # Success message and close the GUI
    messagebox.showinfo("Success", "Client ID saved and desktop shortcut created successfully.")
    root.destroy()  # Close the GUI after saving and creating the shortcut

# Function to create the batch file
def create_batch_file(gfn_path):
    """Creates the batch file that launches pythonw.exe with the Discord Rich Presence script."""
    # Get the path to pythonw.exe
    python_executable = os.path.join(sys.exec_prefix, 'pythonw.exe')
    # Path to the Rich Presence script
    script_path = os.path.join(os.path.dirname(__file__), 'gfn_rich_presence.py')
    
    # Create the batch file
    with open(BATCH_FILE, 'w') as file:
        file.write(f'@echo off\n')
        file.write(f'start "" "{python_executable}" "{script_path}"\n')
        file.write(f'start "" "{gfn_path}"\n')
    
    print("Batch file created successfully.")

# Function to create the desktop shortcut
def create_desktop_shortcut():
    """Creates a desktop shortcut for the batch file."""
    # Path for the desktop shortcut
    shortcut_path = os.path.join(winshell.desktop(), "GeForce NOW.lnk")
    # Path to the batch file
    batch_file_path = os.path.join(os.path.dirname(__file__), BATCH_FILE)
    
    try:
        # Create the shortcut using winshell
        with winshell.shortcut(shortcut_path) as shortcut:
            shortcut.path = batch_file_path
            shortcut.working_directory = os.path.dirname(batch_file_path)
            shortcut.icon_location = (ICON_PATH, 0)  # Assign the icon
            shortcut.description = "Launch GeForce NOW with Rich Presence"
        
        print("Desktop shortcut created successfully.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to create desktop shortcut: {e}")

# Function to open a file dialog to select GeForceNOW.exe
def browse_file(entry):
    """Opens a file dialog to select the GeForceNOW.exe file."""
    file_path = filedialog.askopenfilename(filetypes=[("Executable Files", "*.exe")])
    if file_path:
        # Insert the selected path into the entry field
        entry.delete(0, tk.END)
        entry.insert(0, file_path)

# Function to set up the GUI
def setup_gui():
    """Creates the GUI for entering the Discord Client ID and selecting GeForceNOW.exe."""
    global root
    root = tk.Tk()
    root.title("GeForce NOW Rich Presence Setup")

    # Field for Discord Client ID
    tk.Label(root, text="Discord Client ID:").grid(row=0, column=0, sticky="e")
    client_id_entry = tk.Entry(root, width=40)
    client_id_entry.grid(row=0, column=1, padx=5, pady=5)

    # Field for the GeForceNOW.exe path
    tk.Label(root, text="Path to GeForceNOW.exe:").grid(row=1, column=0, sticky="e")
    gfn_path_entry = tk.Entry(root, width=40)
    gfn_path_entry.grid(row=1, column=1, padx=5, pady=5)
    gfn_path_button = tk.Button(root, text="Browse...", command=lambda: browse_file(gfn_path_entry))
    gfn_path_button.grid(row=1, column=2, padx=5, pady=5)

    # Button to save and generate the shortcut
    save_button = tk.Button(root, text="Save and Generate Shortcut", command=lambda: save_and_generate_shortcut(client_id_entry.get(), gfn_path_entry.get()))
    save_button.grid(row=2, column=1, pady=15)

    root.mainloop()

# Run the GUI when setup.py is executed
if __name__ == "__main__":
    setup_gui()
