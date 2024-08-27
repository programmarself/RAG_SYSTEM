import streamlit as st

# Define functions for each splitter type
def recursive_splitter(data):
    # A simple example of recursive splitting, dividing by paragraphs
    return data.split('\n\n')

def html_splitter(data):
    # An example splitter that splits on HTML tags
    return data.split('<')

def markdown_splitter(data):
    # A splitter that splits based on markdown headings
    return data.split('#')

def code_splitter(data):
    # A splitter that divides by functions or classes in code (using def as a proxy here)
    return data.split('def ')

def token_splitter(data):
    # A splitter that splits text into tokens/words
    return data.split()

def character_splitter(data):
    # A splitter that divides the text by each character
    return list(data)

def semantic_chunker(data):
    # A simplistic semantic chunker that splits by sentences (periods)
    return data.split('.')

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
    - **Recursive Splitter**: Recursively splits the data into smaller chunks (e.g., paragraphs).
    - **HTML Splitter**: Splits data based on HTML tags.
    - **Markdown Splitter**: Splits markdown content based on headings.
    - **Code Splitter**: Splits code into functions or classes.
    - **Token Splitter**: Splits data into individual tokens/words.
    - **Character Splitter**: Splits data into individual characters.
    - **Semantic Chunker**: Splits data based on semantic meaning, usually by sentences.
    """)

