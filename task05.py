def check_guess(secret, guess):
    return secret == guess


def print_result(is_correct):
    if is_correct:
        print("🎉 To‘g‘ri topdingiz!")
    else:
        print("❌ Xato, yana urinib ko‘ring.")


secret_number = 7


guess = int(input("Sonni taxmin qiling (1-10): "))


result = check_guess(secret_number, guess)
print_result(result)