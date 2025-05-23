import google.generativeai as genai

genai.configure(api_key="AIzaSyCJ8LNsCrH2M6RfcYrUprWQ7JhphBKfd_4")

while True:

    idea=input("What kind of image do you want to generate?\n")

    prompt=f"""
    Create a detailed, optimized prompt for generating an AI image based on this idea:'{idea}'

    The prompt should:
    - Be specific about style, composition, lighting, colors, and mood
    - Include relevant technical specifications (aspect ratio, quality level)
    - Use descriptive language that AI image generators respond well to
    - Be structured in a way that prioritizes the most important elements
    - Be between 50-150 words for optimal results

    Just provide the final prompt without explanations.
    """

    model = genai.GenerativeModel("gemini-2.0-flash")
    response=model.generate_content(prompt)

    if response.text.strip():  # Check if response is not empty or only whitespace
        print("\nOptimized image prompt:\n")
        print(response.text.strip())
        print("\nYou can use this prompt with your preferred image generation tool.")
    else:
        print("\nNo valid response received. Please try again.")

    userChoice=input("Do you want to generate prompt for another image? (yes/no): ")
    if userChoice!='yes':
        print("Exiting the program.")
        break

# for model in genai.list_models():
#     print(model.name)

# pip install google-generativeai     
