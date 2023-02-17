from pychatsonic.chatai.chat import ChatSonic

chat = ChatSonic("my_api_key", "en")
put = str(input("[?] Ask a ai: "))
text = chat.ask(put)
                
print("[I] {}".format(text))
