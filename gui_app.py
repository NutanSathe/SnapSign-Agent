import tkinter as tk
from tkinter import Label, Button, Entry
from PIL import Image, ImageTk
from agents.input_agent import InputAgent
from agents.keyword_agent import KeywordAgent
from agents.sign_agent import SignAgent

class SnapSignGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("SnapSign Desktop App")
        self.root.geometry("400x500")

        # Input label
        Label(root, text="Enter Here:", font=("Arial", 14)).pack(pady=10)

        # Input box
        self.input_box = Entry(root, font=("Arial", 14))
        self.input_box.pack(pady=10)

        # Button
        Button(root, text="Show Sign", font=("Arial", 14), command=self.run_agent).pack(pady=10)

        # Area to show sign result
        self.result_label = Label(root, text="", font=("Arial", 14))
        self.result_label.pack(pady=10)

        # Image display area
        self.image_label = Label(root)
        self.image_label.pack(pady=20)

    def run_agent(self):
        text = self.input_box.get()

        input_agent = InputAgent()
        keyword_agent = KeywordAgent()
        sign_agent = SignAgent()

        cleaned = input_agent.process(text)
        keyword = keyword_agent.extract(cleaned)
        image_path = sign_agent.get_sign(keyword)

        self.result_label.config(text=f"Keyword: {keyword}")

        img = Image.open(image_path)
        img = img.resize((200, 200))
        img = ImageTk.PhotoImage(img)

        self.image_label.configure(image=img)
        self.image_label.image = img

if __name__ == "__main__":
    root = tk.Tk()
    app = SnapSignGUI(root)
    root.mainloop()
