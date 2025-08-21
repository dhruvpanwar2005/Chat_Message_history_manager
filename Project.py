import time
from collections import deque

class Message:
    def __init__(self, text):
        self.text = text
        self.timestamp = time.strftime("%Y-%m-%d %H:%M:%S")

    def __repr__(self):
        return f"[{self.timestamp}] {self.text}"

class ChatManager:
    def __init__(self):
        self.messages = deque()  
        self.undo_stack = []      
        self.redo_stack = []        

    def send_message(self, text):
        msg = Message(text)
        self.messages.append(msg)
        self.undo_stack.append(("send", msg))
        self.redo_stack.clear() 
        print(f"Sent: {msg}")

    def undo(self):
        if not self.undo_stack:
            print("Nothing to undo.")
            return
        action, msg = self.undo_stack.pop()
        if action == "send":
            if msg in self.messages:
                self.messages.remove(msg)
            self.redo_stack.append(("send", msg))
            print(f"Undo send: {msg}")
        elif action == "delete":
            self.messages.append(msg)
            self.redo_stack.append(("delete", msg))
            print(f"Undo delete: {msg}")

    def redo(self):
        if not self.redo_stack:
            print("Nothing to redo.")
            return
        action, msg = self.redo_stack.pop()
        if action == "send":
            self.messages.append(msg)
            self.undo_stack.append(("send", msg))
            print(f"Redo send: {msg}")
        elif action == "delete":
            if msg in self.messages:
                self.messages.remove(msg)
            self.undo_stack.append(("delete", msg))
            print(f"Redo delete: {msg}")

    def delete_message(self, index):
        if 0 <= index < len(self.messages):
            msg = list(self.messages)[index]
            self.messages.remove(msg)
            self.undo_stack.append(("delete", msg))
            self.redo_stack.clear()
            print(f"Deleted: {msg}")
        else:
            print("Invalid message index.")

    def show_messages(self):
        if not self.messages:
            print("No messages in chat.")
            return
        print("\n--- Chat History ---")
        for i, msg in enumerate(self.messages):
            print(f"{i}. {msg}")
        print("-------------------\n")

def menu():
    chat = ChatManager()
    while True:
        print("1. Send Message")
        print("2. Show Messages")
        print("3. Delete Message")
        print("4. Undo")
        print("5. Redo")
        print("6. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            text = input("Enter message: ")
            chat.send_message(text)
        elif choice == "2":
            chat.show_messages()
        elif choice == "3":
            chat.show_messages()
            idx = int(input("Enter message index to delete: "))
            chat.delete_message(idx)
        elif choice == "4":
            chat.undo()
        elif choice == "5":
            chat.redo()
        elif choice == "6":
            print("Exiting Chat Manager.")
            break
        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    menu()
