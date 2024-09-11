# GPT Chatbot with OpenAI API

This Python script implements a simple conversation loop that allows users to interact with OpenAI's GPT-4 model. The script takes user input, sends it to the OpenAI API, and returns the model's response. It continues the conversation until the user types "exit" to end the session.

## Features

- Establishes a conversation with GPT-4 using the OpenAI API.
- Prompts the user for input and displays the GPT-4 response.
- Ends the conversation loop when the user types "exit".

## Prerequisites

Before running this script, ensure you have the following:

- Python 3.7+
- An OpenAI API key. You can get one by signing up at [OpenAI](https://platform.openai.com/signup/).

## Installation

1. Clone the repository or download the script.
2. Install the required dependencies:
    ```bash
    pip install openai
    ```

## Usage

1. Replace the placeholder `'your-api-key-here'` in the script with your actual OpenAI API key.
2. Run the script:
    ```bash
    python chatbot.py
    ```

3. Start interacting with GPT-4 by typing your queries. Type `'exit'` to stop the conversation.
you might encounter this error while pip install openai idk the solution tbh..
![image](https://github.com/user-attachments/assets/bf99f675-0c88-43c1-a185-abbc1f384313)

## Code Example

```python
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

# Conversation loop
if __name__ == "__main__":
    print("Chat with GPT! Type 'exit' to stop the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        response = chat_with_gpt(user_input)
        print(f"GPT: {response}")
