def c_to_f(celsius):
    return (celsius * 9/5) + 32


def f_to_c(fahrenheit):
    return (fahrenheit - 32) * 5/9


choice = input("1: C → F, 2: F → C ni tanlang: ")

if choice == "1":
    c = float(input("Celsius kiriting: "))
    print(f"Fahrenheit: {c_to_f(c)}")
elif choice == "2":
    f = float(input("Fahrenheit kiriting: "))
    print(f"Celsius: {f_to_c(f)}")
else:
    print("❌ Noto‘g‘ri tanlov")