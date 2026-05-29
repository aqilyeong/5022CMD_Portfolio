5022CMD Advanced Algorithms - Portfolio 

## 📌 Project Overview

This repository contains the source code for the **Advanced Algorithms (5022CMD)** portfolio assignment. The project consists of three distinct Python programs designed to demonstrate the practical application of data structures, algorithm theory, and concurrent processing.

## 🚀 Projects Included

1. Pharmacy Inventory System (Hashing) 

A local management system designed for a pharmacy store, utilizing custom data structures for efficient data retrieval.

**Core Mechanism:** Implements a Hash Table utilizing Linear Probing (Open Addressing) for collision resolution.
**Features:** A command-line interface that allows users to insert, display, and search for pharmacy products (e.g., medicine).
**Performance Analysis:** Includes a built-in benchmarking tool to compare the execution time of searching records in the Hash Table versus a standard one-dimensional array.



2. Transaction Management System (Divide & Conquer) 
* A menu-driven program that processes and organizes customer transaction data for an online shopping system.

**Sorting:** Utilizes **Merge Sort** to organize unsorted transaction records based on their `transactionID`.
**Searching:** Implements **Binary Search** to quickly locate specific transactions.
**Comparison:** Evaluates the performance differences between Binary Search and standard Linear Search.



3. Factorial Concurrency Analyzer 
* A performance-testing application built to evaluate the efficiency of multithreading in Python.

**Operation:** Calculates the factorials of 50!, 100!, and 200!.
**Multithreading:** Uses separate, dedicated threads to handle each factorial calculation concurrently.
**Benchmarking:** Measures and compares the total processing time (in nanoseconds) between multithreaded execution and standard single-threaded execution across 10 rounds of testing.



## 💻 Technology Stack
**Language:** Python 
**Interface:** Command-Line Interface (CLI) 



## 📋 How to Run

1. Clone this repository to your local machine.
2. Navigate to the directory of the specific program you wish to test (e.g., `Question 1`, `Question 2`, or `Question 3`).
3. Execute the Python scripts via your terminal:
```bash
python main.py

```


*(Note: Update `main.py` to the actual filename used in your project).*
