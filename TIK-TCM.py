try:
    from TikTokLive import TikTokLiveClient;from TikTokLive.types.events import *;from TikTokLive.types.errors import *;from datetime import datetime;from colorama import Fore;d=datetime.now();d1=str(d).split(" ")[0];d2=str(d).split(" ")[1]
except Exception as e:print(f'[!] Download The Missing Module ! , {e}');exit()

print(f"""

{Fore.LIGHTRED_EX}████████╗██╗██╗  ██╗  {Fore.RED}████████╗ ██████╗███╗   ███╗
{Fore.LIGHTRED_EX}╚══██╔══╝██║██║ ██╔╝  {Fore.RED}╚══██╔══╝██╔════╝████╗ ████║
{Fore.LIGHTRED_EX}   ██║   ██║█████╔╝{Fore.LIGHTWHITE_EX}█████╗{Fore.RED}██║   ██║     ██╔████╔██║
{Fore.LIGHTRED_EX}   ██║   ██║██╔═██╗{Fore.LIGHTWHITE_EX}╚════╝{Fore.RED}██║   ██║     ██║╚██╔╝██║
{Fore.LIGHTRED_EX}   ██║   ██║██║  ██╗     {Fore.RED}██║   ╚██████╗██║ ╚═╝ ██║
{Fore.LIGHTRED_EX}   ╚═╝   ╚═╝╚═╝  ╚═╝     {Fore.RED}╚═╝    ╚═════╝╚═╝     ╚═╝{Fore.RESET}

              By @TweakPY - @vv1ck   
""")
user=input(f"{Fore.WHITE}[{Fore.LIGHTRED_EX}?{Fore.WHITE}] username : ");print("\n")
client: TikTokLiveClient=TikTokLiveClient(unique_id=f"@{user}")
@client.on("connect")
def connect(_: ConnectEvent):
    print(f"{Fore.WHITE}[{Fore.LIGHTRED_EX}!{Fore.WHITE}] Viewers Count :", client.viewer_count)
    print(f"{Fore.WHITE}[{Fore.LIGHTRED_EX}!{Fore.WHITE}] Connected to Room ID :", client.room_id)
@client.on("live_end")
def dis_connect(event: LiveEndEvent):
    print(f"\n\n{Fore.WHITE}[{Fore.LIGHTRED_EX}-{Fore.WHITE}] Livestream Ended !\n")
    print(f"\n{Fore.WHITE}[{Fore.LIGHTRED_EX}+{Fore.WHITE}] Press (CTRL + C ) to Exit")
###join , msg if you want to enable that just delete all [#] on the left of the code
#@client.on("join")
#def join(event: JoinEvent):
#    print(f"{Fore.WHITE}[{Fore.LIGHTRED_EX}+{Fore.WHITE}] {event.user.uniqueId}  <-- user | Name -->  {event.user.nickname}  Joined The Stream !")
#    with open(f'{user}_Join_{d1}.txt', 'a') as x:
#        x.write(str(event.user.uniqueId)+'\n')
@client.on("like")
def like(event: LikeEvent):
    print(f"{Fore.WHITE}[{Fore.LIGHTRED_EX}+{Fore.WHITE}] {event.user.uniqueId}  <-- user | Name -->  {event.user.nickname}  Liked The Stream !")
    with open(f'{user}_Like_{d1}.txt', 'a') as x:
        x.write(str(event.user.uniqueId)+'\n')
@client.on("follow")
def follow(event: FollowEvent):
    print(f"{Fore.WHITE}[{Fore.LIGHTRED_EX}+{Fore.WHITE}] {event.user.uniqueId}  <-- user | Name -->  {event.user.nickname}  Followed The Streamer !")
    with open(f'{user}_Follow_{d1}.txt', 'a') as x:
        x.write(str(event.user.uniqueId)+'\n')
@client.on("share")
def share(event: ShareEvent):
    print(f"{Fore.WHITE}[{Fore.LIGHTRED_EX}+{Fore.WHITE}] {event.user.uniqueId}  <-- user | Name -->  {event.user.nickname}  Shared The Streamer !")
    with open(f'{user}_Share_{d1}.txt', 'a') as x:
        x.write(str(event.user.uniqueId)+'\n')

def Comment(event: CommentEvent):
    #Beta Badwords Filter
    badwords=['badword','0']
    try:    
        if event.comment in badwords:
            print(f'{"*"*30}\n{Fore.WHITE}[{Fore.LIGHTRED_EX}!{Fore.WHITE}] Bad word Detected -> {event.comment}\nsent by user : \n{Fore.WHITE}[{Fore.LIGHTRED_EX}!{Fore.WHITE}] user : {event.user.uniqueId}\n{Fore.WHITE}[{Fore.LIGHTRED_EX}!{Fore.WHITE}] Name : {event.user.nickname}\n{Fore.WHITE}[{Fore.LIGHTRED_EX}!{Fore.WHITE}] userid : {event.user.userId}\n{"*"*30}')
            with open(f'{user}_users_ban_{d1}.txt', 'a') as x:
                x.write(str(event.user.uniqueId+"    "+str(event.user.nickname)+"    "+str(event.user.userId)+"    -->  "+str(event.comment))+"    "+str(f'|  Detected in : {d2}')+'\n')
        else:
            print(f"{Fore.WHITE}[{Fore.LIGHTRED_EX}+{Fore.WHITE}] {event.user.uniqueId} : {event.comment}")
    except Exception as i:print(f'{Fore.WHITE}[{Fore.LIGHTRED_EX}!{Fore.WHITE}] Error , {i} ');exit()

client.add_listener("comment",Comment)
try:
    try:client.run()
    except KeyboardInterrupt:exit()
except (FailedFetchRoomInfo,FailedParseUserHTML,FailedConnection):print(f'{Fore.WHITE}[{Fore.LIGHTRED_EX}!{Fore.WHITE}] user Not Found or The user is offline in The Moment.');exit()
