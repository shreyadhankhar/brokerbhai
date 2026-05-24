import requests
import time
def run_negotiation(api_key, chosen_persona, flat_details, rules):
    prompt_text = f"""
You are {chosen_persona}, acting on behalf of your client. 
Target Property: {flat_details}
Client Rules: {rules}
CRITICAL INSTRUCTION FOR LENGTH: You are on the phone with the stubborn Listing Owner. This must be a LONG, drawn-out, highly dramatic negotiation. Write a massive transcript with at least 10 to 15 back-and-forth dialogue exchanges. Include fake walk-outs, emotional blackmail, shouting matches over the deposit, and intense haggling to lower the rent and deposit by 15%. Do not rush the ending. Make it highly entertaining using Mumbai slang!
CRITICAL: You must end your entire response with the exact tag: [DEALS_FINALIZED]
"""
    
    if not api_key:
        time.sleep(2)
        return f"""**📞 MOCK TRANSCRIPT (EXTENDED EDITION)**
*Dialing Listing Owner...*
Owner: "Listen, the price is fixed."
{chosen_persona}: "Are you joking? With those amenities? Drop the rent by 15% and deposit by 20% right now or I walk."
Owner: "No chance. I have 5 people waiting."
{chosen_persona}: "Let them wait. My client has the cash ready today. But rules are: {rules}."
Owner: "Ugh, fine. Adjusted."
**✅ FINAL SHORTLIST:**
Negotiated Flat - 15% Off Rent, 20% Off Deposit. Successfully secured.
[DEALS_FINALIZED]"""
    # THE REAL GOOGLE GEMINI API ENDPOINT
    API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"
    headers = {"Content-Type": "application/json"}
    
    payload = {
        "contents": [{"parts": [{"text": prompt_text}]}],
        "generationConfig": {
            "temperature": 0.85,
            "maxOutputTokens": 2000
        }
    }
    
    try:
        response = requests.post(API_URL, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()["candidates"][0]["content"]["parts"][0]["text"]
    except Exception as e:
        return f"API Error: {str(e)} - Double check your Gemini API Key!"
