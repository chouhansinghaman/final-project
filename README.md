# Credit Card Fraud Detector

#### Video Demo: <https://www.youtube.com/watch?v=0oGjd5Oacks>

#### Description:

This Python-based project is designed to analyze credit card transactions and identify potentially fraudulent activity using a pre-labeled dataset. The dataset used is the popular "Credit Card Fraud Detection" dataset available on Kaggle, which contains anonymized credit card transactions made by European cardholders in September 2013. It consists of 284,807 transactions, each with 30 features (labeled V1 through V28), along with the transaction amount, time, and a binary class label indicating whether the transaction was fraudulent (`Class = 1`) or legitimate (`Class = 0`).

The core goal of this project is to demonstrate a basic but functional fraud detection pipeline using Python’s data handling capabilities via the `pandas` library. The project reads and processes the dataset, flags fraudulent transactions, saves them to a new file, and displays important summary statistics.

---

### Features:

- Loads a large dataset (280,000+ transactions) efficiently.
- Filters and identifies all transactions labeled as fraudulent (`Class == 1`).
- Outputs a new CSV file (`flagged.csv`) containing only the flagged fraud transactions.
- Calculates and prints useful summary statistics such as:
  - Total number of transactions.
  - Total number of fraud cases.
  - Fraud rate as a percentage.
- Paginated display of flagged transactions using a customizable page size.
- Includes five unit tests written using `pytest` to ensure the functionality and accuracy of the key components.

---

### Files:

- `project.py`: Contains all the main logic of the program, including:
  - `main()`: The entry point that handles user interaction and ties all functionality together.
  - `detect_fraud(data)`: Filters the dataset to return only transactions labeled as fraudulent.
  - `save_flagged_transactions(data, output_file)`: Saves the filtered fraud data into a separate CSV file.
  - `summarize_data(data)`: Prints key metrics about the dataset, including fraud statistics.
  - `display_flagged_file(file_path, page_size)`: Allows viewing the flagged transactions in a paginated format.

- `test_project.py`: Contains five test functions that validate the behavior of the main project functions:
  - Ensures the fraud detection logic correctly identifies transactions.
  - Verifies file output contents and structure.
  - Confirms accurate summary statistics.
  - Handles edge cases (e.g., empty datasets).

- `requirements.txt`: Lists required Python packages (`pandas`, `pytest`, and `colorama`) so users can easily install dependencies.

- `creditcard.csv`: The dataset file that needs to be placed in the same directory as the code for the project to run.

---

### Design Choices:

- `pandas` was chosen for its powerful and efficient data manipulation capabilities.
- CSV output was selected to make it easy to open and review results in Excel or any spreadsheet tool.
- Paginated display was added for better readability when working with large datasets.
- Minimal dependencies were used to keep the project lightweight and easy to run on any system with Python installed.

---

### How to Run:

```bash
pip install -r requirements.txt
python project.py
