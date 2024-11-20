#This will have the AI image generation function for each step
import openai
import os

openai.api_key = "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"

def generate_image(step_text):
    try:
        prompt = f"A detailed photograph of: {step_text}"

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

