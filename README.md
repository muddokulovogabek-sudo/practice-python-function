## ✅ Loyihalar ro'yxati (real va qiziqarli)

### 1. 💡 **Calculator (Kalkulyator)**

* **Vazifa**: Foydalanuvchi son va amalni kiritadi: `+`, `-`, `*`, `/`
* **Funksiyalar**:

  * `add(a, b)`, `subtract(a, b)`, `multiply(a, b)`, `divide(a, b)`
* **Qamrab oladi**: funksiya, `if`, `input/output`, `return`, primitive types

---

### 2. 🕐 **Age Calculator**

* **Vazifa**: Tug‘ilgan yilni kiritadi → hozirgi yildan yoshini hisoblab beradi.
* **Funksiya**:

  * `calculate_age(birth_year, current_year)`
* **Qo‘shimcha**: “Siz balog‘atga yetgansiz/yetmagansiz” degan javob chiqarsin.

---

### 3. 🔢 **Even/Odd Number Checker**

* **Vazifa**: Son kiritiladi, u **juft yoki toq**ligini aniqlaydi.
* **Funksiya**:

  * `is_even(number)` → `True/False`
  * `print_even_message(number)`

---

### 4. 🏆 **Simple Grading System**

* **Vazifa**: Foydalanuvchi ball kiritadi → `A`, `B`, `C`, `F` baho qaytadi.
* **Funksiya**:

  * `get_grade(score)`
* **Qo‘llaniladigan narsa**: `if-elif-else`, `str`, `int`

---

### 5. 🎲 **Number Guessing Game (Random ishlatilmaydi)**

* **Vazifa**: Kompyuterda sirli son mavjud. Foydalanuvchi taxmin qiladi. To‘g‘ri yoki xato deyilgan bo‘ladi.
* **Funksiya**:

  * `check_guess(secret, guess)`
  * `print_result(is_correct)`

---

### 6. 📞 **Phone Number Validator**

* **Vazifa**: Telefon raqam 9 ta raqamdan iboratligini tekshiradi.
* **Funksiya**:

  * `is_valid_phone_number(phone: str)` → `True/False`

---

### 7. 🧠 **Mini Quiz Game (1-2 savol)**

* **Vazifa**: Savol beriladi, javobni tekshiradi.
* **Funksiya**:

  * `ask_question(question: str, correct_answer: str)`
  * `check_answer(user_answer, correct_answer)`

---

### 8. 🕹 **Temperature Converter**

* **Vazifa**: Celsius ↔ Fahrenheit aylantirish.
* **Funksiya**:

  * `c_to_f(celsius)`
  * `f_to_c(fahrenheit)`

---

### 🎁 **Bonus 1: Simple ATM Simulation**

* **Vazifa**: Foydalanuvchining balansi bor. U `deposit`, `withdraw` yoki `check balance` qiladi.
* **Funksiya**lar:

  * `deposit(balance, amount)`
  * `withdraw(balance, amount)`
  * `check_balance(balance)`

🧠 Primetivlar: `int`, `float`, `str`, `bool`

---

### 🎁 **Bonus 2: Password Strength Checker**

* **Vazifa**: Parolni kiritadi, kuchli yoki kuchsizligini tekshiradi (masalan, uzunligi 8 dan katta bo‘lsa kuchli).
* **Funksiya**:

  * `is_strong_password(password: str) -> bool`

🧠 Bu yerda `len()` funksiyasini ishlatish mumkin, lekin **list** ishlatilmaydi.

---

### 🎁 **Bonus 3: Tax Calculator**

* **Vazifa**: Maoshni kiritadi → soliqni hisoblab beradi.
* **Funksiya**:

  * `calculate_tax(salary: float) -> float`
  * `calculate_net_salary(salary: float) -> float`

🧠 Moslashuvchan `if` bilan soliq stavkasi o‘zgarishi mumkin (masalan, >5mln bo‘lsa 20%, boshqacha 13%).

---

### 🎁 **Bonus 4: BMI Calculator (Body Mass Index)**

* **Vazifa**: Og‘irlik va bo‘y kiritiladi → BMI va uning holati (`normal`, `overweight`) chiqadi.
* **Funksiya**:

  * `calculate_bmi(weight: float, height: float) -> float`
  * `bmi_status(bmi: float) -> str`

---

### 🎁 **Bonus 5: Palindrome Checker (faqat str bilan)**

* **Vazifa**: So‘z kiritiladi → teskari o‘qiganda ham bir xilmi, yo‘qmi tekshiriladi.
* **Funksiya**:

  * `is_palindrome(text: str) -> bool`

🧠 Bu yerda slicing (`[::-1]`) ishlatiladi, lekin list emas!

---
