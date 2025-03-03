# pdf-summarizer

This project automates the summarization of PDF documents using artificial intelligence models. It compares the performance of Ollama's Llama 3.2 (local model) and ChatGPT (cloud-based model) by generating summaries and evaluating their effectiveness.

Features:
  - Extracts text from multiple PDF files.
  - Generates summaries using Ollama (Llama 3.2).
  - Compares results with manually written ChatGPT summaries.
  - Analyzes performance in terms of accuracy, conciseness, and readability


# 1. Installing Ollama and Setting Up the Environment

First, I installed Ollama, which is required to run the Llama 3.2 model locally.
Downloaded and installed Llama 3.2 by running:
  ollama pull llama3.2

I verified that the installation was successful by checking:
  ollama list

This displayed available models, including Llama 3.2.


# 2. Setting Up Python and Dependencies

Created a Python virtual environment to manage dependencies:
  python3 -m venv myenv
  source myenv/bin/activate

Installed required Python packages:
  pip install -r requirements.txt


# 3. Extracting Text from PDFs

I used PyPDF2 to extract text from multiple PDFs stored in the working directory.
Implemented a function in main.py to process all PDFs
Extracted full text from PDFs and stored it in memory for processing.


# 4. Summarizing Text Using Ollama (Llama 3.2)

I used Ollama CLI to generate summaries of extracted text. The created function sent the extracted text to Llama 3.2, and the summarized output was stored in summaries.txt.


# 5. Generating ChatGPT Summaries for Comparison

To compare results, I manually summarized the same PDF texts using ChatGPT.
Stored both Ollama summaries and ChatGPT summaries for evaluation.


# 6. Comparing and Evaluating Summaries

I compared the summaries using these criteria:
  - Is the summary compact and informative?
  - Does the summary retain essential information?
  - Is the summary structured and easy to understand?


# 8. Conclusion

Ollama was better for concise, direct summaries where quick understanding was required. ChatGPT excelled in detailed, structured summaries, particularly for complex topics. The comparison between models helped analyze their effectiveness in different contexts.
