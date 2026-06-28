5022CMD Advanced Algorithms - Portfolio 

## 📌 Project Overview

This repository contains the source code for the **Advanced Algorithms (5022CMD)** portfolio assignment. The project consists of three distinct Python programs designed to demonstrate the practical application of data structures, algorithm theory, and concurrent processing.

## 🚀 Projects Included

**Question 1: Pharmacy Inventory System (Hashing)** 
* A local management system designed for a pharmacy store, utilizing custom data structures for efficient data retrieval.
  * **Core Mechanism:** Implements a Hash Table utilizing Linear Probing (Open Addressing) for collision resolution.
  * **Features:** A command-line interface that allows users to insert, display, and search for pharmacy products (e.g., medicine).
  * **Performance Analysis:** Includes a built-in benchmarking tool to compare the execution time of searching records in the Hash Table versus a standard one-dimensional array.

**Question 2: Transaction Management System (Divide & Conquer)** 
* A menu-driven program that processes and organizes customer transaction data for an online shopping system.
  * **Sorting:** Utilizes **Merge Sort** to organize unsorted transaction records based on their `transactionID`.
  * **Searching:** Implements **Binary Search** to quickly locate specific transactions.
  * **Comparison:** Evaluates the performance differences between Binary Search and standard Linear Search.

**Question 3: Factorial Concurrency Analyzer** 
* A performance-testing application built to evaluate the efficiency of multithreading in Python.
  * **Operation:** Calculates the factorials of 50!, 100!, and 200!.
  * **Multithreading:** Uses separate, dedicated threads to handle each factorial calculation concurrently.
  * **Benchmarking:** Measures and compares the total processing time (in nanoseconds) between multithreaded execution and standard single-threaded execution across 10 rounds of testing.

## 💻 Technology Stack
**Language:** Python 
**Interface:** Command-Line Interface (CLI) 

## 📋 How to Run

**Requirements:** Python 3.x only. No external libraries or installation needed — the project uses the standard library exclusively.

1. Download (or clone) this repository and extract it. All files sit in a single folder.
2. Open a terminal **inside that folder** (this is required so the local module imports resolve correctly).
3. Run the entry point for the question you want to test:

   ```bash
   python Q1_Main.py    # Question 1: Pharmacy Inventory System (Hashing)
   python Q2_Main.py    # Question 2: Transaction Management System (Divide & Conquer)
   python Q3_Main.py    # Question 3: Factorial Concurrency Analyzer
   ```

4. Each program is menu-driven — follow the on-screen options to run the features and benchmarks.

> Note: run the scripts from the project root folder. The `Q*_Main.py` files import the other modules by name (e.g. `from Q1_Medicine import Medicine`), so they must stay together in the same directory.
