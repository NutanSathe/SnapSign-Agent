from agents.input_agent import InputAgent
from agents.keyword_agent import KeywordAgent
from agents.sign_agent import SignAgent
from agents.display_agent import DisplayAgent

def run_snapsign():
    print("=== SnapSign Agent ===")
    user_input = input("Enter a phrase: ")

    # Step 1: Input processing
    input_agent = InputAgent()
    cleaned = input_agent.process(user_input)

    # Step 2: Keyword extraction
    keyword_agent = KeywordAgent()
    keyword = keyword_agent.extract(cleaned)

    # Step 3: Sign mapping
    sign_agent = SignAgent()
    sign_image = sign_agent.get_sign(keyword)

    # Step 4: Display result
    display_agent = DisplayAgent()
    display_agent.show(sign_image, keyword)

if __name__ == "__main__":
    run_snapsign()
