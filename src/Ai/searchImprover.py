import os
from dotenv import load_dotenv
from google import genai
load_dotenv()
ai_api_key = os.environ.get("GEMINI_API_KEY")

def fixSpelling(query):

    client = genai.Client(api_key=ai_api_key)
    response = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents=f"""
        QUERY: {query}
        Goal: Output a cleaned and slightly refined YouTube search, preserving the same language (German or English or Both).
        Instructions:
        IF THE QUERY STARTS WITH "no imp" IT SHOULD NOT BE CHANGED AND BE JUST RETURNED IN FORMAT ALSO INCLUED IT IN THE RESPONSE.
        Detect the input language (German or English) and keep the output in that language only.
        Fix spelling, spacing, and capitalization of names, brands, models, and common terms.
        Normalize tech/product terms (e.g., noise cancelling, Bluetooth, 4K, RTX 3060; deutsch/englisch).
        Keep meaningful numbers, versions, years; remove accidental filler words.
        If intent is obvious, add 1–2 highly relevant helper terms (e.g., tutorial, review, official, test, live) that match the purpose; avoid guessing if uncertain.
        Use quotes around multi‑word titles, product models, and proper names to keep them together.
        Only add exclusions with minus terms when the user clearly asked to avoid something.
        Return only the final YouTube search string, no extra text."""
    )
    return response.text

def improveQuery(query):

    client = genai.Client(api_key=ai_api_key)
    response = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents=f"""QUERY: {query}
            Goal: Produce a high‑quality YouTube search string that boosts relevance, adds precise modifiers, and appends a fitting channel name when appropriate. Return only the final YouTube search string, no extra text.
            
            Core principles
            IF THE QUERY STARTS WITH "no imp" IT SHOULD NOT BE CHANGED AND BE JUST RETURNED IN FORMAT.
            Infer intent first (how‑to, repair, tutorial, guide, review, comparison, benchmark, news, interview, documentary, music video, live, playlist, VOD).
            Keep the user’s language if clear; optionally add a language tag (deutsch/german/englisch/english) only if it helps the search.
            Quote multi‑word keyphrases, product names, and proper nouns to keep them together.
            Add 1–3 targeted modifiers that strengthen the intent (e.g., tutorial, guide, review, comparison, benchmark, official, full, playlist).
            Append an exact channel name in quotes only when there’s a strong, widely known association with the topic. If unsure, skip the channel.
            Use minus terms to filter unwanted formats when the intent suggests it (e.g., -shorts, -live, -cover, -remix, -fanmade, -compilation).
            Keep it compact. Prefer a few strong terms over many weak ones. Avoid parentheses and special punctuation; use only quotes and minus.
            Channel addition heuristics

            Tutorials/how‑tos: consider "iFixit", "Corey Schafer", "Fireship", "freeCodeCamp.org", "Traversy Media", "Web Dev Simplified", "The Net Ninja".
            Tech reviews/benchmarks: "Marques Brownlee", "Dave2D", "Mrwhosetheboss", "Linus Tech Tips", "GamersNexus", "Digital Foundry".
            Academic/lectures: "MIT OpenCourseWare", "Stanford", "Khan Academy", "3Blue1Brown".
            Science/explainers: "Kurzgesagt – In a Nutshell", "Veritasium", "PBS Space Time", "Two Minute Papers".
            Music/live/session: "NPR Music", "Colors", official artist channel.
            Localized German content: "GIGA", "heise online", "ct magazin", "ComputerBase", "BR24", "tagesschau", "WBS".
            Only add a channel when it clearly fits the topic and audience language; don’t guess niche names.
            Disambiguation and enrichment

            Versions/models: include exact identifiers (e.g., "RTX 4070 Ti Super", "iPhone 15 Pro", "ThinkPad X1 Carbon Gen 10", "PS5").
            Years and patches: add a year or version only when it narrows intent (2024, iOS 17, patch 1.2.1).
            Platforms: Windows 11, macOS, Android, iOS, PS5, Xbox, Nintendo Switch.
            Regions/language: deutsch/german/englisch/english, EU/US/UK only if it affects content.
            Music specifics: official video, lyric video, audio, live, cover, remix; exclude with minus terms when intent is official.
            Gaming specifics: build, guide, boss, speedrun, any%, no commentary, patch number; add -shorts if long‑form is desired.
            Structure and phrasing

            Quote primary multi‑word phrases and channel names.
            Keep 1–3 modifiers; avoid keyword stuffing.
            Use exact, commonly recognized spellings and diacritics.
            Avoid ambiguous add‑ons like free, best, top unless clearly implied by intent.
            No extra commentary; output is the search string only.
            Step‑by‑step assembly

            Normalize obvious typos and brand/model spellings.
            Identify the main phrase(s) and quote them.
            Decide the intent and add 1–3 precise modifiers.
            Add disambiguators (version/year/platform/patch/language) only if helpful.
            Append a well‑matched channel in quotes if strongly associated; otherwise omit.
            Add minus terms to filter formats you don’t want.
            Remove fluff; ensure quotes and spacing are clean.
            Return only the final YouTube search string."""
    )
    return response.text