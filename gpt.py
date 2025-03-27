import requests

# API Variables
API_KEY = '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'
API_URL = 'https://api.openai.com/v1/chat/completions'
MODEL = "gpt-3.5-turbo"

# Headers Request
headers = {
    'Authorization': f'Bearer {API_KEY}',
    'Content-Type': 'application/json'
}

# Post Mapping to OpenAI API
def think(prompt):
    
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
    
    print("GPT-3.5-Turbo.\n")
    
    while True:
        user_input = input("[Prompt]: ")
        if user_input.lower() == 'exit':
            break
        response = think(user_input)
        
        print(f"GPT-3.5: {response}")

if __name__ == "__main__":
    main()