import pandas as pd
from tabulate import tabulate
import os
from colorama import init, Fore, Style

def main():
    # Load dataset
    try:
        df = pd.read_csv("creditcard.csv")
    except FileNotFoundError:
        print("Error: creditcard.csv not found.")
        return

    print("Dataset loaded. Total records:", len(df))

    # Detect fraud
    fraud_df = detect_fraud(df)
    print(f"Number of fraudulent transactions: {len(fraud_df)}")

    # Save to file
    save_flagged_transactions(fraud_df)
    print("Flagged transactions saved to 'flagged.csv'.")

    # Ask user if they want to view flagged transactions from file
    choice = input("Do you want to view the flagged transactions from file? (y/n): ").strip().lower()
    if choice == 'y':
        display_flagged_file()

    # Summary stats
    summary = summarize_data(df)
    print("\nTransaction Summary:")
    for key, value in summary.items():
        print(f"{key}: {value}")

def detect_fraud(data):
    """Returns all transactions where Class == 1 (fraud)."""
    return data[data["Class"] == 1]

def save_flagged_transactions(data, output_file="flagged.csv"):
    """Save fraudulent transactions to CSV."""
    data.to_csv(output_file, index=False)

def summarize_data(data):
    """Return basic summary statistics of the dataset."""
    summary = {
        "total_transactions": len(data),
        "fraud_transactions": len(data[data["Class"] == 1]),
        "legit_transactions": len(data[data["Class"] == 0]),
        "fraud_percentage": round(100 * len(data[data["Class"] == 1]) / len(data), 4)
    }
    return summary

# Initialize colorama
init(autoreset=True)

def display_flagged_file(file_path="flagged.csv", page_size=10):
    """Read and display data from the flagged.csv file interactively."""
    print("\n" + "="*50)
    print(Fore.CYAN + Style.BRIGHT + "📄 Viewing Flagged Fraudulent Transactions")
    print("="*50)

    if not os.path.exists(file_path):
        print(Fore.RED + f"❌ File '{file_path}' does not exist. Run fraud detection first.")
        return

    try:
        df = pd.read_csv(file_path)

        if df.empty:
            print(Fore.YELLOW + "⚠️  No fraudulent transactions were detected.")
            return

        # Format Amount column for better readability
        df["Amount"] = df["Amount"].apply(lambda x: f"${x:,.2f}")

        total_rows = len(df)
        current = 0

        while current < total_rows:
            end = min(current + page_size, total_rows)
            print(tabulate(df.iloc[current:end], headers="keys", tablefmt="fancy_grid", showindex=False))
            print(Fore.GREEN + f"\nShowing {current + 1} to {end} of {total_rows} flagged transactions.")

            if end == total_rows:
                print(Fore.CYAN + "\n✅ End of data.")
                break

            user_input = input(Fore.YELLOW + "Press Enter to view more, or type 'q' to quit: ").strip().lower()
            if user_input == 'q':
                print(Fore.CYAN + "Exited viewer.")
                break
            current += page_size

    except Exception as e:
        print(Fore.RED + f"An error occurred while reading {file_path}: {e}")

if __name__ == "__main__":
    main()
