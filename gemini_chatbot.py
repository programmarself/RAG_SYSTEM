import streamlit as st

# A dictionary of splitter descriptions or actions
splitter_info = {
    "Recursive Splitter": "A Recursive Splitter breaks down a large document into smaller chunks recursively.",
    "HTML Splitter": "HTML Splitter is used to divide HTML documents by tags, making it easier to process web content.",
    "Markdown Splitter": "Markdown Splitter segments markdown documents into smaller pieces for easier processing.",
    "Code Splitter": "Code Splitter is used to divide code files into smaller logical blocks.",
    "Token Splitter": "Token Splitter splits text into individual tokens or words for finer processing.",
    "Character Splitter": "Character Splitter divides text into individual characters, useful for very granular tasks.",
    "Semantic Chunker": "Semantic Chunker divides text based on semantic meaning, keeping related concepts together."
}

# Streamlit app
st.title("RAG System: Dynamic Splitter Information")

# User input
user_input = st.text_input("Enter a splitter name:", "Recursive Splitter")

# Normalize user input to handle case sensitivity and extra spaces
user_input = user_input.strip().title()

# Retrieve and display the relevant information
if user_input in splitter_info:
    st.subheader(f"Information about {user_input}")
    st.write(splitter_info[user_input])
else:
    st.error("Splitter type not found. Please enter a valid splitter name.")

# Optionally, display the full list of available splitters
if st.checkbox("Show all available splitters"):
    st.write("Available Splitters:")
    for splitter in splitter_info:
        st.write(f"- {splitter}")
