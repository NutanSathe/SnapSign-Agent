class DisplayAgent:
    def show(self, image_path, keyword):
        if image_path:
            print(f"\nKeyword detected: {keyword}")
            print(f"Sign image: {image_path}")
        else:
            print("\nSorry, no sign found for that keyword.")
