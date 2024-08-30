# Discord Nuke Bot
## made by zentonik

**Warning:** This script is intended for educational purposes only. Using it maliciously is against Discord's Terms of Service and can result in severe consequences, including bans and legal action.

## Overview

This bot script, written in Python using `discord.py`, is designed to perform a destructive set of actions on a Discord server:

- **Change server name and icon.**
- **Delete all channels and roles.**
- **Ban all members.**
- **Create new channels and roles.**
- **Send spam messages across the server.**

## Features

- **Rate Limiting Handling:** Manages Discord’s rate limits to ensure smooth operation.
- **Concurrent Operations:** Deletes channels and roles, and creates new ones concurrently for efficiency.

## Required Libraries

This bot requires the following Python libraries:

- `discord.py` for interacting with the Discord API.
- `aiohttp` for making asynchronous HTTP requests.

## Setup

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/zentonik/discord-nuke-bot.git
   cd discord-nuke-bot
