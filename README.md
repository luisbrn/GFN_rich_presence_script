GeForce Now Discord Rich Presence Script (v1.2.0)
=================================================
![a79c8754-a3dc-421d-bf21-9b9b9e10f435](https://github.com/user-attachments/assets/8bf4145a-947c-4e3e-bc56-9e3076a0d229)

Overview
--------

The GeForce Now Discord Rich Presence Script allows you to display your current game from GeForce Now directly in your Discord status. It adds a customized Rich Presence, including the game name, a custom image (if available in your Rich Presence assts), and the elapsed playtime. The script runs in the background as long as GeForce Now is open and automatically closes when you exit GeForce Now.

Features
--------

-   Automatic Discord Rich Presence: Automatically detects the game you're playing on GeForce Now and updates your Discord status accordingly.
-   Custom Images: Shows game-specific images or icons in Discord Rich Presence for supported games.
-   Time Tracking: Displays the amount of time you've been playing the game.
-   Silent Background Operation: Runs without popping up windows (via `pythonw.exe`).
-   Auto-Exit: Stops running automatically when GeForce Now is closed.

Prerequisites
-------------

-   Python 3.7+ installed on your system.
-   Install the following required Python libraries:
    ```bash
    pip install pypresence psutil pygetwindow
    ```
    
Installation
------------

1.  **Clone or Download the Repository**: Download the repository to your local machine and unzip it if necessary.

2.  **Run the Setup Script**: Open a terminal or command prompt, navigate to the repository folder, and run `setup.py` to configure your Discord Client ID and GeForce Now executable path:

    arduino
    ```bash
    python setup.py
    ```
    During setup:

    -   Enter your Discord Client ID (you can create one via the Discord Developer Portal).
    -   Browse and select your GeForceNOW.exe file.
    -   Optionally, create a desktop shortcut that will launch both GeForce Now and the Rich Presence script.
3.  **Create a Shortcut**: After setting up the configurations, you can create a desktop shortcut using the setup GUI. This shortcut will start GeForce Now and the Discord Rich Presence script together.

4.  **Launch the Shortcut**: Use the shortcut on your desktop to launch GeForce Now with the Rich Presence script running in the background. Your Discord status will automatically update with the game you're playing.

How It Works
------------

The script detects the games you're playing by:

1.  **Monitoring GeForce Now**: It scans the window titles in GeForce Now to detect the active game.
2.  **Updating Discord**: It sends updates to Discord's Rich Presence API to reflect the current game, time played, and an optional custom image.
3.  **Auto-Closing**: The script stops running when you close GeForce Now, removing your Rich Presence status.

### Game and Asset Mapping

The script relies on two dictionaries in the `game_assets.py` file:

-   **`game_map`**: Maps detected game titles to game names that are displayed in Discord.
-   **`asset_map`**: Maps game names to asset keys used for displaying custom images in Discord.

#### Example `game_assets.py`:

```python
# game_assets.py

game_map = {
    "Halo Infinite": "Halo Infinite",
    "Cyberpunk 2077": "Cyberpunk 2077",
    "Far Cry 5": "Far Cry 5"
}

asset_map = {
    "Halo Infinite": "halo_infinite_image",
    "Cyberpunk 2077": "cyberpunk_2077_image",
    "Far Cry 5": "far_cry_5_image"
}`
```

You can edit this file to add or remove games as needed.

### Adding Custom Images to Discord

To show custom images for each game in Discord Rich Presence, follow these steps:

1.  **Go to the Discord Developer Portal**:

    -   Open the Discord Developer Portal.
    -   Select or create your application (used for Rich Presence).
2.  **Upload Rich Presence Assets**:

    -   Navigate to the **Rich Presence** section.
    -   Click **Art Assets** and upload custom images. Each image needs a **unique key**.
3.  **Link the Assets to Your Script**:

    -   After uploading, note the **asset key** for each image.
    -   In the `asset_map` dictionary in `game_assets.py`, link the game name to the asset key.

    Example:

    ```python
    asset_map["Cyberpunk 2077"] = "cyberpunk_2077_image"
    ```
    
4.  **Save the Changes**:

    -   Once the images are uploaded and the `game_assets.py` file is updated, the images will appear in your Discord Rich Presence while playing GeForce Now.

How to Add More Games
---------------------

To add support for more games:

1.  Open the `game_assets.py` file.
2.  Add new entries to both `game_map` and `asset_map` dictionaries.
    -   `game_map` should contain the window title detected by GeForce Now.
    -   `asset_map` should contain the corresponding asset key from Discord.

Example:

```python
game_map["New Game"] = "New Game"
asset_map["New Game"] = "new_game_image"`
```

Screenshots
-----------
![image](https://github.com/user-attachments/assets/ff082a4d-f56d-49d2-a1ae-b7315bda3af7)

![image](https://github.com/user-attachments/assets/8458347e-5016-48eb-8b25-ff5b93ca4789)

![image](https://github.com/user-attachments/assets/f1bc5685-f33d-4363-a69d-d37519232caa)

![image](https://github.com/user-attachments/assets/46e5e5c3-afd5-4712-a379-544902688f9f)



### Discord Rich Presence Example

Here's what your Discord status will look like while playing a game on GeForce Now.

Notes
-----

-   **Game detection** is based on the window title from GeForce Now. Ensure that the game's title is correctly mapped in `game_map`.
-   If no custom image is available for a game, a default image will be used in Discord Rich Presence.
-   You can configure more games and images by editing `game_assets.py` and adding assets to your Discord Developer application.

Troubleshooting
---------------

-   **Rich Presence not updating**: Ensure the game title from GeForce Now matches an entry in `game_map`. Add the game manually if necessary.
-   **Python not found**: Ensure `pythonw.exe` is installed and configured correctly in your system's PATH.

License
-------

This project is licensed under the MIT License. See the LICENSE file for details.
