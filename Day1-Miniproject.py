bills = { #bills (monthly)

        "rent": int(),
        "phone_recharge": int(),
        "internet": int(),
        "electric": int(),
        "transportation": int(),
        "personal care": int(),
        "food": int(),
        "other": int(),
        "gym": int(),
        "charity": int()
}

n = len(bills)
total = int()
for keys in bills:
    print(f"{keys} :",end=" ")
    value = int(input())
    bills[keys] = value

for values in bills.values():
    total += values

print(f"Total: {total}")
print(f"Monthly Average: {total/n}")