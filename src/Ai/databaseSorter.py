import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
ai_api_key = os.environ.get("GEMINI_API_KEY")

def DbClasschooser(channelName, channelDes):

    client = genai.Client(api_key=ai_api_key)
    response = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents=f"""
        This is the Name of a youtube channel {channelName} and it's description: {channelDes}.
        Pleas Return one or two types where the channel would fit in. The Types you can choos from are:
        1. Frontend
        2. Backend
        3. Bible/Religion
        4. ML/AI/LLM
        5. Engeeniring/Architekture
        6. Motivation
        7. CyberSec
        8. PersonalDevelopment
        9. AI SLOP
        10. Hardware
        11. News/Nachrichten
        12. Finance/Finanzen
        13. General

        Pleas consider basic youtube knowlage and that im tech interested so most types are meant IT like Architecktue i want software atchiteckture.
        Pleas give rather on than 2 only if youre realy sure that it is split into 2 caretogire give 2.
        And the return should only be the 1 or 2 kategories in this format. if there is not a second use ----
        The Format: Frist: KATEGORIE | Second: KATEGORIE   

        """
    )
    return response.text



