#List of (name, balance) pairs
customers=[("Nahom",1250.00),
   ("Selam", 480.50),
    ("Bereket", 999.99),
    ("Hanna", 75.00),
    ("Yonas", 1000.00),
    ("Meklit", 512.30),
]

def tier(balance):
    ""Return the customer tier based on their TeleBirr balance"".

    if balance >= 1000:
        return "Premium"
    elif balance >= 500:
        return "Standard"
    else:
        return "Basic"

        def main():
    tier_counts = {"Premium": 0, "Standard": 0, "Basic": 0}
 
    print(f"{'Name':<12}{'Tier':<12}{'Balance (ETB)':>15}")
    print("-" * 39)
 
    for name, balance in customers:
        customer_tier = tier(balance)
        tier_counts[customer_tier] += 1
        print(f"{name:<12}{customer_tier:<12}{balance:>15,.2f}")
 
    print("-" * 39)
    print("\nSummary:")
    for tier_name in ("Premium", "Standard", "Basic"):
        print(f"  {tier_name:<10}: {tier_counts[tier_name]} customer(s)")

        if __name__ == "__main__":
    main()