import os
from dotenv import load_dotenv
from google import genai
import time


def fixSpelling(query):
    load_dotenv()
    ai_api_key = os.environ.get("GEMINI_API_KEY")

    client = genai.Client(api_key=ai_api_key)
    response = client.models.genrate_content(
        model="gemini-2.5-flash-lite",
        content=f"""
        Fix the spelling errors in this youtube search query.  
        Only correct obivous typos. Don't change correctly spelled words.

        Query: {query}

        Return the query in this format:
        Corrected: Query"""
    )
    return response.text

