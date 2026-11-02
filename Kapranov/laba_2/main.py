import tkinter as tk

root = tk.Tk()
root.title("Капранов А.А, АСИ 23-1")
root.geometry("400x320")
root.resizable(False, False)

# курсы на 19.10.2026
rates = {
    "USD": 82.75,
    "EUR": 92.86,
    "KZT": 0.18
}

tk.Label(
    root,
    text="Конвертер валют",
    font=("Arial", 16, "bold")
).place(x=110, y=15)

tk.Label(
    root,
    text="Введите сумму в рублях:"
).place(x=30, y=65)

rubles = tk.Entry(root)
rubles.place(x=200, y=65, width=150)

tk.Label(
    root,
    text="Выберите валюту:"
).place(x=30, y=110)

currency = tk.StringVar()

tk.Radiobutton(
    root,
    text="USD",
    variable=currency,
    value="USD"
).place(x=30, y=140)

tk.Radiobutton(
    root,
    text="EUR",
    variable=currency,
    value="EUR"
).place(x=130, y=140)

tk.Radiobutton(
    root,
    text="KZT",
    variable=currency,
    value="KZT"
).place(x=230, y=140)


result_label = tk.Label(
    root,
    text="",
    font=("Arial", 11)
)
result_label.place(x=30, y=205)


def convert():
    try:
        input_rubles = float(rubles.get().replace(",", "."))

        if input_rubles <= 0:
            result_label.config(
                text="Недопустимое число"
            )
            return

        selected_currency = currency.get()
        result = input_rubles / rates[selected_currency]
        result_label.config(
            text=f"Результат: {result:.2f} {selected_currency}"
        )

    except ValueError:
        result_label.config(
            text="Ошибка: вы ввели нечисловое значение"
        )


tk.Button(
    root,
    text="Конвертировать",
    command=convert
).place(x=135, y=255)

root.mainloop()
