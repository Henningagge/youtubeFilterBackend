import os
from dotenv import load_dotenv
from google import genai
import time
load_dotenv()
ai_api_key = os.environ.get("GEMINI_API_KEY")

def fixSpelling(query):

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

def improveQuery(query):

    client = genai.Client(api_key=ai_api_key)
    response = client.models.genrate_content(
        model="gemini-2.5-flash-lite",
        content=f"""
        Rewrite this Youtube Search query to be more specific and searchbal.

        Original: {query}

        Consider:
        - That the person that write the Query is interested in Tech and Programming.
        - Keep it concise (under 10 words)
        - It should be a google style search query that's very specific
        - Don't use boolean logic


        Return the query in this format:
        Rewritten query: Query"""
    )
    return response.text