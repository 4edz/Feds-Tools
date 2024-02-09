import discord
import asyncio
import webbrowser
import time



def print_fading_text():
    text = r"""
            ______         __        ______            __    ___   __
           / ____/__  ____/ /____   /_  __/___  ____  / /  _/ ( )_/ /
          / /_  / _ \/ __  / ___/    / / / __ \/ __ \/ /  / __/// __/
         / __/ /  __/ /_/ (__  )    / / / /_/ / /_/ / /  (_  ) (_  ) 
        /_/    \___/\__,_/____/    /_/  \____/\____/_/  /  _/ /  _/  
                                                  
                                                 
    +-----------------------+|1. Server Raider  |+-----------------------+
    +-----------------------+|2. Server Booster |+-----------------------+
    +-----------------------+|3. Server Joiner  |+-----------------------+
    +-----------------------+|4. Server Nuker   |+-----------------------+

    +-----------------------+|x. Our Server     |+-----------------------+
    +-----------------------+|w. For Help       |+-----------------------+"
    """

    for i in range(len(text)):
        if i < len(text) // 2:
            print(f"\033[91m{text[i]}", end="")
        else:
            print(f"\033[94m{text[i]}", end="")
        time.sleep(0.001)

print_fading_text()



while True:
    user_input = input("Enter Your Choice: ")
    
    if user_input == "x":
        webbrowser.open("https://discord.gg/dTDAQfNxS7")
        
    elif user_input == "w":
        webbrowser.open("https://hastebin.com/share/fumaqowiyu.vbnet")

    elif user_input == "3":
        with open('token.txt', 'r') as file:
            token = file.read().strip()

        client = discord.Client()

        @client.event
        async def on_ready():
            print(f'Logged in as {client.user.name} ({client.user.id})')

            invite_link = input('Enter the Discord invite link: ')

            try:
                invite = await client.get_invite(invite_link)
                await invite.accept()
                print('Joined the server successfully!')
            except discord.errors.NotFound:
                print('Invalid invite link.')
            except discord.errors.HTTPException:
                print('Failed to join the server.')

        client.run(token)

    elif user_input == "1":
        def spam_message(token, channel_id, message):
            intents = discord.Intents.default()
            client = discord.Client(intents=intents)

            @client.event
            async def on_ready():
                channel = client.get_channel(channel_id)
                if channel is not None:
                    for _ in range(100):
                        await channel.send(message)
                else:
                    print("Invalid channel ID")

            client.run(token)

        def main():
            token_file = "token.txt"
            invite_link = input("Enter the Discord invite link: ")
            channel_id = input("Enter the channel ID: ")
            message = input("Enter the message to be spammed: ")

            with open(token_file, "r") as file:
                token = file.read().strip()

            spam_message(token, int(channel_id), message)

        if __name__ == "__main__":
            main()

    elif user_input == "2":
        print("This Is Not Apart Of The Free Version Of Feds Tool..")

    elif user_input == "4":
        webbrowser.open("https://cdn.discordapp.com/attachments/1202453567940862013/1203227794155372544/GalaxyNuker.rar?ex=65d05435&is=65bddf35&hm=d9d4f7466c7bba697ea906a7830116f2ac1a26b3a11dd1a30f035299c42d59b4&")
