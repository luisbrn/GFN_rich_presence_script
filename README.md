# GeForce Now Discord Rich Presence Script

This script adds Discord Rich Presence for games played on GeForce Now desktop app. It detects the game you're playing and automatically updates your Discord status with the game title, time played, and a relevant game icon. The script also includes automatic time tracking and clears your status when no game is detected or when GeForce Now is closed.

## Features
- **Discord Rich Presence Integration**: Automatically updates your Discord status when playing games on GeForce Now.
- **Game Detection**: Identifies games from Steam, Xbox, and Epic Games running on GeForce Now by window title.
- **Time Tracking**: Uses Discord's built-in feature to track how long you've been playing a game.
- **Auto Clear**: Automatically clears your Discord status when GeForce Now is closed or no supported game is detected.

## Installation Instructions

### 1. Clone the Repository
First, clone this repository to your local machine:
```bash
git clone https://github.com/yourusername/geforce-now-discord-rich-presence.git
```
### 2. Install the Required Dependencies
Navigate to the project folder and install the required Python packages:
```bash
pip install -r requirements.txt
```
### 3. Setting Up Discord Client ID
1.Go to the Discord Developer Portal.
2.Create a new application.
3.Copy the Client ID and paste it into the DISCORD_CLIENT_ID variable in main.py.

### 4. Modifying Game Images
The script uses specific image assets for each game in Discord Rich Presence. To customize or add your own images:
1.Go to the images folder in the root directory of the script.
2.Upload your images to the Discord Developer Portal under Rich Presence > Art Assets.
3.Ensure the image names you upload in Discord match the names used in the asset_map located in the game_assets.py file.
Example of asset_map in game_assets.py:
```python
asset_map = {
    "Counter-Strike: Global Offensive": "csgo_image",
    "Dota 2": "dota2_image",
    "Fortnite": "fortnite_image",
    # Add more games here
}
```
If you upload a new image named my_custom_game_image, add it to asset_map like this:
```python
"Custom Game": "my_custom_game_image"
```
### 5. Adding New Games to game_assets.py
To add new games that the script can detect, you need to modify the game_assets.py file.

1.Open the game_assets.py file.
2.Add the new game to the game_map and asset_map.

Example:
```python
game_map = {
    "Custom Game": "custom_game_process_name",  # Add the process/window name of the new game
    # Existing games...
}

asset_map = {
    "Custom Game": "custom_game_image",  # Add the image name uploaded in the Discord Developer Portal
    # Existing games...
}
```
Make sure the process/window name for the game (as shown in Task Manager) matches the entry in the game_map.

## Running the Script at Windows Startup
To run the script automatically when Windows starts, follow these steps:

### Step 1: Create a Batch File
1.Open Notepad and paste the following code:
```batch
@echo off
cd /d "C:\path\to\your\script"
start pythonw main.py
exit
```
Replace C:\path\to\your\script with the path where your main.py file is located.
2.Save the file as start_geforce_rich_presence.bat.

###Step 2: Add the Batch File to Windows Startup
1.Press Win + R, type shell:startup, and press Enter. This will open the Windows Startup folder.
2.Copy the start_geforce_rich_presence.bat file you created and paste it into the Startup folder.
Now, every time Windows starts, this batch file will run the script automatically in the background.

### License

This project is licensed under the MIT License. See the LICENSE file for more details.


