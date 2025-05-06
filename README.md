# A Personal AI Assistant

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Required Modules](#required-modules)
- [Installation Instructions](#installation-instruction)
  - [Installing Environment](#installing_environment)
  - [Installing Libraries](#installing_libraries)
- [Execution](#execution)
- [Snaps](#snaps)
  

## Overview

# 🧠 Local AI Chatbot with Ollama + LLaMA 2

This project is a local chatbot assistant powered by [Ollama](https://ollama.com) running the **LLaMA 3** model. It's designed to operate entirely offline, giving you privacy and full control over your AI tools.

---

## 🚀 Features

- Run **LLaMA 2** locally on your machine
- Private and offline AI chatbot
- Python-based environment for easy development
- Fully open-source and customizable

---

## Required Modules

    1.langchain-community
    2.langchain-core
    3.streamlit

---

## Installation Instruction

**installing environment**

- *install [Jupyter notebook](https://jupyter.org/install)*
- *install [visual studio code](https://code.visualstudio.com/download)*
- *install [Ollama](https://ollama.com/download)*

---

**Ollama Installation**: *Ollama* is a local AI tool that lets you run large language models like LLaMA 3, Mistral, and Code LLaMA directly on your computer without needing the internet or cloud services. It provides a simple interface to download, run, and interact with powerful open-source models for tasks like chatting, coding help, writing, or building AI apps—all privately and efficiently on your own machine. 

by double clicking the .exe file download from the browser after install the ollama locally run the command on the cmd

```bash
ollama run llama2

```

## Execution

```bash
# Clone the repository
git clone [https://github.com/username/repository.git](https://github.com/Ajith-ajay/Personal-Chatbot.git)

# Navigate into the directory
cd Personal-Chatbot
```

## Set Up Python Environment

```bash
python -m venv env
# Activate the environment:

# On Windows:
.env\Scripts\activate

# On macOS/Linux:
source env/bin/activate
```

---

**installing libraries**

```bash
pip install langchain-community
```
```bash
pip install langchain-core
```
```bash
pip install streamlit
```
---


## Start the Project

```bash
#start the app
streamlit run main.py
```

---

##  Project Structure

```bash

Personal-Chatbot/
│
├── env/                # Python virtual environment (ignored in Git)
├── main.py             # Your chatbot code or integration script
├── README.md           # You're reading this!
└── .gitignore          # To exclude env/ from version control

---

## Snaps
**Index**
![Bot interface](https://github.com/user-attachments/assets/bf1e853e-42ca-455c-858e-a67e5eb78c5b)
![Bot Response](https://github.com/user-attachments/assets/ad2ed74f-24d7-461c-ac28-47009b50c2c9)


 
