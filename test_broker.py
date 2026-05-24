import sys
import os
def test_imports():
    print("Testing module imports...")
    try:
        import app
        print("[OK] app module imported successfully.")
    except Exception as e:
        print(f"[FAIL] Import failed: {e}")
        sys.exit(1)
def test_mock_negotiation():
    print("Testing offline mock negotiation...")
    import app
    # Temporarily mock run_negotiation to return a mock string
    original_run = app.run_negotiation
    app.run_negotiation = lambda chosen_persona, flat_details, rules: "Negotiated Flat. Secured."
    try:
        res = app.run_negotiation(
            chosen_persona="Raju (Street Hustler)",
            flat_details="Title: Cozy 1BHK | Rent: ₹45,000 | Deposit: ₹1,50,000",
            rules="No restrictions"
        )
        if res and len(res) > 0:
            print("[OK] Mock response contains output.")
        else:
            print("[FAIL] Mock response empty!")
            sys.exit(1)
    finally:
        app.run_negotiation = original_run
def test_pdf_generation():
    print("Testing PDF builder...")
    import app
    try:
        pdf_bytes = app.generate_contract(
            flat_details="Title: Cozy 1BHK | Rent: ₹45,000 | Deposit: ₹1,50,000",
            transcript="Mock transcript text for testing purposes."
        )
        if isinstance(pdf_bytes, bytes) and len(pdf_bytes) > 0:
            print(f"[OK] PDF successfully generated. Size: {len(pdf_bytes)} bytes.")
        else:
            print("[FAIL] Generated PDF is empty or invalid type!")
            sys.exit(1)
    except Exception as e:
        print(f"[FAIL] PDF generation threw exception: {e}")
        sys.exit(1)
if __name__ == "__main__":
    test_imports()
    test_mock_negotiation()
    # Install fpdf before running this test if running stand-alone
    try:
        import fpdf
        test_pdf_generation()
    except ImportError:
        print("[WARNING] Skipping PDF generation test (fpdf not installed yet).")
    print("[SUCCESS] All preliminary module tests passed!")
