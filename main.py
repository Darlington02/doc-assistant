from typing import Set
from backend.core import run_llm
import streamlit as st
from streamlit_chat import message

# Add custom CSS
st.markdown("""
<style>
    .main {
        background-color: #f0f2f6;
    }
    .stTextInput input {
        border-radius: 20px;
        border: 1px solid #16a34a;
        padding: 15px;
    }
    .stTextInput input:focus {
        border-color: #15803d;
        box-shadow: 0 0 0 1px #15803d;
    }
    .stSpinner > div {
        border-top-color: #16a34a !important;
    }
    /* Custom title styling */
    .custom-title {
        color: #15803d;
        font-size: 2.5rem;
        font-weight: 600;
        margin-bottom: 2rem;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

# Replace header with custom styled title
st.markdown("<h1 class='custom-title'>AI Documentation Assistant 🤖</h1>", unsafe_allow_html=True)

# Create a clean container for the chat interface
chat_container = st.container()

# Move session state initialization to top
if (
    "chat_answers_history" not in st.session_state and
    "user_prompt_history" not in st.session_state and
    "chat_history" not in st.session_state
):
    st.session_state["user_prompt_history"] = []
    st.session_state["chat_answers_history"] = []
    st.session_state["chat_history"] = []


def create_sources_string(source_urls: Set[str]) -> str:
    if not source_urls:
        return ""
    sources_list = list(source_urls)
    sources_list.sort()
    sources_string = "sources:\n"
    for i, source in enumerate(sources_list):
        sources_string += f"{i+1}, {source}\n"
    return sources_string


# Create a cleaner input area at the bottom
with st.container():
    prompt = st.text_input(
        "",  # Remove label
        placeholder="Ask me anything about the documentation...",
        key="user_input"
    )

# Process the input
if prompt:
    with st.spinner("Thinking..."):
        generated_response = run_llm(query=prompt, chat_history=st.session_state["chat_history"])
        sources = set([doc.metadata["source"] for doc in generated_response["source_documents"]])

        formatted_response = f"{generated_response['result']} \n\n {create_sources_string(sources)}"

        st.session_state["user_prompt_history"].append(prompt)
        st.session_state["chat_answers_history"].append(formatted_response)
        st.session_state["chat_history"].append(("human", prompt))
        st.session_state["chat_history"].append(("ai", generated_response["result"]))


# Display chat messages with custom styling
with chat_container:
    if st.session_state["chat_answers_history"]:
        for generated_response, user_query in zip(
            reversed(st.session_state["chat_answers_history"]), 
            reversed(st.session_state["user_prompt_history"])
        ):
            message(
                user_query,
                is_user=True,
                avatar_style="thumbs",  # You can customize avatar style
                seed="user123",  # Consistent user avatar
            )
            message(
                generated_response,
                is_user=False,
                avatar_style="bottts",  # Robot-style avatar for AI
                seed="assistant123",  # Consistent assistant avatar
            )