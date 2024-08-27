import streamlit as st
import re

# Define the split functions
def recursive_splitter(data):
    paragraphs = data.split('\n\n')
    sentences = [sentence for para in paragraphs for sentence in para.split('.')]
    return [sentence.strip() + '.' for sentence in sentences if sentence.strip()]

def html_splitter(data):
    parts = re.split(r'(<[^>]+>)', data)
    return [part for part in parts if part.strip()]

def markdown_splitter(data):
    parts = re.split(r'(^#{1,6} .*$)', data, flags=re.MULTILINE)
    return [part.strip() for part in parts if part.strip()]

def code_splitter(data):
    parts = re.split(r'(?m)^def ', data)
    return [f'def {part.strip()}' if idx > 0 else part.strip() for idx, part in enumerate(parts) if part.strip()]

def token_splitter(data):
    tokens = re.findall(r'\b\w+\b', data)
    return tokens

def character_splitter(data):
    return list(data)

def semantic_chunker(data):
    sentences = re.split(r'(?<=\.)\s+', data)
    return [sentence.strip() for sentence in sentences if sentence.strip()]

# Mapping splitter names to functions and descriptions
splitter_details = {
    "Recursive Splitter": {
        "function": recursive_splitter,
        "description": "Recursively splits the data into smaller chunks, like paragraphs into sentences. Useful for processing text at different levels of granularity."
    },
    "HTML Splitter": {
        "function": html_splitter,
        "description": "Splits data based on HTML tags, making it easier to work with structured web content, such as isolating specific sections of HTML code."
    },
    "Markdown Splitter": {
        "function": markdown_splitter,
        "description": "Splits markdown content based on headings (e.g., '# ', '## '). Useful for processing documents written in Markdown format."
    },
    "Code Splitter": {
        "function": code_splitter,
        "description": "Splits programming code into logical blocks like functions or classes. Useful for code analysis and documentation."
    },
    "Token Splitter": {
        "function": token_splitter,
        "description": "Splits data into individual tokens/words, which is often the first step in natural language processing (NLP) tasks."
    },
    "Character Splitter": {
        "function": character_splitter,
        "description": "Splits text into individual characters. Useful for character-level analysis or encoding tasks."
    },
    "Semantic Chunker": {
        "function": semantic_chunker,
        "description": "Splits data based on semantic meaning, typically by sentences. Ensures that related information stays together."
    },
}

# Streamlit app
st.sidebar.title("Splitter Settings")
st.sidebar.subheader("Data Input")
user_data = st.sidebar.text_area("Enter the data you want to split:", "This is a sample text. Enter your data here...")

st.sidebar.subheader("Splitter Type")
splitter_type = st.sidebar.selectbox(
    "Choose a splitter type:",
    list(splitter_details.keys())
)

st.sidebar.subheader("Options")
show_info = st.sidebar.checkbox("Show information about all splitter types")

st.title("RAG Splitter System")
st.markdown('<p class="title">Developed By: Irfan Ullah Khan</p>', unsafe_allow_html=True)

# Processing
if st.button("Split Data"):
    with st.spinner('Processing data...'):
        splitter_function = splitter_details[splitter_type]["function"]
        split_output = splitter_function(user_data)
        
        if split_output:
            st.subheader(f"Output using {splitter_type}")
            for idx, part in enumerate(split_output):
                with st.expander(f"Part {idx + 1}"):
                    st.write(part)

if show_info:
    for name, details in splitter_details.items():
        st.subheader(name)
        st.write(details["description"])

uploaded_file = st.file_uploader("Upload a file", type=["txt", "md", "html", "py"])
if uploaded_file is not None:
    user_data = uploaded_file.read().decode("utf-8")
    st.text_area("File content:", user_data, height=300)
