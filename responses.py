
import crypto

def sample_responses(input_text):
    user_message = str(input_text).lower()

    if user_message in ("oi", "ola", "olá"):
        return "E ai, blz?"
    elif "links" in user_message:
        return "linktree: https://bsalles2596.github.io/Bsalles2596.github.io-Linktree/"
    elif "contato" in user_message:
        return "Converse comigo no WhatsApp: https://wa.me/message/U7VIT2HZCZBEJ1"
    
    elif "github" in user_message:
        return "Github: https://github.com/Bsalles2596"

    return "não estou entendendo você! tente novamente."