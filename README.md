# 🤖 AI IT Helpdesk Agent

## An Agentic AI-Based Technical Support System

The AI IT Helpdesk Agent is a technical-support application designed to provide first-level assistance for common IT problems.

## Project Objective

The objective of this project is to demonstrate the use of Agentic AI concepts in an IT helpdesk environment.

The system can:

- Understand IT-related user queries
- Search a technical knowledge base
- Provide troubleshooting instructions
- Check simulated system status
- Create simulated support tickets
- Maintain conversation context

## Features

### 1. AI Helpdesk Interface

Users can describe their technical problem using natural language.

### 2. Knowledge Retrieval

The system searches the IT helpdesk knowledge base and returns relevant troubleshooting information.

### 3. Tool Calling

The system contains tools for:

- System status
- Support ticket creation

### 4. Conversation

The Streamlit interface maintains the conversation during the current session.

## Supported Issues

- Wi-Fi problems
- Internet problems
- Login issues
- Slow computer
- Application problems
- Keyboard and mouse problems
- General IT support

## Technologies

- Python
- Streamlit
- LangChain
- LangGraph
- RAG
- ChromaDB
- MCP concepts
- GitHub

## Project Structure

```text
AI-IT-Helpdesk-Agent/
│
├── app.py
├── requirements.txt
├── README.md
│
├── data/
│   └── helpdesk_knowledge.txt
│
├── tools/
│   └── helpdesk_tools.py
│
├── rag/
│   └── knowledge_base.py
│
└── screenshots/