# 📝 Simple CLI To-Do List Application

A basic command-line To-Do List application written in Python. It allows users to:

- View current tasks
- Add new tasks
- Mark tasks as completed
- Remove tasks
- Exit the application

This is a beginner-friendly project for those learning Python or looking to build simple CLI-based tools.

---

## 🚀 Features

- Minimal, menu-driven interface
- Simple task tracking with completion status
- Console-based interaction (no external dependencies)

---

## 💻 Getting Started

### 🔧 Prerequisites

Make sure you have **Python 3.x** installed.

Check your version with:

bash
python --version

📂 File Structure
todo-cli-app/
│
├── todo.py         # Main application script
└── README.md       # Documentation


📥 Installation
1. Clone this repository:
  git clone https://github.com/YOUR_USERNAME/todo-cli-app.git
  cd todo-cli-app

2. Run the script:
   python todo.py
   
📸 Demo

--- To-Do List Menu ---
1. View To-Do List
2. Add Task
3. Mark Task as Complete
4. Remove Task
5. Exit
-----------------------
Enter your choice (1-5): 1

Your to-do list is empty!

--- To-Do List Menu ---
1. View To-Do List
2. Add Task
3. Mark Task as Complete
4. Remove Task
5. Exit
-----------------------
Enter your choice (1-5): 2
Enter the task to add: Remind me to complete the build of AI Agent
Task 'Remind me to complete the build of AI Agent' added successfully!

--- To-Do List Menu ---
1. View To-Do List
2. Add Task
3. Mark Task as Complete
4. Remove Task
5. Exit
-----------------------
Enter your choice (1-5): 2
Enter the task to add: Complete 3 projects of API's
Task 'Complete 3 projects of API's' added successfully!

--- To-Do List Menu ---
1. View To-Do List
2. Add Task
3. Mark Task as Complete
4. Remove Task
5. Exit
-----------------------
Enter your choice (1-5): 2
Enter the task to add: Remind me to meditate4
Task 'Remind me to meditate4' added successfully!

--- To-Do List Menu ---
1. View To-Do List
2. Add Task
3. Mark Task as Complete
4. Remove Task
5. Exit
-----------------------
Enter your choice (1-5): 1

--- Your To-Do List ---
1. [ ] Remind me to complete the build of AI Agent
2. [ ] Complete 3 projects of API's
3. [ ] Remind me to meditate4
-----------------------

--- To-Do List Menu ---
1. View To-Do List
2. Add Task
3. Mark Task as Complete
4. Remove Task
5. Exit
-----------------------
Enter your choice (1-5): 3

--- Your To-Do List ---
1. [ ] Remind me to complete the build of AI Agent
2. [ ] Complete 3 projects of API's
3. [ ] Remind me to meditate4
-----------------------
Enter the number of the task to mark as complete: 1, 3
Invalid input. Please enter a number.

--- To-Do List Menu ---
1. View To-Do List
2. Add Task
3. Mark Task as Complete
4. Remove Task
5. Exit
-----------------------
Enter your choice (1-5): 3  

--- Your To-Do List ---
1. [ ] Remind me to complete the build of AI Agent
2. [ ] Complete 3 projects of API's
3. [ ] Remind me to meditate4
-----------------------
Enter the number of the task to mark as complete: 1
Task 'Remind me to complete the build of AI Agent' marked as complete!

--- To-Do List Menu ---
1. View To-Do List
2. Add Task
3. Mark Task as Complete
4. Remove Task
5. Exit
-----------------------
Enter your choice (1-5): 1

--- Your To-Do List ---
1. [✓] Remind me to complete the build of AI Agent
2. [ ] Complete 3 projects of API's
3. [ ] Remind me to meditate4
-----------------------

--- To-Do List Menu ---
1. View To-Do List
2. Add Task
3. Mark Task as Complete
4. Remove Task
5. Exit
-----------------------
Enter your choice (1-5): 4

--- Your To-Do List ---
1. [✓] Remind me to complete the build of AI Agent
2. [ ] Complete 3 projects of API's
3. [ ] Remind me to meditate4
-----------------------
Enter the number of the task to remove: 3
Task 'Remind me to meditate4' removed successfully!

--- To-Do List Menu ---
1. View To-Do List
2. Add Task
3. Mark Task as Complete
4. Remove Task
5. Exit
-----------------------
Enter your choice (1-5): 1

--- Your To-Do List ---
1. [✓] Remind me to complete the build of AI Agent
2. [ ] Complete 3 projects of API's
-----------------------

--- To-Do List Menu ---
1. View To-Do List
2. Add Task
3. Mark Task as Complete
4. Remove Task
5. Exit
-----------------------
Enter your choice (1-5): 5
Exiting to-do list application. Goodbye!

🤝 Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you'd like to change.

📜 License
This project is open-source and available under the MIT License.

🙋‍♂️ Author
Thoshan Naik R S

GitHub: @thoshanrs10
