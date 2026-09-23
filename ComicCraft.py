import google.generativeai as genai
genai.configure(api_key="AQ.Ab8RN6KIkCM8sv95Cqs-qRBVvyrolRWI04NEQ_tIzt4jmfow_A")

def generate_comic_story(prompt_text):
    model = genai.GenerativeModel('gemini-3.6-flash')
    
    prompt = f"Create a 4-panel comic strip script based on: '{prompt_text}'. Include Panel descriptions, character actions, and dialogues."
    
    print("Generating comic script...\n")
    response = model.generate_content(prompt)
    return response.text

if __name__ == "__main__":
    print("=== ComicCraft: AI Comic Story Creator ===")
    topic = input("Enter your comic story idea: ")
    result = generate_comic_story(topic)
    print("\n=== COMIC SCRIPT OUTPUT ===")
    print(result)
