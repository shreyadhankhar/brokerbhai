import streamlit as st
import broker_agent
import pdf_builder
import requests
import time
from fpdf import FPDF
st.set_page_config(page_title="Broker-Bhai", page_icon="🏢")
st.title("🏢 Broker-Bhai: The Autonomous Flat Negotiator")
st.caption("Enter your criteria. Let the AI fight the Mumbai brokers for you.")
# --- 1. PDF GENERATOR LOGIC ---
# THE FIX: Renamed this function to avoid the variable collision!
def sanitize_pdf_text(text):
    return text.encode('ascii', 'ignore').decode('ascii')
with st.sidebar:
    st.header("⚙️ Settings")
    api_key = st.text_input("Antigravity API Key:", type="password")
    st.caption("Leave blank for Mock Mode")
def generate_contract(flat_details, transcript):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(200, 10, txt="BROKER-BHAI: OFFICIAL SHORTLIST", ln=True, align='C')
    pdf.ln(10)
    pdf.set_font("Arial", size=11)
    pdf.multi_cell(0, 7, txt=sanitize_pdf_text(f"Target Property: {flat_details}"))
    pdf.ln(5)
    clean_transcript = transcript.replace("[DEALS_FINALIZED]", "").strip()
    pdf.multi_cell(0, 7, txt=sanitize_pdf_text(clean_transcript))
    return pdf.output(dest='S').encode('latin-1')
st.subheader("📋 Your Requirements")
with st.container(border=True):
    col1, col2 = st.columns(2)
    with col1:
        location = st.text_input("Preferred Location", "Andheri West")
        rent = st.number_input("Max Rent (Rs/month)", value=40000)
    with col2:
        deposit = st.number_input("Max Deposit (Rs)", value=150000)
        rules = st.text_input("Special Rules", "Bachelor, Need parking")
# --- 2. AI AGENT LOGIC ---
def run_negotiation(chosen_persona, flat_details, rules):
    api_key = "AIzaSyDESH1-U9eg07gM4Q3hWw0QrBKrYwlZ35A"
    
    prompt_text = f"""
You are {chosen_persona}, acting on behalf of your client. 
Target Property: {flat_details}
Client Rules: {rules}
if st.button("🚀 Unleash Broker-Bhai", use_container_width=True):
    with st.spinner("Broker-Bhai is negotiating..."):
        response = broker_agent.negotiate_flat(api_key, location, rent, deposit, rules)
CRITICAL INSTRUCTION FOR LENGTH: You are on the phone with the stubborn Listing Owner. This must be a LONG, drawn-out, highly dramatic negotiation. Write a massive transcript with at least 10 to 15 back-and-forth dialogue exchanges. Include fake walk-outs, emotional blackmail, shouting matches over the deposit, and intense haggling to lower the rent and deposit by 15%. Do not rush the ending. Make it highly entertaining using Mumbai slang!
"""
    API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={api_key}"
    headers = {"Content-Type": "application/json"}
    
    payload = {
        "contents": [{"parts": [{"text": prompt_text}]}],
        "safetySettings": [
            {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_NONE"},
            {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_NONE"},
            {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_NONE"},
            {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_NONE"}
        ],
        "generationConfig": {
            "temperature": 0.85,
            "maxOutputTokens": 2000
        }
    }
    
    try:
        response = requests.post(API_URL, headers=headers, json=payload)
        response.raise_for_status()
        data = response.json()
        
        st.success("Negotiation Complete!")
        clean_text = response.replace("[DEALS_FINALIZED]", "").strip()
        if "candidates" in data and len(data["candidates"]) > 0:
            candidate = data["candidates"][0]
            if candidate.get("finishReason") == "SAFETY":
                return "The negotiation got too heated and Google's safety filters cut the call! Try a different agent like Kunal."
            return candidate["content"]["parts"][0]["text"]
        else:
            return "API Error: Unexpected response format from Google."
            
    except Exception as e:
        return f"API Error: {str(e)}"
# --- 3. STREAMLIT UI LOGIC ---
st.set_page_config(page_title="Broker-Bhai", page_icon="🏢", layout="wide")
personas = {
    "Raju (Street Hustler)": "raju.png",
    "Sharma Ji (Strict Uncle)": "sharma.png",
    "Kunal (Corporate Shark)": "kunal.png"
}
with st.sidebar:
    st.header("⚙️ Settings")
    st.success("✅ Live Gemini 2.5 API Connected")
    st.divider()
    st.header("🤖 Choose Your Fighter")
    chosen_persona = st.radio("Select Negotiator:", list(personas.keys()))
    
    try:
        st.image(personas[chosen_persona], caption=f"Active Agent: {chosen_persona.split(' ')[0]}", use_container_width=True)
    except Exception:
        pass 
        
        with st.expander("📜 View Live Transcript", expanded=True):
            st.markdown(clean_text)
        
        if "[DEALS_FINALIZED]" in response:
            pdf_bytes = pdf_builder.generate_contract(location, rent, deposit, response)
            st.download_button("📄 Download Final Shortlist PDF", data=pdf_bytes, file_name="Shortlist.pdf", mime="application/pdf", type="primary")
    rules = st.text_input("Any Dealbreakers?", "E.g., Bachelor, Need parking")
st.title("🏢 Broker-Bhai: AI Real Estate Dashboard")
st.info("Select an agent from the sidebar and deploy them on a property below.")
properties = [
    {"id": 1, "title": "Luxury 2BHK in Bandra West", "rent": "₹85,000", "deposit": "₹3,00,000", "img": "https://images.unsplash.com/photo-1522708323590-d24dbb6b0267?w=400"},
    {"id": 2, "title": "Cozy 1BHK in Andheri East", "rent": "₹45,000", "deposit": "₹1,50,000", "img": "https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?w=400"}
]
for prop in properties:
    with st.container(border=True):
        col1, col2 = st.columns([1, 2])
        with col1:
            st.image(prop["img"], use_container_width=True)
        with col2:
            st.subheader(prop["title"])
            flat_details = f"Title: {prop['title']} | Rent: {prop['rent']} | Deposit: {prop['deposit']}"
            st.write(f"**Rent:** {prop['rent']} | **Deposit:** {prop['deposit']}")
            
            if st.button(f"🚀 Deploy {chosen_persona.split(' ')[0]} Here", key=f"btn_{prop['id']}"):
                with st.status(f"Deploying {chosen_persona.split(' ')[0]}..."):
                    response = run_negotiation(chosen_persona, flat_details, rules)
                
                st.success("Negotiation Complete!")
                display_text = response.replace("[DEALS_FINALIZED]", "").strip()
                with st.expander("📜 View Live Transcript", expanded=True):
                    st.markdown(display_text)
                
                pdf_bytes = generate_contract(flat_details, response)
                st.download_button("📄 Download Final Contract", data=pdf_bytes, file_name=f"Deal_{prop['id']}.pdf", mime="application/pdf", type="primary")
