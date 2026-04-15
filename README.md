# QueryCord
A self-hosted Discord bot script for executing PostgreSQL queries from Discord.

## Overvier
**QueryCord** is a self-hosted Discord bot script that allows trusted users to execute PostgreSQL quaries directly from Discord.

It is designed to be deployed as part of your own Discord bot, not invited as a shared or hosted bot. You run it yourself and decide who has access.

This project is intended for personal Discord servers.

## Configuration
Create a .env file or set environment variables following the contents of .env.example:
```
# Your discord bot token
DISCORD_TOKEN=

# Username of users who can use database commands
USER_DB_PERMISSION=
- To add more users, add spaces between usernames.


# Database connection settings
DATABASE=
HOST=
USER=
PASSWORD=
```

## Security Warning
This bot exposes database access through Discord messages.
- Do not deploy in public servers
- Do not grant access to untrusted users
