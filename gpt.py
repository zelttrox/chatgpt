import requests

# API Variables
API_KEY = ''
API_URL = 'https://api.openai.com/v1/chat/completions'
MODEL = "gpt-3.5-turbo"

# Headers Request
headers = {
    'Authorization': f'Bearer {API_KEY}',
    'Content-Type': 'application/json'
}

arch_context = "I'm using a Dell XPS 13 9340 laptop on Arch Linux with Hyprland. I'm using the yay AUR."
arch_symbol = '@'

# Post Mapping to OpenAI API
def think(prompt):
    
    if prompt[0] == arch_symbol:
        prompt = arch_context + prompt[1:]
    
    data = {
        "model": MODEL,
        "messages": [{"role": "user", "content": prompt}]
    }
    
    response = requests.post(API_URL, headers=headers, json=data)
    
    if response.status_code == 200:
        return response.json()['choices'][0]['message']['content']
    else:
        return "Error: " + response.text

def main():
    try:
        while True:
            user_input = input("\033[91m[Prompt]: \033[0m")
            if user_input.lower() == 'exit':
                break
            response = think(user_input)
            print(f"\033[91m[GPT-3]: \033[0m{response}\n")
    except KeyboardInterrupt:
        print("\n\033[91m[System]: \033[0mExiting..")

if __name__ == "__main__":
    main()
