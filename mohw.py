import asyncio
import discord
import openpyxl

client = discord.Client()

@client.event
async def on_ready():
    print(client.user.name)
    print(client.user.id)
    print("온라인이에요!")

@client.event
async def on_message(message):
    if message.content.startswith("보건복지부 공지"):
        channel = message.content.split(' ')[2]
        msg = message.content.split(channel)[1][1:]
        await client.get_channel(int(channel)).send(msg)

async def my_background_task():
    await client.wait_until_ready()
    while not client.is_closed():
        game = discord.Game("시범 운영중인 서비스입니다.")
        await client.change_presence(status=discord.Status.online, activity=game)
        await asyncio.sleep(5)
        game = discord.Game(f'{len(client.users)}명의 시민들과 소통하는중')
        await client.change_presence(status=discord.Status.online, activity=game)
        await asyncio.sleep(5)
        game = discord.Game("국민의 삶의 질을 높이고 모두를 포용하는 복지!")
        await client.change_presence(status=discord.Status.online, activity=game)
        await asyncio.sleep(5)
        game = discord.Game("보건복지부입니다.")
        await client.change_presence(status=discord.Status.online, activity=game)
        await asyncio.sleep(5)

client.loop.create_task(my_background_task())

access_token = os.environ["BOT_TOKEN"]
client.run('BOT_TOKEN')
