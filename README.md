# Discord Rich Presence for GeForce Now

This script updates Discord Rich Presence based on the game running on GeForce Now.

## Features

- Detects games running via GeForce Now.
- Updates Discord Rich Presence with the current game’s details.
- Uses pre-uploaded images for game assets.

## Requirements

- Python 3.x
- `pygetwindow`
- `pypresence`

## Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/yourusername/discord-rich-presence-gfn.git
    cd discord-rich-presence-gfn
    ```

2. **Install Dependencies**:
    ```bash
    pip install pygetwindow pypresence
    ```

## Configuration

1. **Edit the Script**:
    - Open `main.py` and replace `your_discord_client_id` with your actual Discord client ID.

2. **Add Game Mappings**:
    - Modify the `game_map` dictionary in `main.py` to include the games you want to detect.
    - Add entries as follows:
      ```python
      game_map = {
          "Platform": {
              "Process Name": "Game Title"
          }
      }
      ```

3. **Upload Assets to Discord**:
    - Go to the [Discord Developer Portal](https://discord.com/developers/applications).
    - Select your application and navigate to the "Rich Presence" section.
    - Upload images for each game in the "Art Assets" section.
    - Note the names of the assets and update the `asset_map` dictionary in `main.py` with these names.

## Usage

1. **Run the Script**:
    ```bash
    python main.py
    ```

2. **Observe**:
    - The script will periodically check for running games and update your Discord Rich Presence accordingly.

## Auto-Start with Windows

To have the script and GeForce Now start automatically when Windows starts, follow these steps:

1. **Create a Batch File**:
    - Create a file named `start_gfn_and_script.bat` with the following content:

      ```batch
      @echo off
      start "" "C:\path\to\GeForceNow.exe"
      python "C:\path\to\main.py"
      ```

    - Replace `C:\path\to\GeForceNow.exe` with the actual path to the GeForce Now executable.
    - Replace `C:\path\to\main.py` with the actual path to your Python script.

2. **Add the Batch File to Windows Startup**:
    - Press `Win + R`, type `shell:startup`, and press Enter. This opens the Startup folder.
    - Place a shortcut to your `start_gfn_and_script.bat` file in this folder. The batch file will now run automatically when Windows starts.

## Troubleshooting

- Ensure that the `DISCORD_CLIENT_ID` is correct.
- Verify that the asset names in `asset_map` match the names of the uploaded images in the Discord Developer Portal.
- Make sure Python is installed and added to your system PATH.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
