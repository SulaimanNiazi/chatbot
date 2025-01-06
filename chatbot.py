from os import system, name
import requests

def clrscr():
    if name=='nt':
        system('cls')
    else:
        system('clear')
    return
def genText(query):
    headersdata={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:133.0) Gecko/20100101 Firefox/133.0",
        "Accept": "text/x-component",
        "Accept-Language": "en-US,en;q=0.5",
        "Next-Action": "a36d91d9045092774ec0cbe4fffe0f24354fa327",
        "Next-Router-State-Tree": "%5B%22%22%2C%7B%22children%22%3A%5B%22reply-generator%22%2C%7B%22children%22%3A%5B%5B%22type%22%2C%22generic-reply%22%2C%22d%22%5D%2C%7B%22children%22%3A%5B%22__PAGE__%3F%7B%5C%22type%5C%22%3A%5C%22generic-reply%5C%22%7D%22%2C%7B%7D%5D%7D%5D%7D%5D%7D%2Cnull%2Cnull%2Ctrue%5D",
        "Content-Type": "text/plain;charset=UTF-8",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "no-cors",
        "Sec-Fetch-Site": "same-origin",
        "Priority": "u=0",
        "Pragma": "no-cache",
        "Cache-Control": "no-cache"
    }
    jsondata="[{\"reply\":\""+query+"\",\"variationsNumber\":1,\"emoji\":false,\"replyLength\":\"shorter\",\"writingStyle\":\"casual\",\"type\":\"generic-reply\",\"replyInstructions\":\"You are in conversation with me\",\"hashtags\":false,\"trackedAnon\":null,\"anonymousId\":\"\"}]"
    x=requests.post('https://free-tools.planable.io/reply-generator/generic-reply',data=jsondata,headers=headersdata)
    response = x.text.replace('â','\'').replace('\\n',"\n").replace('ï¸','')
    return response[45:len(response)-4]

def main():
    while 1:
        prompt=input('You: ')
        response=genText(prompt)
        print('Chatbot: ',response)
        if prompt.lower().__contains__('bye'):
            return

if __name__=='__main__':
    clrscr()
    main()