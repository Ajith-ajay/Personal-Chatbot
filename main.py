import streamlit as st
from datetime import datetime
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama

# ---- Page Config ----
st.set_page_config(
    page_title="Ajay's Assistant ",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---- Custom Styling ----
st.markdown("""
    <style>
    .stApp {
        background-color: #000000;
        color: white;
    }
    .stTextInput > div > div > input {
        background-color: #111111 !important;
        color: white !important;
        border: 1px solid #333333;
    }
    .stButton>button {
        background-color: #222222;
        color: white;
        border: 1px solid #444444;
        border-radius: 5px;
        padding: 0.5em 1em;
    }
    .stButton>button:hover {
        background-color: #333333;
    }
    .user-message {
        background-color: #222222;
        padding: 1rem;
        border-left: 5px solid #555;
        border-radius: 10px;
        margin-bottom: 1rem;
        margin-left: 20%;
    }
    .bot-message {
        background-color: #111111;
        padding: 1rem;
        border-right: 5px solid #777;
        border-radius: 10px;
        margin-bottom: 1rem;
        margin-right: 20%;
    }
    .typing-indicator {
        display: flex;
        gap: 5px;
    }
    .typing-dot {
        height: 10px;
        width: 10px;
        background-color: #888;
        border-radius: 50%;
        animation: typing 1s infinite ease-in-out;
    }
    .typing-dot:nth-child(1) { animation-delay: 0s; }
    .typing-dot:nth-child(2) { animation-delay: 0.2s; }
    .typing-dot:nth-child(3) { animation-delay: 0.4s; }

    @keyframes typing {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-5px); }
    }
    </style>
""", unsafe_allow_html=True)

# ---- LangChain & Ollama Setup ----
llm = Ollama(model="llama2")
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful AI assistant. Your name is Ajay's Assistant."),
    ("user", "User query: {query}")
])
chain = prompt | llm | StrOutputParser()

# ---- Session State ----
if "messages" not in st.session_state:
    st.session_state.messages = []

if "thinking" not in st.session_state:
    st.session_state.thinking = False

# ---- Header ----
col1, col2 = st.columns([1, 5])
with col1:
    st.image("https://cdn-icons-png.flaticon.com/512/4712/4712035.png", width=80)
with col2:
    st.title("Ajay's Personal Chatbot 🤖")
    st.caption("Locally Powered by LLaMA2 + LangChain")

# ---- Display Chat History ----
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f'<div class="user-message">🧑‍💻 {msg["content"]}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="bot-message">🤖 {msg["content"]}</div>', unsafe_allow_html=True)

# ---- Typing Indicator ----
if st.session_state.thinking:
    st.markdown("""
        <div class="bot-message">
            <div class="typing-indicator">
                <div class="typing-dot"></div>
                <div class="typing-dot"></div>
                <div class="typing-dot"></div>
            </div>
        </div>
    """, unsafe_allow_html=True)

# ---- Chat Input ----
user_input = st.chat_input("Type your message...")

if user_input:
    # Append user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    st.session_state.thinking = True
    st.rerun()

# ---- Process Bot Response ----
if st.session_state.thinking:
    query = st.session_state.messages[-1]["content"]
    with st.spinner("Ajay's Assistant is thinking..."):
        response = chain.invoke({"query": query})
    st.session_state.messages.append({"role": "assistant", "content": response})
    st.session_state.thinking = False
    st.rerun()

# ---- Footer ----
st.markdown("---")
st.caption(f"© {datetime.now().year} Ajay's Assistant | Local Chatbot | Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
