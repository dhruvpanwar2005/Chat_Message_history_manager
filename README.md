# Chat_Message_history_manager

# 📝 Chat Manager (Python CLI)

A simple **command-line chat manager** built with Python.  
It allows users to **send, view, delete, undo, and redo messages** with timestamps, using `deque` for efficient message handling.

---

## 🚀 Features
- ✅ Send messages with timestamps  
- ✅ View chat history  
- ✅ Delete specific messages by index  
- ✅ Undo last action (send/delete)  
- ✅ Redo previously undone action  
- ✅ Interactive **menu-based CLI**  

---

## 📂 Project Structure


---

## 🛠️ Requirements
- Python 3.7+  
(No external libraries needed, only Python standard library: `time`, `collections`)

---

## ▶️ Usage

1. Clone or download the project.  
2. Run the script:

```bash
python chat_manager.py

1. Send Message
2. Show Messages
3. Delete Message
4. Undo
5. Redo
6. Exit

1. Send Message
2. Show Messages
3. Delete Message
4. Undo
5. Redo
6. Exit
Enter choice: 1
Enter message: Hello World
Sent: [2025-08-20 10:30:12] Hello World

Enter choice: 2
--- Chat History ---
0. [2025-08-20 10:30:12] Hello World
-------------------

Enter choice: 4
Undo send: [2025-08-20 10:30:12] Hello World


---
