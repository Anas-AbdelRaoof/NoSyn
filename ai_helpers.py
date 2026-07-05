from groq import Groq
import os
from dotenv import load_dotenv
from system_prompt import system_prompt


def convert_pseudocode_to_code_with_ai():
    """
    Connect to Groq API and convert pseudocode to actual code using AI.
    
    This function sends pseudocode to the Groq API (using the Llama 3.3 70B model)
    and returns the AI-generated code based on the system prompt.
    
    Returns:
        str: The AI-generated code as a string
    """

    # Load environment variables from .env file to access API credentials securely
    load_dotenv()

    # Initialize the Groq API client with the API key from environment variables
    client = Groq(
        api_key=os.environ.get("GROQ_API_KEY")
    )

    # Retrieve the system prompt that defines how the AI should behave
    # This prompt guides the AI on how to convert pseudocode to actual code
    systemPrompt = system_prompt()

    # Send a chat completion request to the Groq API with the system prompt
    # The model will process the pseudocode and generate corresponding code
    current_system_prompt = system_prompt()

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": current_system_prompt,
            } # The system prompt contains the pseudocode to be converted
        ],
        model="llama-3.3-70b-versatile",
    )

    # Extract and return the generated code from the API response
    return chat_completion.choices[0].message.content
