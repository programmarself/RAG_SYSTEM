import streamlit as st
import re

# Improved functions for each splitter type
def recursive_splitter(data):
    # This example will recursively split paragraphs into sentences
    paragraphs = data.split('\n\n')
    sentences = [sentence for para in paragraphs for sentence in para.split('.')]
    return [sentence.strip() + '.' for sentence in sentences if sentence.strip()]

def html_splitter(data):
    # Splits on HTML tags, keeping the tags as part of the output
    parts = re.split(r'(<[^>]+>)', data)
    return [part for part in parts if part.strip()]

def markdown_splitter(data):
    # Splits on Markdown headings (e.g., '# ', '## ', etc.)
    parts = re.split(r'(^#{1,6} .*$)', data, flags=re.MULTILINE)
    return [part.strip() for part in parts if part.strip()]

def code_splitter(data):
    # Simple splitter based on function definitions in Python code
    parts = re.split(r'(?m)^def ', data)
    return [f'def {part.strip()}' if idx > 0 else part.strip() for idx, part in enumerate(parts) if part.strip()]

def token_splitter(data):
    # Splits text into tokens/words, handling punctuation
    tokens = re.findall(r'\b\w+\b', data)
    return tokens

def character_splitter(data):
    # Splits the text into individual characters
    return list(data)

def semantic_chunker(data):
    # Splits based on sentences, assuming sentences end with a period
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
st.title("RAG Splitter System")
Developed By :Irfan Ullah Khan

# User input for data
user_data = st.text_area("Enter the data you want to split:", "This is a sample text. Enter your data here...")

# User selects the splitter type
splitter_type = st.selectbox(
    "Choose a splitter type:",
    list(splitter_details.keys())
)

# Display the selected splitter's description
st.subheader(f"About {splitter_type}")
st.write(splitter_details[splitter_type]["description"])

# Button to perform the splitting
if st.button("Split Data"):
    # Retrieve the selected splitter function
    splitter_function = splitter_details[splitter_type]["function"]
    
    # Apply the splitter function to the user input data
    split_output = splitter_function(user_data)
    
    # Display the output
    st.subheader(f"Output using {splitter_type}")
    for idx, part in enumerate(split_output):
        st.write(f"Part {idx + 1}:")
        st.write(part)

# Optionally, display information about each splitter
if st.checkbox("Show information about all splitter types"):
    for name, details in splitter_details.items():
        st.subheader(name)
        st.write(details["description"])
