
# Student Enrollment System

## Overview
The **Student Enrollment System** is a Python-based project designed to streamline the process of course management and student enrollments. The system implements an MVC architecture, offering functionalities for administrators to manage courses and students, and for students to enroll in courses.

---

## Features
- Admin functionalities:
  - Add and manage courses.
  - Manage student details.
- Student functionalities:
  - Enroll in courses.
  - View enrolled courses.
- Course management:
  - Track enrolled students.
  - Manage course details.
- Secure login system for administrators and students.

---

## System Architecture
The project follows the **Model-View-Controller (MVC)** architecture:
- **Model**: Represents the application's data (e.g., Student, Course, Enrollment).
- **View**: Displays data to the user (CLI-based in this project).
- **Controller**: Handles user input and updates the model and view.

---

## Installation Instructions
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/raveenjk/student-enrollment-system.git
   cd student-enrollment-system
   ```

2. **Set Up the Environment**:
   - Ensure Python 3.x is installed on your system.
   - Install dependencies (if any):
     ```bash
     pip install -r requirements.txt
     ```

3. **Run the Program**:
   ```bash
   python main.py
   ```

---

## Directory Structure
```
student-enrollment-system/
│
├── models/
│   ├── admin.py
│   ├── student.py
│   ├── course.py
│   ├── enrollment.py
│
├── controllers/
│   ├── admin_controller.py
│   ├── student_controller.py
│   ├── course_controller.py
│
├── views/
│   ├── admin_view.py
│   ├── student_view.py
│
├── main.py
├── requirements.txt
└── README.md
```

---

## Usage Instructions
1. **For Admin**:
   - Log in with admin credentials.
   - Manage courses and students.
2. **For Students**:
   - Log in with student credentials.
   - Enroll in available courses.
   - View your enrolled courses.

---

## Technologies Used
- **Programming Language**: Python
- **Architecture**: MVC (Model-View-Controller)
- **Database**: In-memory data structures (can be extended to use a database like SQLite or PostgreSQL)

---

## Future Enhancements
- Add a web-based interface using Django or Flask.
- Implement a payment gateway for course enrollments.
- Introduce reporting features for admin users.
- Enhance the login system with encryption and session handling.

---

## Contributing
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b development
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add feature name"
   ```
4. Push to the branch:
   ```bash
   git push origin development
   ```
5. Create a pull request.

---
List of contributors:
- raveenjk
- pubudusanka
- SahanHansaja
- clasindu
- rashmishehara
- HemanthaNevil
- Shashinipulsara
- Pasindupg
- AdithyaRusith
