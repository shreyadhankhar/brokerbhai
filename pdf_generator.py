from fpdf import FPDF
def clean_text(text):
    return text.encode('ascii', 'ignore').decode('ascii')
def generate_contract(flat_details, transcript):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(200, 10, txt="BROKER-BHAI: OFFICIAL SHORTLIST", ln=True, align='C')
    pdf.ln(10)
    
    pdf.set_font("Arial", size=11)
    pdf.multi_cell(0, 7, txt=clean_text(f"Target Property: {flat_details}"))
    pdf.ln(5)
    
    clean_transcript = transcript.replace("[DEALS_FINALIZED]", "").strip()
    pdf.multi_cell(0, 7, txt=clean_text(clean_transcript))
    
    return pdf.output(dest='S').encode('latin-1')
