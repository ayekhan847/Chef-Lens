#This will have the AI image generation function for each step
import openai
import os

openai.api_key = os.getenv("AYESHA_API")

def generate_image(step_text):
    try:
        prompt = f"A high-quality, realistic photograph showing: {step_text}. No text in the image, clean background, professional food photography style."

        # Generate the image
        response = openai.Image.create(
            model="dall-e-3",
            prompt=prompt,
            size="1024x1024",
            quality="standard",
            n=1
        )
        # Get the URL of the generated image
        image_url = response['data'][0]['url']
        return image_url

    except Exception as e:
        # Print detailed error information
        print("Error generating image:")
        print(f"Type of Exception: {type(e)}")
        print(f"Exception message: {e}")
        if hasattr(e, 'response') and e.response is not None:
            print("Status code:", e.response.status_code)
            print("Response data:", e.response.json())
        return "Image generation failed."

