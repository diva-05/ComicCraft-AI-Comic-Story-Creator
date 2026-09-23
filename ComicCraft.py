import google.generativeai as genai


genai.configure(api_key="AQ.Ab8RN6LtiFVsWCTJpls3LHCVduTP_HyEs7LB9oX_6bFqUHHjdg")

def generate_comic_story(prompt_text):
    model = genai.GenerativeModel('gemini-3.5-flash')
    prompt = f"Create a 4-panel comic strip script based on: '{prompt_text}'. Include Panel descriptions, character actions, and dialogues."
    
    response = model.generate_content(prompt)
    return response.text

if __name__ == "__main__":
    print("=== ComicCraft: AI Comic Story Creator ===")
    topic = input("Enter your comic story idea: ")
    print("\nGenerating comic script...\n")
    result = generate_comic_story(topic)
    print("=== COMIC SCRIPT OUTPUT ===")
    print(result)
