import requests
import time
def negotiate_flat(api_key, location, rent, deposit, rules):
def negotiate_flat(api_key, chosen_persona, flat_details, rules):
    prompt_text = f"""
You are Broker-Bhai, an autonomous AI real estate negotiator in Mumbai.
User Criteria: Location: {location}, Max Rent: {rent}, Max Deposit: {deposit}, Rules: {rules}.
Simulate a live, aggressive, funny phone negotiation using Mumbai slang with 3 brokers: Raju, Sharma Ji, and Kunal. 
You are {chosen_persona}, acting on behalf of your client. 
Target Property: {flat_details}
Client Rules: {rules}
CRITICAL INSTRUCTION FOR LENGTH: This must be a LONG, drawn-out, highly dramatic negotiation. I want a massive transcript with at least 10 to 15 back-and-forth dialogue exchanges. Include fake walk-outs, emotional blackmail, shouting matches over the deposit, and intense haggling before they finally cave in to the user's limits. Do not rush the ending. Make it an entertaining read!
CRITICAL INSTRUCTION FOR LENGTH: You are on the phone with the stubborn Listing Owner. This must be a LONG, drawn-out, highly dramatic negotiation. Write a massive transcript with at least 10 to 15 back-and-forth dialogue exchanges. Include fake walk-outs, emotional blackmail, shouting matches over the deposit, and intense haggling to lower the rent and deposit by 15%. Do not rush the ending. Make it highly entertaining using Mumbai slang!
Filter out bad flats and haggle below the user's max limits.
CRITICAL: You must end your exact response with the tag: [DEALS_FINALIZED]
CRITICAL: You must end your entire response with the exact tag: [DEALS_FINALIZED]
"""
    
    if not api_key:
        time.sleep(2)
        return f"""**📞 MOCK TRANSCRIPT (EXTENDED EDITION)**
*Dialing Raju in {location}...*
Raju: "Hello? Yes bhai, flat is available. Rent is 60k, Deposit is 3 Lakhs. Take it or leave it, 10 people are waiting downstairs."
Broker-Bhai: "Are you mad, Raju? 3 Lakhs deposit for a matchbox? I will give you {deposit} max, and rent {rent}. Final."
Raju: "Arre sir, owner will kill me. Society is very strict. Minimum 2.5 Lakhs."
Broker-Bhai: "Don't play games Raju, I know the market. Either {deposit} or I am hanging up and calling Sharma Ji right now."
Raju: "Wait wait sir... don't cut the call! Let me check with the owner."
*...2 minutes of intense hold music...*
Raju: "Okay sir, owner is crying but he agreed. But no pets allowed."
Broker-Bhai: "My client rules are: {rules}. If that works, deal. If not, I'm walking."
Raju: "Done sir, done. Send the token amount before he changes his mind."
*Dialing Listing Owner...*
Owner: "Listen, the price is fixed."
{chosen_persona}: "Are you joking? With those amenities? Drop the rent by 15% and deposit by 20% right now or I walk."
Owner: "No chance. I have 5 people waiting."
{chosen_persona}: "Let them wait. My client has the cash ready today. But rules are: {rules}."
Owner: "Ugh, fine. Adjusted."
**✅ FINAL SHORTLIST:**
Secured in {location}. Rent: {rent}, Deposit: {deposit}.
Negotiated Flat - 15% Off Rent, 20% Off Deposit. Successfully secured.
[DEALS_FINALIZED]"""
    API_URL = "https://api.antigravity.io/v1/chat/completions"
    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
    
    # Added max_tokens to give the AI plenty of room to write a long script
    payload = {
        "model": "gemini-1.5-flash", 
        "messages": [{"role": "system", "content": prompt_text}], 
    except Exception as e:
        return f"API Error: {str(e)}"
