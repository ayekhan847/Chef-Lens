#This will have the AI explanation function
import openai
# from Mawi_Key import MAWI_API
import json
# Directly assign your OpenAI API key here
with open('.config', 'r') as f:
    config = json.load(f)
openai.api_key = config["OPEN_API_KEY"]



#This function should take each specific step and generate a better explanation
def generate_explanation(step_text):
    # Placeholder: AI function to generate explanations for each step
    try:
        # Use the chat completion endpoint with the chat model
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "user",
                    "content": (
                        f"I'm cooking and I need help with this step: '{step_text}'. "
                        "Please explain it in a friendly, detailed way, as if you are guiding me through it. "
                        "Include any tips or suggestions to make this step easier, and explain why it is important."
                    )
                }
            ]
        )
        explanation = response.choices[0].message.content
        return explanation.strip()
    except Exception as e:
        print(f"Error generating explanation: {e}")
        return "An error occurred while generating the explanation."
