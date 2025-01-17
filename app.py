# import streamlit as st
# import google.generativeai as genai
# from PyPDF2 import PdfReader

# # Configure Google Generative AI
# genai.configure(api_key="AIzaSyCm4CJZBMPW-Klw5dlYFSzyTW97BSvM7Jg")
# model = genai.GenerativeModel("gemini-1.5-flash")

# # Hardcoded PDF Paths
# PDF_PATHS = {
#     "Document 1": "db\CMVR-chapter2.pdf",
    
# }

# # Extract Text from Hardcoded PDFs
# def extract_text_from_pdfs(pdf_paths):
#     pdf_content = {}
#     for name, path in pdf_paths.items():
#         try:
#             reader = PdfReader(path)
#             text = ""
#             for page in reader.pages:
#                 text += page.extract_text()
#             pdf_content[name] = text
#         except Exception as e:
#             pdf_content[name] = f"Error reading PDF: {e}"
#     return pdf_content

# # Process User Query
# def process_query(pdf_content, query):
#     combined_content = "\n\n".join([f"{name}:\n{text}" for name, text in pdf_content.items()])
#     prompt = f"Use the following documents to answer accurately:\n\n{combined_content}\n\nUser Query: {query}"
    
#     response = model.generate_content(prompt)
#     return response.text

# # Streamlit UI
# st.title("आरटीओ मदत")
# st.subheader("Ask questions")

# # Load Hardcoded PDFs
# with st.spinner("Loading "):
#     pdf_content = extract_text_from_pdfs(PDF_PATHS)
# #st.success("Now You can Ask Questions")

# # Query Input Section
# query = st.text_input("Ask a question:")
# if st.button("Submit"):
#     if query:
#         with st.spinner("Processing your query..."):
#             response = process_query(pdf_content, query)
#         st.write("### Chatbot Response:")
#         st.write(response)
#     else:
#         st.warning("Please enter a question.")

# # Footer
# st.markdown("---")
# st.markdown("RTOMadat")


import streamlit as st
import google.generativeai as genai
from PyPDF2 import PdfReader

# Configure Google Generative AI
genai.configure(api_key="AIzaSyCm4CJZBMPW-Klw5dlYFSzyTW97BSvM7Jg")
model = genai.GenerativeModel("gemini-1.5-flash")

# Hardcoded PDF Paths
PDF_PATHS = {
    "Document 1": "CMVR-chapter2.pdf",
}

# Extract Text from Hardcoded PDFs
def extract_text_from_pdfs(pdf_paths):
    pdf_content = {}
    for name, path in pdf_paths.items():
        try:
            reader = PdfReader(path)
            text = ""
            for page in reader.pages:
                text += page.extract_text()
            pdf_content[name] = text
        except Exception as e:
            pdf_content[name] = f"Error reading PDF: {e}"
    return pdf_content

# Process User Query
def process_query(pdf_content, query):
    combined_content = "\n\n".join([f"{name}:\n{text}" for name, text in pdf_content.items()])
    prompt = f"Use the following documents to answer accurately:\n\n{combined_content}\n\nUser Query: {query}"
    
    response = model.generate_content(prompt)
    return response.text

# Custom CSS for improved aesthetics
def add_custom_css():
    st.markdown(
        """
        <style>
       body {
    background-color: #f0f0f0; /* Lighter background for better readability */
    font-family: 'Open Sans', sans-serif; /* Modern and clean font */
    color: #444; /* Text color */
}

.stApp {
    background-color: #fff;
    border: 1px solid #ddd;
    border-radius: 15px; /* Slightly more rounded corners */
    padding: 30px;
    max-width: 800px;
    margin: auto;
    box-shadow: 0px 5px 10px rgba(0, 0, 0, 0.1);
}

h1 {
    color: #673ab7; /* Deeper purple for better contrast */
    font-size: 2.5rem;
    margin-bottom: 20px;
}

h2, h3, h4 {
    color: #3f51b5; /* Slightly darker blue */
    margin-bottom: 15px;
}

.css-1avcm0n textarea {
    border: 1px solid #3f51b5;
    border-radius: 8px;
    padding: 10px;
    font-size: 1rem;
    resize: vertical; /* Allow vertical resizing */
}

.stButton button {
    background-color: #673ab7 !important;
    color: white !important;
    border-radius: 8px !important;
    padding: 12px 25px !important;
    font-weight: 600; /* Slightly bolder button text */
    transition: background-color 0.2s ease-in-out; /* Add hover effect */
}

.stButton button:hover {
    background-color: #512da8 !important; /* Darker color on hover */
}
        </style>
        """,
        unsafe_allow_html=True,
    )

# Main Streamlit App
add_custom_css()
st.markdown("<h1 style='text-align: center;'>RTO Helpdesk  </h1>", unsafe_allow_html=True)
st.markdown(
    "<h3 style='text-align: center; color: #4a75f5;'>Ask questions Related to RTO </h3>",
    unsafe_allow_html=True,
)

# Load Hardcoded PDFs
with st.spinner("Loading documents..."):
    pdf_content = extract_text_from_pdfs(PDF_PATHS)
st.success("Ready!")

# Query Input Section
st.markdown("---")
st.markdown("<h2 style='color: #4a75f5;'>🤖 Ask Your Question</h2>", unsafe_allow_html=True)
query = st.text_input("Enter your query below:", placeholder="Type your question here...")

if st.button("Submit"):
    if query:
        with st.spinner("Processing your query..."):
            response = process_query(pdf_content, query)
        st.markdown("<h3 style='color: #4a75f5;'>Chatbot Response:</h3>", unsafe_allow_html=True)
        st.write(response)
    else:
        st.warning("Please enter a question.")

# Footer
# st.markdown("---")
# st.markdown(
#     "<p style='text-align: center; font-size: 14px; color: #888;'>RTO</p>",
#     unsafe_allow_html=True,
# )
