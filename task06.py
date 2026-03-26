def is_valid_phone_number(phone: str):
    return phone.isdigit() and len(phone) == 9


phone = input("Telefon raqam kiriting (9 ta raqam): ")


if is_valid_phone_number(phone):
    print("✅ Raqam to‘g‘ri")
else:
    print("❌ Raqam noto‘g‘ri")