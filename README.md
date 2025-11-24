# 🧩 SnapSign Agent  
A lightweight multi-agent system that converts short spoken or typed text into simple sign-language visuals for deaf and hard-of-hearing users.

---

## 📘 Introduction

Access to information is something most of us take for granted, but for people who are deaf or hard of hearing, digital content can be difficult to understand. Most videos, tutorials, and apps do not offer sign-language support. Professional translation is slow and expensive, which makes daily communication harder.

**SnapSign Agent** is a simple multi-agent tool that converts short phrases into basic sign-language images.  
It is not a full translator—its purpose is to help users quickly understand the *main idea* of short messages using a lightweight, modular pipeline.

---

## 🎯 Problem Statement

Many hearing-impaired users struggle with audio-based content. Captions are not always available or accurate, especially in regional languages, and creating videos for every sign is unrealistic.

**Core Problem:**  
➡️ How can we provide quick, automatic sign-language assistance for simple daily communication?

Instead of full sentence translation, this project extracts the **key word** and shows its sign-language visual instantly. This solves a small but meaningful accessibility challenge.

---

## 🤖 Why I Used Agents

Agents make the work simpler by breaking the task into small, manageable parts.

### Benefits of Using Agents
- Clear separation of responsibilities  
- Easy chaining of tasks  
- Ability to upgrade individual modules later  
- Clean and testable design  
- Lightweight, modular, and extendable

---

## 🏗️ SnapSign Agent Architecture

The system uses a **sequential multi-agent pipeline** with four main agents:

### 1️⃣ Input Agent
- Accepts text from user or speech-to-text output  
- Normalizes and cleans the input  

### 2️⃣ Keyword Agent
- Extracts the most meaningful word  
- Examples:
  - “hello there” → **hello**
  - “please help me” → **help**
  - “thank you so much” → **thank you**

### 3️⃣ Sign Agent
- Maps keywords to static sign-language images  
- Simple and lightweight (no animation generation)

### 4️⃣ Display Agent
- Shows the final sign image  
- Handles fallback when a keyword is unknown

---

## 🔄 How the System Works (Step-by-Step)

1. User enters a phrase  
2. Input Agent cleans the text  
3. Keyword Agent detects the main concept  
4. Sign Agent fetches the image  
5. Display Agent shows the visual output  

Fast, simple, and effective for short expressions.

---

## 🎥 Demo Summary

Example flow shown in demo:

1. User types **“hello there”**  
2. Pipeline runs  
3. Keyword “hello” is detected  
4. Corresponding sign image appears  
5. Display Agent outputs it cleanly  

Shows the end-to-end working of the agent system.

---

## 🛠️ Technical Implementation

This project uses concepts from the Agent Development Kit (ADK):

### ✔ Multi-Agent Pipeline  
Sequential and modular design.

### ✔ LLM-Powered Agent  
Keyword extraction uses the **Gemini model**, fulfilling the LLM requirement.

### ✔ Custom Tool  
A keyword-to-image mapping tool for sign-language visuals.

### ✔ Context Engineering  
Each agent receives only the necessary information to keep the system fast.

### ✔ Logging & Tracing  
Added to understand flow and catch issues during testing.

### ✔ GitHub Repository  
Includes agents, tools, images, and demo.

---

## 🛠️ Tools and Technologies Used

- **Python (ADK)**
- **Gemini LLM** (for keyword extraction)
- **Sequential Multi-Agent System**
- **Static Sign-Language Image Dataset**
- **GitHub** (code hosting)
- **Small UI for demo only**

---

## ⚠️ Challenges Faced

- Choosing static images vs. generated signs  
- Designing a simple but complete agent pipeline  
- Creating a clear demo  
- Limited time for expanding features  
- Learning multi-agent structuring  

Even with constraints, the system successfully delivers a helpful accessibility tool.

---

## 🚀 Future Improvements

With more time, I would add:

- Larger sign-language image library  
- Full-sentence support  
- Regional sign-language variations  
- Camera-based gesture recognition  
- YouTube browser extension  
- Better UI design  
- Speech-to-text integrated inside agents  
- Deployment using Agent Engine / Cloud Run  
- Smarter fallback for unknown keywords  

---

## 🏁 Conclusion

SnapSign Agent is a lightweight and practical accessibility project using a multi-agent architecture.  
It shows how simple agent workflows, LLM-powered modules, and custom tools can make digital communication more inclusive for deaf and hard-of-hearing users.

This project helped me understand:

- how to design multi-agent systems  
- how to integrate an LLM sub-agent  
- how to build clean pipelines  
- how to use tools and context effectively  

It is a small but meaningful step toward making digital content more accessible.

