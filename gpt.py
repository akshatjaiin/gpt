import openai

# Replace with your OpenAI API key
openai.api_key = 'your-api-key-here'

def chat_with_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are ChatGPT, a helpful AI."},
            {"role": "user", "content": prompt}
        ]
    )
    
    # Extract and return the assistant's reply
    return response['choices'][0]['message']['content']

#Conversation loop
if __name__ == "__main__":
    print("Chat with GPT! Type 'exit' to stop the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        response = chat_with_gpt(user_input)
        print(f"GPT: {response}")
