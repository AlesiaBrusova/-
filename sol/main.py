import discord
import random
from discord import Intents, File
from bot_logic import gen_pass
from discord.ext import commands

TOKEN = "MTE4ODQ4MzUyNDE5ODY3NDQ2Mg.GGQAdK.mMnIlXgLfkye50RHdkNt5TaDSnJ_0CkipGZJXQ"
# Создаем бота в переменной client и передаем все привелегии
bot = commands.Bot(command_prefix="$", intents=Intents.all())

player_data = {}
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    if message.content.isdigit():
        password = gen_pass(int(message.content))
        await message.channel.send(password)
    elif message.content.startswith('$статья'):
        await message.channel.send("Природа нашей Родины очень красива. Прекрасны её леса, поля, рощи и луга. В лесах средней полосы России произрастают деревья и кустарники, некоторые из которых занесены в Красную книгу. Они очень полезны не только для животных, но и для человека. .Не все люди бережно относятся к природе: разводят в лесах костры, вырубают ёлки к Новому году, бросают мусор в реки и озёра, отходы с заводов и фабрик нередко тоже оказываются в водоёмах. А из-за этого погибает множество рыб, иногда очень ценных пород. Если люди не поймут, что природу нужно беречь, то будут погибать не только рыбы, но и животные, птицы. Не будут здоровыми растения. В результате этого коровам, овцам, козам нечего будет есть. Не станет молочных и мясных продуктов в магазинах. Людям будет нечем дышать, так как экология будет испорчена. Поэтому очень важно беречь природу, правильно организовывать работу фабрик и заводов.")
    elif message.content.startswith("$помощь"):
        await message.channel.send("$статья, $помощь, $тест, $ссылку, $стоп")
    elif message.content.startswith("$тест"):
        await message.channel.send(random.choice(['в какую книгу занесены редкие виды животных и растений? ||Красная||', 'Так как экологию будет испорчена, люди не смогут... ||дышать||', "название науки, которая изучает нарушение взаимосвязей в природе ||экология||", "Что, в основном, производят из переработанных пластиковых бутылок? ||одежду||"]))
    elif message.content.startswith("$ссылку"):
        await message.channel.send(random.choice(["https://ru.m.wikipedia.org/wiki/%D0%AD%D0%BA%D0%BE%D0%BB%D0%BE%D0%B3%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B9_%D0%BA%D1%80%D0%B8%D0%B7%D0%B8%D1%81", "https://www.oum.ru/literature/raznoe/ekologiya-osnovnye-ponyatiya/", "https://foxford.ru/wiki/okruzhayuschiy-mir/chto-izuchaet-ekologiya?utm_referrer=https%3A%2F%2Fyandex.ru%2F"]))
    if message.content.startswith("$стоп"):
        exit()
    
    
    
            
        
    
    await bot.process_commands(message)
    
bot.run(TOKEN)