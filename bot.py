import discord
import time
import datetime
client = discord.Client()
'''
IDEAS
- WIG CHANT
'''

#variables

wigged = ""
bewigged = datetime.datetime.now()
foo = 0
truck = """:black_large_square: :black_large_square: :black_large_square: :black_large_square: :black_large_square: 
    :black_large_square: :black_large_square: :black_large_square: :black_large_square: :black_large_square: 
    :white_small_square: :white_small_square: :truck: :white_small_square: :white_small_square:
    :black_large_square: :black_large_square: :black_large_square: :black_large_square: :black_large_square: 
    :black_large_square: :black_large_square: :black_large_square: :black_large_square: :black_large_square:"""
status = ""
tom = "<:tomwalkerface:810822991561752586>"

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    global truck
    global wigged
    global bewigged
    global foo
    global status
    global tom
    if message.author == client.user:
        return
    if message.channel.name == "channel-name":
        if message.content.startswith('HELP ME!'):
            await message.channel.send("try typing one of the following: WIG! | TRUCK! | LEFT! | RIGHT! | LUBE!")
        if message.content.startswith('WIG!'):
            if not wigged:
                bewigged = datetime.datetime.now() + datetime.timedelta(minutes=20)
                wigged = "yes"
                my_message = await message.channel.send(""":yellow_square::yellow_square::yellow_square::yellow_square::yellow_square::yellow_square:""")
                await my_message.edit(content = """<:tomwal1Wig:733522436259184680> :yellow_square::yellow_square::yellow_square::yellow_square::yellow_square:""")
                await my_message.edit(content = """:yellow_square: <:tomwal1Wig:733522436259184680> :yellow_square::yellow_square::yellow_square::yellow_square:""")
                await my_message.edit(content = """:yellow_square::yellow_square: <:tomwal1Wig:733522436259184680> :yellow_square::yellow_square::yellow_square:""")
                await my_message.edit(content = """:yellow_square::yellow_square::yellow_square: <:tomwal1Wig:733522436259184680> :yellow_square::yellow_square:""")
                await my_message.edit(content = """:yellow_square::yellow_square::yellow_square::yellow_square: <:tomwal1Wig:733522436259184680> :yellow_square:""")
                await my_message.edit(content = """:yellow_square::yellow_square::yellow_square::yellow_square::yellow_square: <:tomwal1Wig:733522436259184680> """)
                print(bewigged, wigged)
                my = await message.channel.send(truck + tom)
                tom = "<:tomwalkeranimeface:831515693232160769>"
                await my.edit(content= truck + tom)
        if message.content.startswith('TRUCK!'):
            if datetime.datetime.now() > bewigged:
                tom = "<:tomwalkerface:810822991561752586>"
                wigged=""
            await message.channel.send(truck+tom)
        if message.content.startswith("LEFT!"):
            if datetime.datetime.now() > bewigged:
                tom = "<:tomwalkerface:810822991561752586>"
                wigged=""
            if status:
                await message.channel.send("WEVE ALREADY CRASHED \n"+truck+tom)
            else: 
                my_message = await message.channel.send(":black_large_square: :black_large_square: :black_large_square: :black_large_square: :black_large_square: \n :black_large_square: :black_large_square: :black_large_square: :black_large_square: :black_large_square: \n :white_small_square: :white_small_square: :truck:  :white_small_square:  :white_small_square: \n :black_large_square: :black_large_square: :black_large_square: :black_large_square: :black_large_square: \n :black_large_square: :black_large_square: :black_large_square: :black_large_square: :black_large_square:")
                await my_message.edit(content = """:black_large_square: :black_large_square: :black_large_square: :black_large_square: :black_large_square: 
        :black_large_square: :black_large_square: :black_large_square: :black_large_square: :black_large_square: 
        :white_small_square: :white_small_square: :white_small_square: :white_small_square: :white_small_square:
        :black_large_square: :black_large_square: :truck: :black_large_square: :black_large_square: 
        :black_large_square: :black_large_square: :black_large_square: :black_large_square: :black_large_square: """ + tom)
                await my_message.edit(content = """:black_large_square: :black_large_square: :black_large_square: :black_large_square: :black_large_square: 
        :black_large_square: :black_large_square: :black_large_square: :black_large_square: :black_large_square: 
        :white_small_square: :white_small_square: :white_small_square: :white_small_square: :white_small_square:
        :black_large_square: :black_large_square: :black_large_square: :black_large_square: :black_large_square: 
        :black_large_square: :black_large_square: :truck: :black_large_square: :black_large_square: """+ tom)
                await my_message.edit(content= """:black_large_square: :black_large_square: :black_large_square: :black_large_square: :black_large_square: 
        :black_large_square: :black_large_square: :black_large_square: :black_large_square: :black_large_square: 
        :white_small_square: :white_small_square: :white_small_square: :white_small_square: :white_small_square:
        :black_large_square: :black_large_square: :black_large_square: :black_large_square: :black_large_square: 
        :black_large_square: :black_large_square: :black_large_square: :black_large_square: :black_large_square:
                    :truck: """+ tom)
                truck = """:black_large_square: :black_large_square: :black_large_square: :black_large_square: :black_large_square: 
        :black_large_square: :black_large_square: :black_large_square: :black_large_square: :black_large_square: 
        :white_small_square: :white_small_square: :white_small_square: :white_small_square: :white_small_square:
        :black_large_square: :black_large_square: :black_large_square: :black_large_square: :black_large_square: 
        :black_large_square: :black_large_square: :black_large_square: :black_large_square: :black_large_square:
                    :truck:
                """
                status = "l"
                await my_message.edit(content=truck+tom)

        if message.content.startswith("RIGHT!"):
            if datetime.datetime.now() > bewigged:
                tom = "<:tomwalkerface:810822991561752586>"
                wigged=""
            if status:
                await message.channel.send("WEVE ALREADY CRASHED \n"+truck+tom)
            else: 
                my_message = await message.channel.send(""":black_large_square: :black_large_square: :black_large_square: :black_large_square: :black_large_square:
        :black_large_square: :black_large_square: :black_large_square: :black_large_square: :black_large_square:
        :white_small_square: :white_small_square: :truck: :white_small_square:  :white_small_square:
        :black_large_square: :black_large_square: :black_large_square:  :black_large_square: :black_large_square:
        :black_large_square: :black_large_square: :black_large_square: :black_large_square: :black_large_square:"""+ tom)
                await my_message.edit(content = """:black_large_square: :black_large_square: :black_large_square: :black_large_square: :black_large_square: 
        :black_large_square: :black_large_square: :truck: :black_large_square: :black_large_square: 
        :white_small_square: :white_small_square: :white_small_square: :white_small_square: :white_small_square:
        :black_large_square: :black_large_square: :black_large_square: :black_large_square: :black_large_square: 
        :black_large_square: :black_large_square: :black_large_square: :black_large_square: :black_large_square: """+ tom)
                await my_message.edit(content= """:black_large_square: :black_large_square: :truck: :black_large_square: :black_large_square: 
        :black_large_square: :black_large_square: :black_large_square: :black_large_square: :black_large_square: 
        :white_small_square: :white_small_square: :white_small_square: :white_small_square: :white_small_square:
        :black_large_square: :black_large_square: :black_large_square: :black_large_square: :black_large_square: 
        :black_large_square: :black_large_square: :black_large_square: :black_large_square: :black_large_square: """+ tom)
                truck = """                         :truck:
        :black_large_square: :black_large_square: :black_large_square: :black_large_square: :black_large_square: 
        :black_large_square: :black_large_square: :black_large_square: :black_large_square: :black_large_square: 
        :white_small_square: :white_small_square: :white_small_square: :white_small_square: :white_small_square:
        :black_large_square: :black_large_square: :black_large_square: :black_large_square: :black_large_square: 
        :black_large_square: :black_large_square: :black_large_square: :black_large_square: :black_large_square: """
                status = "r"
                await my_message.edit(content=truck+ tom)

        if message.content.startswith("LUBE!"):
            if datetime.datetime.now() > bewigged:
                tom = "<:tomwalkerface:810822991561752586>"
                wigged=""
            my_message = await message.channel.send(""":black_large_square: :black_large_square: :black_large_square: :black_large_square: :black_large_square: :pickup_truck: """)
            await my_message.edit(content = """ :black_large_square: :black_large_square: :black_large_square: :black_large_square: :pickup_truck: """)
            await my_message.edit(content = """ :black_large_square: :black_large_square: :black_large_square: :pickup_truck: """)
            await my_message.edit(content = """ :black_large_square: :black_large_square: :pickup_truck: """)
            await my_message.edit(content = """ :black_large_square: :pickup_truck: """)
            await my_message.edit(content = """ :pickup_truck: """)
            await my_message.edit(content = "DID YOU CALL 13")
            await my_message.edit(content = "DID YOU CALL 13 30")
            await my_message.edit(content = "DID YOU CALL 13 30 32???")
            status = ""
            truck = """:black_large_square: :black_large_square: :black_large_square: :black_large_square: :black_large_square: 
    :black_large_square: :black_large_square: :black_large_square: :black_large_square: :black_large_square: 
    :white_small_square: :white_small_square: :truck: :white_small_square: :white_small_square:
    :black_large_square: :black_large_square: :black_large_square: :black_large_square: :black_large_square: 
    :black_large_square: :black_large_square: :black_large_square: :black_large_square: :black_large_square:"""
            await my_message.edit(content =truck+tom)
client.run('<YOUR-ID-GOES-HERE>')
