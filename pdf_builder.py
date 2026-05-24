from fpdf import FPDF
import re
def clean_text(text):
    # Viciously remove everything that isn't standard text
    return text.encode('ascii', 'ignore').decode('ascii')
def generate_contract(location, rent, deposit, transcript):
def generate_contract(flat_details, transcript):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', 16)
    # NO EMOJIS HERE
    pdf.cell(200, 10, txt="BROKER-BHAI: OFFICIAL SHORTLIST", ln=True, align='C')
    pdf.ln(10)
    
    pdf.set_font("Arial", size=11)
    pdf.cell(200, 10, txt=f"Location: {clean_text(location)} | Rent: {rent} | Deposit: {deposit}", ln=True)
    pdf.multi_cell(0, 7, txt=clean_text(f"Target Property: {flat_details}"))
    pdf.ln(5)
    
    clean_transcript = transcript.replace("[DEALS_FINALIZED]", "").strip()
    pdf.multi_cell(0, 7, txt=clean_text(clean_transcript))
    
    return pdf.output(dest='S').encode('latin-1')
