import streamlit as st
from recomendation import recommendation

st.title("SetelahLulus Chatbot")

# Sidebar
with st.sidebar:
    
    new_chat_button = st.button("New Chat", type="primary")
    
    # it will to reset session
    if new_chat_button:
        if len(st.session_state.messages) > 1:
            st.session_state.messages = [st.session_state.messages[0]]


if __name__ == "__main__":
    st.markdown(
    """
<style>
    .st-emotion-cache-janbn0 {
        flex-direction: row-reverse;
        text-align: right;
    }
</style>
""",
    unsafe_allow_html=True,
)
    recommendation()