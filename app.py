import streamlit as st

from rag.knowledge_base import search_knowledge
from tools.helpdesk_tools import (
    get_system_status,
    create_support_ticket
)


# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="AI IT Helpdesk Agent",
    page_icon="🤖",
    layout="centered"
)


# --------------------------------------------------
# APPLICATION TITLE
# --------------------------------------------------

st.title("🤖 AI IT Helpdesk Agent")

st.write(
    "An Agentic AI-Based Technical Support System"
)


# --------------------------------------------------
# SESSION MEMORY
# --------------------------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []


# --------------------------------------------------
# DISPLAY PREVIOUS CONVERSATION
# --------------------------------------------------

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])


# --------------------------------------------------
# AI RESPONSE FUNCTION
# --------------------------------------------------

def generate_response(query):

    query_lower = query.lower()


    # --------------------------------------------------
    # SYSTEM STATUS TOOL
    # --------------------------------------------------

    if (
        "system status" in query_lower
        or "service status" in query_lower
        or "check status" in query_lower
    ):

        status = get_system_status()

        return (
            "### 🟢 System Status\n\n"
            f"**Status:** {status['status']}\n\n"
            f"**Checked at:** {status['checked_at']}\n\n"
            f"{status['message']}"
        )


    # --------------------------------------------------
    # KNOWLEDGE BASE SEARCH
    # --------------------------------------------------

    knowledge = search_knowledge(query)


    if knowledge:

        return (
            "### 🔧 Troubleshooting Guidance\n\n"
            "I found the following information related "
            "to your problem:\n\n"
            f"{knowledge}\n\n"
            "If the problem continues after following "
            "these steps, please contact your IT support team."
        )


    # --------------------------------------------------
    # SUPPORT TICKET TOOL
    # --------------------------------------------------

    if any(
        word in query_lower
        for word in [
            "ticket",
            "support",
            "help me",
            "cannot solve",
            "create ticket"
        ]
    ):

        ticket = create_support_ticket(query)

        return (
            "### 🎫 Support Ticket Created\n\n"
            f"**Ticket ID:** `{ticket['ticket_id']}`\n\n"
            f"**Issue:** {ticket['issue']}\n\n"
            f"**Status:** {ticket['status']}\n\n"
            f"{ticket['message']}"
        )


    # --------------------------------------------------
    # UNKNOWN ISSUE
    # --------------------------------------------------

    return (
        "### 🤔 I need more information\n\n"
        "I couldn't find a specific troubleshooting "
        "procedure for this issue.\n\n"
        "Please describe your problem in more detail.\n\n"
        "**You can ask about:**\n\n"
        "- 📶 Wi-Fi / Internet\n"
        "- 🔐 Login problems\n"
        "- 🐌 Slow computer\n"
        "- 💻 Application problems\n"
        "- ⌨️ Keyboard or mouse\n"
        "- 🟢 System status\n"
        "- 🎫 Support ticket"
    )


# --------------------------------------------------
# CHAT INPUT
# --------------------------------------------------

user_query = st.chat_input(
    "Describe your IT problem..."
)


# --------------------------------------------------
# PROCESS USER QUERY
# --------------------------------------------------

if user_query:

    # Store user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_query
        }
    )


    # Display user message
    with st.chat_message("user"):

        st.markdown(user_query)


    # Generate AI response
    response = generate_response(user_query)


    # Store AI response
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )


    # Display AI response
    with st.chat_message("assistant"):

        st.markdown(response)