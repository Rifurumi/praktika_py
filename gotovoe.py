import tkinter as tk
from datetime import date


class Employee:
    def __init__(self, role, gender, date_of_birth, date_of_employment, education, num_negative_reviews,
                 num_positive_reviews, negative_review_translation="", positive_review_translation=""):
        self.role = role
        self.gender = gender
        self.date_of_birth = date_of_birth
        self.date_of_employment = date_of_employment
        self.education = education
        self.num_negative_reviews = num_negative_reviews
        self.num_positive_reviews = num_positive_reviews
        self.negative_review_translation = negative_review_translation
        self.positive_review_translation = positive_review_translation

    def calculate_age(self):
        today = date.today()
        age = today.year - self.date_of_birth.year
        if today.month < self.date_of_birth.month or (
                today.month == self.date_of_birth.month and today.day < self.date_of_birth.day):
            age -= 1
        return age


def add_employee():
    role = role_entry.get()
    gender = gender_entry.get()
    dob = dob_entry.get()
    doe = doe_entry.get()
    education = education_entry.get()
    num_negative_reviews = int(negative_reviews_entry.get())
    num_positive_reviews = int(positive_reviews_entry.get())
    negative_review_translation = negative_review_entry.get("1.0", tk.END).strip()
    positive_review_translation = positive_review_entry.get("1.0", tk.END).strip()

    dob_date = date.fromisoformat(dob)
    doe_date = date.fromisoformat(doe)

    employee = Employee(role, gender, dob_date, doe_date, education, num_negative_reviews,
                        num_positive_reviews, negative_review_translation, positive_review_translation)
    employees.append(employee)
    update_status_label("Employee added successfully!")
    clear_entries()
    save_employees()


def load_employees():
    try:
        with open("employees.txt", "r", encoding="utf-8") as file:
            for line in file:
                employee_data = line.strip().split(";")
                if len(employee_data) == 9:
                    role = employee_data[0]
                    gender = employee_data[1]
                    dob = date.fromisoformat(employee_data[2])
                    doe = date.fromisoformat(employee_data[3])
                    education = employee_data[4]
                    num_negative_reviews = int(employee_data[5])
                    num_positive_reviews = int(employee_data[6])
                    negative_review_translation = employee_data[7]
                    positive_review_translation = employee_data[8]
                    employee = Employee(role, gender, dob, doe, education, num_negative_reviews,
                                        num_positive_reviews, negative_review_translation, positive_review_translation)
                    employees.append(employee)
    except FileNotFoundError:
        pass


def save_employees():
    with open("employees.txt", "w", encoding="utf-8") as file:
        for employee in employees:
            file.write(f"{employee.role};{employee.gender};{employee.date_of_birth.isoformat()};"
                       f"{employee.date_of_employment.isoformat()};{employee.education};"
                       f"{employee.num_negative_reviews};{employee.num_positive_reviews};"
                       f"{employee.negative_review_translation};{employee.positive_review_translation}\n")


def clear_entries():
    role_entry.delete(0, tk.END)
    gender_entry.delete(0, tk.END)
    dob_entry.delete(0, tk.END)
    doe_entry.delete(0, tk.END)
    education_entry.delete(0, tk.END)
    negative_reviews_entry.delete(0, tk.END)
    positive_reviews_entry.delete(0, tk.END)
    negative_review_entry.delete("1.0", tk.END)
    positive_review_entry.delete("1.0", tk.END)


def update_status_label(message):
    status_label.config(text=message)


def view_waiters():
    waiters_text.delete("1.0", tk.END)
    for employee in employees:
        if employee.gender == "Мужской" and employee.calculate_age() <= 30 and "Техническое" in employee.education:
            waiters_text.insert(tk.END, f"Должность: {employee.role}\n")
            waiters_text.insert(tk.END, f"Пол: {employee.gender}\n")
            waiters_text.insert(tk.END, f"Дата рождения: {employee.date_of_birth}\n")
            waiters_text.insert(tk.END, f"Дата приема на работу: {employee.date_of_employment}\n")
            waiters_text.insert(tk.END, f"Образование: {employee.education}\n")
            waiters_text.insert(tk.END, f"Количество негативных отзывов: {employee.num_negative_reviews}\n")
            waiters_text.insert(tk.END, f"Количество позитивных отзывов: {employee.num_positive_reviews}\n")
            waiters_text.insert(tk.END, f"Негативные отзывы: {employee.negative_review_translation}\n")
            waiters_text.insert(tk.END, f"Позитивные отзывы: {employee.positive_review_translation}\n")
            waiters_text.insert(tk.END, "\n")


