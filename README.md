# Student Management Microservice

A console-based Python application demonstrating an independent Student Management Microservice, designed as a component of a larger system transitioning from a monolithic to a Microservices Architecture (MSA).

---

##  Project Goal

To implement a standalone microservice capable of managing student data while incorporating logging to track operations, thereby showcasing the independence and specific functionality of a single service in an MSA environment.

---

##  Microservice Functionality

This console application provides the following student management capabilities:

* **Add Students:** Register students with unique IDs, names and courses.
* **Retrieve Student Details:** Look up and display student information using a Student ID.
* **List All Students:** Display a list of all currently registered students.
* **Operation Logging:** Implements Python's `logging` module to track activities and ensure the service runs independently.

---

##  Architecture Discussion

The project includes an evaluation and discussion of key aspects related to the transition to Microservices Architecture:

* **Benefits:** Discusses the advantages of moving from a monolithic system, such as increased scalability, independence and technological diversity.
* **Key Components:** Evaluates essential components that power an MSA, ensuring scalability and independence (e.g., API Gateway, Service Discovery, Containers).

---

## How to Run

1.  Ensure you have Python installed.
2.  Execute the main program file (e.g., `student_service.py`).
    ```bash
    python student_service.py
    ```
3.  Follow the on-screen menu (options 1-4) to interact with the student data management functions.
