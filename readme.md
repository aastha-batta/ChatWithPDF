# ChatWithPDFs

## Overview
ChatWithPDFs is an interactive Streamlit web application that allows users to engage in a conversation with multiple PDF documents. The app extracts text from the uploaded PDFs, processes the text using a language model, and provides responses to user queries. It can also fetch additional information from the web when the answer is not found in the provided documents.

## Features
- **PDF Text Extraction**: Upload multiple PDFs and extract text for analysis.
- **Text Chunking**: Split extracted text into manageable chunks for processing.
- **Conversational Interface**: Engage in a Q&A session with the extracted content using a conversational model.
- **Web Search Integration**: Fetch additional information from the web using Tavily when the answer is not found in the documents.
- **Interactive UI**: User-friendly interface built with Streamlit.

## Technologies Used
- **Python**: Core programming language.
- **Streamlit**: Framework for creating the interactive web application.
- **PyPDF2**: Library for extracting text from PDF files.
- **Langchain**: Used for text chunking and prompt management.
- **GPT4AllEmbeddings & FAISS**: For creating vector stores from text chunks.
- **HuggingFaceHub**: For integrating large language models.
- **Tavily**: For querying the internet to fetch additional information.
- **HTML/CSS**: Custom styling for the chat interface.
  
## Install local models
GPT4All is a locally run model and downloading this model is the major pre-requisite for execution of this project. 
[Download from here](https://www.nomic.ai/gpt4all)

## Installation
1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/ChatWithPDFs.git
    cd ChatWithPDFs
    ```
2. **Create and activate a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```
3. **Install the required packages**:
    ```bash
    pip install -r chatwpdfproject.yaml
    ```

## Usage
1. **Run the Streamlit app**:
    ```bash
    streamlit run app.py
    ```
2. **Upload your PDF documents**: Use the sidebar to upload multiple PDFs.
3. **Ask questions**: Enter your question in the provided text input box and get responses based on the content of your PDFs or additional web links.

## Contributing
Contributions are welcome! Please submit a pull request or open an issue to discuss your ideas or report bugs.

