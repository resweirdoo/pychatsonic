import requests
class ChatSonic():
    def __init__(self, api: str, lang: str, content_type = "application/json"):
        self.api = api
        self.engines = ("good", "average", "premium", "economy",)
        self.lang = lang
        self.content_type = content_type

    def ask(self, question, engine="premium", enable_google_results="true", enable_mem=False) -> str:
        url = f"https://api.writesonic.com/v2/business/content/chatsonic?engine={engine}&lang={self.lang}"

        payload = {
    "enable_google_results": enable_google_results,
    "enable_memory": enable_mem,
    "input_text": question
}
        headers = {
    "accept": "application/json",
    "content-type": self.content_type,
    "X-API-KEY": self.api
}   
        return requests.post(url, json=payload, headers=headers).json()["message"]
    
    def question(self, paragraph, num=3, engine="premium") -> list:
        url = f"https://api.writesonic.com/v2/business/content/question-generation?language={self.lang}&num_copies={num}"

        payload = {"paragraph": paragraph}
        
        headers = {
    "accept": "application/json",
    "content-type": self.content_type,
    "X-API-KEY": self.api
}
        return requests.post(url, json=payload, headers=headers).json()
