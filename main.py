import discord
from discord.ext import commands

from tabulate import tabulate

import os
from dotenv import load_dotenv

from config.config import get_connection


load_dotenv()

discord_token = os.getenv('DISCORD_TOKEN')
users_with_dbpermission = os.getenv('USER_DB_PERMISSION').split(' ')

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=".", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')



# ==================================================
# ---------------------COMMANDS---------------------
# ==================================================


statements = [
    'SELECT',
    'INSERT',
    'DELETE',
    'UPDATE'
]

@bot.command(name="db", description="Database command.")
async def dbCmd(ctx, sql, table: str | None):
    if ctx.author.name not in users_with_dbpermission:
        await ctx.reply('You do not have permission to database.')
        return
    
    
    if not sql.strip().upper().startswith(tuple(statements)):
        await ctx.send(f'Only {', '.join(statements)} statements are allowed.')
        return
    
    conn = get_connection()
    cursor = conn.cursor()


    try:
        cursor.execute(sql)

        if sql.strip().upper().startswith('SELECT'):
            record = cursor.fetchall()
            headers = [desc[0] for desc in cursor.description]

            formatted_output = '\n'.join(str(row) for row in record) or 'No results.'
            formatted_table = tabulate(record, headers=headers, tablefmt='grid')

            if table == 'tabulate':
                formatted_output = formatted_table

            await ctx.send(f'**Output:**\n```\n{formatted_output}```')


        else:
            conn.commit()
            await ctx.send(f'**Query:**\n```\n{sql}```\n- Query sent successfully.')


    except Exception as err:
        await ctx.send(f'Error: {err}')

    
    finally:
        conn.close()
        cursor.close()



@bot.command(name='test', description='Test command.')
async def test(ctx, arg):
    await ctx.send(f'Test command received with argument: {arg}')



bot.run(discord_token)