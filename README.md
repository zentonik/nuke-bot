# Discord Nuke Bot
### Made by Zentonik

**Warning:** This script is intended for educational purposes only. Using it maliciously is against Discord's Terms of Service and can result in severe consequences, including bans and legal action.

## Overview

This bot script, written in Python using `discord.py`, is designed to perform a destructive set of actions on a Discord server:

- **Change server name and icon.**
- **Delete all channels and roles.**
- **Ban all members.**
- **Create new channels and roles based on user input.**
- **Send spam messages across the server.**

## Features

- **User Input for Customization:** When you run the script, it asks how many channels and roles you want to create, as well as their names. This allows for customization of the server's new structure after the destructive actions.
- **Rate Limiting Handling:** Manages Discord’s rate limits to ensure smooth operation.
- **Concurrent Operations:** Deletes channels and roles, and creates new ones concurrently for efficiency.

## Required Libraries

This bot requires the following Python libraries:

- `discord.py` for interacting with the Discord API.
- `aiohttp` for making asynchronous HTTP requests.

## Notes
- You must replace the placeholders `YOUR_ICON_URL` and `YOUR_BOT_TOKEN` in the script for it to work properly.
- The bot requires appropriate permissions in the Discord server, such as Manage Channels, Manage Roles, Ban Members, etc.
- During the execution, the script will prompt you to input:
  - **Number of channels to create.**
  - **Number of roles to create.**
  - **Names for the new channels and roles.**

## How to Use

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/zentonik/discord-nuke-bot.git
   cd discord-nuke-bot