def view_all_employees():
    all_employees_text.delete("1.0", tk.END)
    for employee in employees:
        all_employees_text.insert(tk.END, f"Должность: {employee.role}\n")
        all_employees_text.insert(tk.END, f"Пол: {employee.gender}\n")
        all_employees_text.insert(tk.END, f"Дата рождения: {employee.date_of_birth}\n")
        all_employees_text.insert(tk.END, f"Дата приема на работу: {employee.date_of_employment}\n")
        all_employees_text.insert(tk.END, f"Образование: {employee.education}\n")
        all_employees_text.insert(tk.END, f"Количество негативных отзывов: {employee.num_negative_reviews}\n")
        all_employees_text.insert(tk.END, f"Количество позитивных отзывов: {employee.num_positive_reviews}\n")
        all_employees_text.insert(tk.END, f"Негативные отзывы: {employee.negative_review_translation}\n")
        all_employees_text.insert(tk.END, f"Позитивные отзывы: {employee.positive_review_translation}\n")
        all_employees_text.insert(tk.END, "\n")


window = tk.Tk()
window.title('Ресторан "Не печаль"')
window.geometry("800x750")

employees = []

load_employees()

status_label = tk.Label(window, text="")
status_label.pack()

# Фрейм для добавления сотрудника
add_employee_frame = tk.Frame(window)
add_employee_frame.pack(pady=10)

role_label = tk.Label(add_employee_frame, text="Должность:")
role_label.grid(row=0, column=0, padx=5, pady=5)
role_entry = tk.Entry(add_employee_frame)
role_entry.grid(row=0, column=1, padx=5, pady=5)

gender_label = tk.Label(add_employee_frame, text="Пол:")
gender_label.grid(row=1, column=0, padx=5, pady=5)
gender_entry = tk.Entry(add_employee_frame)
gender_entry.grid(row=1, column=1, padx=5, pady=5)

dob_label = tk.Label(add_employee_frame, text="Дата рождения (ГГГГ-ММ-ДД):")
dob_label.grid(row=2, column=0, padx=5, pady=5)
dob_entry = tk.Entry(add_employee_frame)
dob_entry.grid(row=2, column=1, padx=5, pady=5)

doe_label = tk.Label(add_employee_frame, text="Дата приема на работу (ГГГГ-ММ-ДД):")
doe_label.grid(row=3, column=0, padx=5, pady=5)
doe_entry = tk.Entry(add_employee_frame)
doe_entry.grid(row=3, column=1, padx=5, pady=5)

education_label = tk.Label(add_employee_frame, text="Образование:")
education_label.grid(row=4, column=0, padx=5, pady=5)
education_entry = tk.Entry(add_employee_frame)
education_entry.grid(row=4, column=1, padx=5, pady=5)

negative_reviews_label = tk.Label(add_employee_frame, text="Количество негативных отзывов:")
negative_reviews_label.grid(row=5, column=0, padx=5, pady=5)
negative_reviews_entry = tk.Entry(add_employee_frame)
negative_reviews_entry.grid(row=5, column=1, padx=5, pady=5)

positive_reviews_label = tk.Label(add_employee_frame, text="Количество позитивных отзывов:")
positive_reviews_label.grid(row=6, column=0, padx=5, pady=5)
positive_reviews_entry = tk.Entry(add_employee_frame)
positive_reviews_entry.grid(row=6, column=1, padx=5, pady=5)

negative_review_label = tk.Label(add_employee_frame, text="Расшифровка негативного отзыва:")
negative_review_label.grid(row=7, column=0, padx=5, pady=5)
negative_review_entry = tk.Text(add_employee_frame, height=4, width=30)
negative_review_entry.grid(row=7, column=1, padx=5, pady=5)

positive_review_label = tk.Label(add_employee_frame, text="Расшифровка позитивного отзыва:")
positive_review_label.grid(row=8, column=0, padx=5, pady=5)
positive_review_entry = tk.Text(add_employee_frame, height=4, width=30)
positive_review_entry.grid(row=8, column=1, padx=5, pady=5)

add_employee_button = tk.Button(add_employee_frame, text="Добавить сотрудника", command=add_employee)
add_employee_button.grid(row=9, column=0, columnspan=2, padx=5, pady=5)

# Фрейм для просмотра сотрудников
view_employees_frame = tk.Frame(window)
view_employees_frame.pack(pady=10)

view_waiters_button = tk.Button(view_employees_frame, text="Просмотреть официантов",
                                command=view_waiters)
view_waiters_button.grid(row=0, column=0, padx=5, pady=5)

view_all_employees_button = tk.Button(view_employees_frame, text="Просмотреть всех сотрудников",
                                      command=view_all_employees)
view_all_employees_button.grid(row=0, column=1, padx=5, pady=5)

# Фрейм для вывода сотрудников
employees_output_frame = tk.Frame(window)
employees_output_frame.pack(pady=10)

waiters_text = tk.Text(employees_output_frame, height=10, width=50)
waiters_text.pack(side=tk.LEFT, padx=10)

all_employees_text = tk.Text(employees_output_frame, height=10, width=50)
all_employees_text.pack(side=tk.LEFT, padx=10)

window.mainloop()
