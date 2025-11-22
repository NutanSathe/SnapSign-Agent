
import google.generativeai as genai

genai.configure(api_key="AIzaSyA8Cni3PeQlOxYQhkT6RYJXjSAy8eilsWE")

class KeywordAgent:
    def extract(self, text):
        prompt = f"Extract the main keyword from this phrase: '{text}'"

        # FREE model (works for generate_content)
        model = genai.GenerativeModel("gemini-2.0-flash")

        response = model.generate_content(prompt)

        return response.text.strip().lower()


