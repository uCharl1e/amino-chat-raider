import amino

print("╔════════════════════════════════════════╗")
print("      Amino Chat Raider by uCharl1e")
print("╚════════════════════════════════════════╝")

print("\n-- login --")
email= input("Enter your email address >> ")
password= input("Enter your password >> ")
client=amino.Client()
client.login(email=email,password=password)
print("\nLogged in...")
print("-- choose A community --")
comlist= client.sub_clients(size=100)
for name, id in zip(comlist.name,comlist.comId):
   print("Comm name: ",name,"\nComm Id:",id,"\n-----------")
ID= input("Please enter Community ID >> ")
print("-- choose A chat --")
subclient = amino.SubClient(comId=ID, profile=client.profile)
chats = subclient.get_public_chat_threads(size=1000)
for name, id in zip(chats.title, chats.chatId):
    print(name,":", id, "\n")
print("-----------")
Chat= input("Please paste chat ID here >> ")
client.join_community(comId=ID)
print("\nJoined Community...")
print("-- start --")
subclient.join_chat(chatId=Chat)
print("\nAnd so... the chaos begins...")
mssg=input("\nInput Message >> ")
while True:
    subclient.send_message(chatId=Chat,message=mssg)
    print("you sent: ",mssg)
