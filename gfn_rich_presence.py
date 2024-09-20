import time
import sys
import json
import os
import pygetwindow as gw
import psutil  # To monitor GeForce Now process
from pypresence import Presence
from game_assets import game_map, asset_map  # Import game_map and asset_map

CONFIG_FILE = 'config.json'

def load_settings():
    """Load Client ID and other settings from the configuration file."""
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'r') as file:
            return json.load(file)
    else:
        print("Configuration file not found. Exiting.")
        sys.exit(1)

def initialize_presence(client_id):
    """Initialize and connect to Discord using the provided Client ID."""
    rpc = Presence(client_id)
    try:
        rpc.connect()
        return rpc
    except Exception as e:
        print(f"Failed to connect to Discord: {e}")
        sys.exit(1)

def detect_geforce_now():
    """Check if GeForce Now is running and identify the game from the window title."""
    for window in gw.getAllTitles():
        if "GeForce NOW" in window:
            game_title = window.split(" on GeForce NOW")[0]
            if game_title in game_map:  # Check if the detected game is in the game_map
                return game_title
    return None

def is_geforce_now_running():
    """Check if the GeForce Now process is running."""
    for proc in psutil.process_iter(['name']):
        if proc.info['name'] == "GeForceNOW.exe":
            return True
    return False

def update_discord_presence(rpc, game_title, start_time):
    """Update Discord Rich Presence with the current game info and time played."""
    if game_title:
        asset_name = asset_map.get(game_title, "default_asset")  # Use a default asset if the game is not in asset_map
        rpc.update(
            details=f"Playing {game_title}",
            state="In game",
            start=start_time,
            large_image=asset_name,
            large_text=game_title
        )
    else:
        rpc.clear()

def main():
    settings = load_settings()
    rpc = initialize_presence(settings['client_id'])
    current_game = None
    game_start_time = None

    while True:
        if is_geforce_now_running():
            game_title = detect_geforce_now()
            if game_title and game_title != current_game:
                current_game = game_title
                game_start_time = time.time()  # Reset timer for new game
                print(f"Detected game: {game_title}")
            update_discord_presence(rpc, current_game, game_start_time)
        else:
            print("GeForce Now is not running. Exiting.")
            rpc.clear()  # Clear Discord presence if GeForce Now is closed
            sys.exit(0)  # Exit the script when GeForce Now is closed
        time.sleep(10)  # Poll every 10 seconds

if __name__ == "__main__":
    main()
