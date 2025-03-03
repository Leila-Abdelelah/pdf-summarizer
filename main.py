import os
import subprocess
import PyPDF2

SUMMARY_FILE = "summaries.txt"

def extract_text_from_pdf(pdf_path):
    text = ""
    try:
        with open(pdf_path, "rb") as file:
            reader = PyPDF2.PdfReader(file)
            for page in reader.pages:
                text += page.extract_text() if page.extract_text() else ""
        return text.strip()
    except Exception as e:
        print(f"Error extracting text from {pdf_path}: {e}")
        return None

def summarize_with_ollama(text, model="llama3.2"):
    try:
        result = subprocess.run(
            ["ollama", "run", model],
            input=text,
            text=True,
            capture_output=True
        )
        if result.returncode == 0:
            return result.stdout.strip() 
        else:
            print("Error:", result.stderr)
            return None
    except Exception as e:
        print("An error occurred:", e)
        return None

def process_pdfs():
    pdf_files = [f for f in os.listdir() if f.endswith(".pdf")]  #new_list = [expression for item in iterable if condition]
    
    if not pdf_files:
        print("No PDF files found in the directory.")
        return

    with open(SUMMARY_FILE, "w", encoding="utf-8") as summary_file:
        for pdf in pdf_files:
            print(f"\nProcessing {pdf}...")

            pdf_text = extract_text_from_pdf(pdf)
            if not pdf_text:
                print(f"Skipping {pdf} due to text extraction failure.")
                continue

            print("Summarizing extracted text...")
            summary = summarize_with_ollama(pdf_text)

            if summary:
                print(f"Summary for {pdf}:\n{summary}\n")
                summary_file.write(f"Summary for {pdf}:\n{summary}\n\n")
            else:
                print(f"Failed to summarize {pdf}.")

    print(f"\nSummaries saved to {SUMMARY_FILE}")

if __name__ == "__main__":
    process_pdfs()




