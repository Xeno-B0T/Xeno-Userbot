from telethon.sessions import StringSession
from telethon.sync import TelegramClient
import random
from colorama import Fore, Style, Back


legend = """
╔╗──╔═══╦═══╦═══╦═╗─╔╦═══╦═══╦═══╦╗──╔╗
║║──║╔══╣╔═╗║╔══╣║╚╗║╠╗╔╗║╔═╗║╔═╗║╚╗╔╝║  
║║──║╚══╣║─╚╣╚══╣╔╗╚╝║║║║║║─║║╚═╝╠╗╚╝╔╝  
║║─╔╣╔══╣║╔═╣╔══╣║╚╗║║║║║║╚═╝║╔╗╔╝╚╗╔╝   
║╚═╝║╚══╣╚╩═║╚══╣║─║║╠╝╚╝║╔═╗║║║╚╗─║║   
╚═══╩═══╩═══╩═══╩╝─╚═╩═══╩╝─╚╩╝╚═╝─╚╝   

"""
baap_bolte = """
#Demented Xeno Userbot         
Made with love by Xeno Officials
"""
                                                                                                            
print("")
print(Style.BRIGHT + Fore.MAGENTA + legend)
print(Style.RESET_ALL)
print(Style.BRIGHT + Fore.BLUE + logo)
print(Style.RESET_ALL)
print(Style.BRIGHT + Fore.CYAN + Back.BLUE + baap_bolte)
print(Style.RESET_ALL)
print("""Welcome To Xeno String Session Generator By @SempleBoy""")
print("""Kindly Enter Your Details To Continue ! """)

apiKEY = input("API_KEY: ")
apiHASH = input("API_HASH: ")

while True:
    try:
        with TelegramClient(StringSession(), API_KEY, API_HASH) as client:
            print("String Session Saved In Your Saved Messages ! ")
            print("")
            session = client.session.save()
            client.send_message(
                "me",
                f"Here is your TELEGRAM STRING SESSION\n(Tap to copy it)👇 \n\n `{session}` \n\n And Visit @XenoChats For Any Help !",
            )

            print(
                "Thanks for Choosing Xeno Userbot Have A Good Time....Note That When You Terminate the Old Session ComeBack And Genrate A New String Session Old One Wont Work"
            )
    except:
        print("")
        print(
            "Wrong phone number \n make sure its with correct country code. Example : +919811099999 ! Kindly Retry"
        )
        print("")
        continue
    break
