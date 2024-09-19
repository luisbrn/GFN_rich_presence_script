import time
import pygetwindow as gw
import psutil  # To monitor GeForce Now process
from pypresence import Presence
from game_assets import game_map, asset_map  # Importing game and asset maps

# Configuration - Replace with your actual Discord Client ID
DISCORD_CLIENT_ID = 'YOUR_DISCORD_CLIENT_ID'

# Initialize Discord Presence
rpc = Presence(DISCORD_CLIENT_ID)
rpc.connect()

# Fallback asset for games not found in the asset map
fallback_asset = "default_fallback_image"

# Configurable option for Minimal Mode (set to False for full details, True for minimal)
show_detailed_presence = False

def update_discord_presence(game_title, start_time):
    """Update Discord Rich Presence with the current game info and Discord's built-in elapsed time."""
    if game_title:
        asset_name = asset_map.get(game_title, fallback_asset)
        if show_detailed_presence:
            rpc.update(
                state="Playing",
                details=game_title,
                large_image=asset_name,
                large_text=game_title,
                start=start_time  # Use Discord's built-in time tracking
            )
        else:
            rpc.update(
                details=game_title,
                large_image=asset_name,
                large_text=game_title,
                start=start_time  # Use Discord's built-in time tracking
            )
    else:
        rpc.clear()

def detect_geforce_now():
    """Check if GeForce Now is running and identify the game from the window title."""
    try:
        # Iterate over all window titles to find one containing "GeForce NOW" and a known game title
        for window in gw.getAllTitles():
            if "GeForce NOW" in window:
                # Extract the game title part from the window title
                game_title = window.split(" on GeForce NOW")[0]
                # Check if the extracted title matches any known game titles
                if game_title in game_map:
                    return game_title
        return None
    except Exception as e:
        return None

def is_geforce_now_running():
    """Check if GeForce Now process is running."""
    for proc in psutil.process_iter(['name']):
        if proc.info['name'] == "GeForceNOW.exe":
            return True
    return False

def main():
    """Main function to run the presence updater with Discord's built-in time tracking."""
    no_game_detected_count = 0
    game_start_time = None
    current_game = None
    game_detected_sleep_duration = 60  # Sleep time in seconds after detecting a game

    while True:
        if not is_geforce_now_running():
            rpc.clear()  # Clear Discord presence if GeForce Now itself is not running
            time.sleep(30)  # Check every 30 seconds if GeForce Now starts again
            continue

        game_title = detect_geforce_now()
        if game_title:
            if game_title != current_game:
                current_game = game_title
                game_start_time = time.time()  # Start timer when a new game is detected
            update_discord_presence(game_title, game_start_time)
            no_game_detected_count = 0  # Reset counter when a game is detected
            time.sleep(game_detected_sleep_duration)  # Sleep for 60 seconds when game is detected
        else:
            if current_game:
                current_game = None
                game_start_time = None
                rpc.clear()  # Clear Discord Rich Presence only when the game exits
            no_game_detected_count += 1
            # Adjust sleep time based on how long no game has been detected
            if no_game_detected_count > 5:
                time.sleep(30)  # If no game detected for 5 cycles, check every 30 seconds
            else:
                time.sleep(10)  # Default check every 10 seconds

if __name__ == "__main__":
    main()
