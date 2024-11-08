def show_summary(tracker):
    print("\n--- Income ---")
    for item in tracker.income:
        print(f"{item['description']}: ${item['amount']}")

    print("\n--- Expenses ---")
    for item in tracker.expenses:
        print(f"{item['description']}: ${item['amount']}")

    balance = tracker.calculate_balance()
    print(f"\n--- Balance ---\n${balance}")
