![Logo](https://cdn.discordapp.com/attachments/1047795672520339488/1076176039685918760/11_20230217191858.png)

# Chatsonic API

A python adapter for the Chatsonic API, designed to allow for easy integration and use of the Chatsonic API within a Python environment. 
The adapter provides a convenient and streamlined way for developers to access the full suite of features offered by the Chatsonic API, including real-time messaging, automated chatbots, and other advanced chat functionalities. 
With this adapter, developers can easily create custom chat experiences for their users and take advantage of the scalability and reliability offered by the Chatsonic platform. Whether building a simple chatbot or a complex conversational system, the Chatsonic API adapter for Python is a must-have tool for any developer looking to enhance their chat-based applications.

(_text writed by chat-ai_)


## Demo

```python 
from pychatsonic.chatai.chat import ChatSonic

chat = ChatSonic("your_api_key", "en")
text = chat.ask("Hello!")

print(text)
```
----
```python
import telebot

bot = telebot.TeleBot(token="your_telegram_api_token")
chat = ChatSonic("your_api_key", "en")

@bot.message_handler(content_types=["text"]):
def cmd_ai(message):
    text = chat.ask(message.text)
    bot.send_message(message.chat_id, text)

bot.infinity_polling() 
'''Warning! This code may not work!'''

```



## Authors

- [@resweirdoo](https://www.github.com/resweirdoo) (or i)


## Installation

Install my-project with git

```bash
  git clone https://github.com/resweirdoo/chat-ai
```
    
## Donate

Hey! I will be so happy if you [buy me a coffee](https://boosty.to/resweirdoo)

thank you!
