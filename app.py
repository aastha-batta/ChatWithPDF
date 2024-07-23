import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.embeddings import GPT4AllEmbeddings
from langchain_community.vectorstores import faiss
from langchain.prompts import PromptTemplate
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from htmltemp import css, bot_template

from langchain_community.llms import HuggingFaceHub
import tavily 

# Custom template for guiding the LLM model
custom_template = """
You are an AI assistant. Answer the question strictly based on the provided documents. If the answer is not found in the documents, respond with "The answer is not found in the provided documents."

Question: {question}
"""

CUSTOM_QUESTION_PROMPT = PromptTemplate.from_template(custom_template)

# Function to extract text from PDF documents
def extract_pdf_text(documents):
    text = ""
    for pdf in documents:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

# Function to split text into chunks
def split_text_into_chunks(raw_text):
    text_splitter = CharacterTextSplitter(
        separator="\n", chunk_size=1000, chunk_overlap=200, length_function=len
    )
    chunks = text_splitter.split_text(raw_text)
    return chunks

# Function to create a vectorstore using GPT4AllEmbeddings and FAISS
def create_vectorstore(text_chunks):
    embeddings = GPT4AllEmbeddings()  # Using GPT4AllEmbeddings
    vectorstore = faiss.FAISS.from_texts(texts=text_chunks, embedding=embeddings)
    return vectorstore

# Function to create a conversation chain
def create_conversation_chain(vectorstore):
    llm = HuggingFaceHub(
        repo_id="mistralai/Mistral-7B-Instruct-v0.2",  # Replace with your desired LLM
        task="text-generation",
        huggingfacehub_api_token="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",
        model_kwargs={
            "max_new_tokens": 512,
            "top_k": 30,
            "temperature": 0.1,
            "repetition_penalty": 1.03,
        },
    )
    memory = ConversationBufferMemory(
        memory_key="chat_history", return_messages=True, output_key="answer"
    )  # Using conversation buffer memory
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        condense_question_prompt=CUSTOM_QUESTION_PROMPT,
        memory=memory,
    )
    return conversation_chain

# Function to query the internet for additional information using Tavily
def query_internet_with_tavily(question, api_key):
    client = tavily.TavilyClient(api_key="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")
    results = client.search(query=question)
    urls = [result['url'] for result in results['results']]
    return urls

# Function to handle user questions and display responses
def handle_user_question(question):
    response = st.session_state.conversation({"question": question})
    answer = response["answer"]
    st.session_state.chat_history = response["chat_history"]
    
    # Display the answer
    st.write(bot_template.replace("{{MSG}}", answer), unsafe_allow_html=True)
    
    # Check if the response indicates that the answer is not found in the documents
    if "The answer is not found in the provided documents." in answer:
        api_key = st.secrets["TAVILY_API_KEY"]  # Ensure your Tavily API key is stored in Streamlit secrets
        links = query_internet_with_tavily(question, api_key)
        if links:
            st.write("Here are some links that might be useful:")
            for link in links:
                st.markdown(f"- [{link}]({link})", unsafe_allow_html=True)

def main():
    load_dotenv()
    st.set_page_config(page_title="Chat with Multiple PDFs", page_icon=":books:")
    st.write(css, unsafe_allow_html=True)

    if "conversation" not in st.session_state:
        st.session_state.conversation = None

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None

    st.header("ChatWithPDFs :book:")
    question = st.text_input("Ask a question from your document:")

    if question:
        handle_user_question(question)

    with st.sidebar:
        st.subheader("Your Documents")
        documents = st.file_uploader(
            "Upload your PDF here and click on 'Process'", accept_multiple_files=True
        )
        if st.button("Process"):
            with st.spinner("Processing"):
                # Get the PDF text
                raw_text = extract_pdf_text(documents)

                # Split text into chunks
                text_chunks = split_text_into_chunks(raw_text)

                # Create vectorstore
                vectorstore = create_vectorstore(text_chunks)

                # Create conversation chain
                st.session_state.conversation = create_conversation_chain(vectorstore)

if __name__ == "__main__":
    main()
