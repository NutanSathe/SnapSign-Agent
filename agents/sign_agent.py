from tools.sign_mapper_tool import SIGN_MAP

class SignAgent:
    def get_sign(self, keyword):
        if keyword in SIGN_MAP:
            return SIGN_MAP[keyword]
        return None
