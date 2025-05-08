import pdfplumber
import pandas as pd

def extract_transactions_from_pdf(pdf_path):
    transactions = []

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                lines = text.split('\n')
                for line in lines:
                    if any(keyword in line for keyword in ["Paid to", "Received from", "Money sent to", "Paytm Merchant"]):
                        transactions.append(line.strip())

    return transactions

if __name__ == "__main__":
    pdf_file = "data/Paytm_UPI_Statement_06_May'23_-_07_May'25.pdf"  # Adjust filename as needed
    extracted = extract_transactions_from_pdf(pdf_file)

    for i, line in enumerate(extracted[:20], 1):  # Print first 20 lines
        print(f"{i}: {line}")
