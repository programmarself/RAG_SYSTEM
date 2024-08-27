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

# Mapping splitter names to functions
splitter_functions = {
    "Recursive Splitter": recursive_splitter,
    "HTML Splitter": html_splitter,
    "Markdown Splitter": markdown_splitter,
    "Code Splitter": code_splitter,
    "Token Splitter": token_splitter,
    "Character Splitter": character_splitter,
    "Semantic Chunker": semantic_chunker,
}

# Streamlit app
st.title("Dynamic Splitter Selector")

# User input for data
user_data = st.text_area("Enter the data you want to split:", "This is a sample text. Enter your data here...")

# User selects the splitter type
splitter_type = st.selectbox(
    "Choose a splitter type:",
    list(splitter_functions.keys())
)

# Button to perform the splitting
if st.button("Split Data"):
    # Retrieve the selected splitter function
    splitter_function = splitter_functions[splitter_type]
    
    # Apply the splitter function to the user input data
    split_output = splitter_function(user_data)
    
    # Display the output
    st.subheader(f"Output using {splitter_type}")
    for idx, part in enumerate(split_output):
        st.write(f"Part {idx + 1}:")
        st.write(part)

# Optionally, display information about each splitter
if st.checkbox("Show information about each splitter type"):
    st.write("""
    - **Recursive Splitter**: Recursively splits the data into smaller chunks, like paragraphs into sentences.
    - **HTML Splitter**: Splits data based on HTML tags.
    - **Markdown Splitter**: Splits markdown content based on headings.
    - **Code Splitter**: Splits code into functions or classes.
    - **Token Splitter**: Splits data into individual tokens/words.
    - **Character Splitter**: Splits data into individual characters.
    - **Semantic Chunker**: Splits data based on semantic meaning, typically by sentences.
    """)
