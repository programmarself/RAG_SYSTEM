import streamlit as st
from langchain.text_splitter import (
    RecursiveCharacterTextSplitter,
    HTMLTextSplitter,
    MarkdownTextSplitter,
    CodeTextSplitter,
    TokenTextSplitter,
    CharacterTextSplitter,
    SemanticChunker
)

# Mapping splitter names to LangChain splitter classes and descriptions
splitter_details = {
    "Recursive Splitter": {
        "splitter_class": RecursiveCharacterTextSplitter,
        "description": "Recursively splits the data into smaller chunks, like paragraphs into sentences. Useful for processing text at different levels of granularity."
    },
    "HTML Splitter": {
        "splitter_class": HTMLTextSplitter,
        "description": "Splits data based on HTML tags, making it easier to work with structured web content, such as isolating specific sections of HTML code."
    },
    "Markdown Splitter": {
        "splitter_class": MarkdownTextSplitter,
        "description": "Splits markdown content based on headings (e.g., '# ', '## '). Useful for processing documents written in Markdown format."
    },
    "Code Splitter": {
        "splitter_class": CodeTextSplitter,
        "description": "Splits programming code into logical blocks like functions or classes. Useful for code analysis and documentation."
    },
    "Token Splitter": {
        "splitter_class": TokenTextSplitter,
        "description": "Splits data into individual tokens/words, which is often the first step in natural language processing (NLP) tasks."
    },
    "Character Splitter": {
        "splitter_class": CharacterTextSplitter,
        "description": "Splits text into individual characters. Useful for character-level analysis or encoding tasks."
    },
    "Semantic Chunker": {
        "splitter_class": SemanticChunker,
        "description": "Splits data based on semantic meaning, typically by sentences. Ensures that related information stays together."
    },
}

# Streamlit app
st.title("Dynamic Splitter Selector with LangChain")

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
    # Initialize the selected splitter class
    splitter_class = splitter_details[splitter_type]["splitter_class"]
    splitter = splitter_class()
    
    # Apply the splitter to the user input data
    split_output = splitter.split_text(user_data)
    
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
