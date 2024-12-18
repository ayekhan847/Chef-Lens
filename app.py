#This is the main streamlit app file
import streamlit as st
from parse_recipe import parse_recipe
from generate_explanation import generate_explanation
from generate_image import generate_image

st.title("Recipe Explainer")
recipe_url = st.text_input("Enter Recipe URL:")

if recipe_url:
    # Call the parse_recipe function
    recipe_content = parse_recipe(recipe_url)

    # Display the recipe title
    st.subheader(recipe_content["title"])

    # Display Ingredients
    st.subheader("Ingredients")
    for ingredient in recipe_content["ingredients"]:
        st.write(ingredient)

    # Display Steps with Explanations and Images
    st.subheader("Instructions")
    steps = recipe_content["instructions"].split('. ')  # Split instructions into individual steps
    for i, step in enumerate(steps):
        st.write(f"Step {i + 1}: {step}")

        # Generate and display explanation
        explanation = generate_explanation(step)
        st.write(f"Explanation: {explanation}")

        # Generate and display AI image (only when clicked in an expandable container)
        with st.expander(f"Show Image for Step {i+1}"):
            image_url = generate_image(step)
            if image_url != "Image generation failed.":
                st.image(image_url, caption=f"Visual for Step {i+1}")
            else:
                st.write("Image could not be generated.")


    # Display recipe image
    if recipe_content["image_url"]:
        st.image(recipe_content["image_url"], caption=recipe_content["title"])
