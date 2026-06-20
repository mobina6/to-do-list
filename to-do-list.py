import csv
import os

# کلاس Task: مدل‌سازی هر کار
class Task:
    def __init__(self, name, description, priority):
        self.name = name
        self.description = description
        self.priority = priority  # می‌تواند 'high', 'medium', 'low' باشد

    def __str__(self):
        return f"نام: {self.name} | توضیحات: {self.description} | اولویت: {self.priority}"


# کلاس ToDoList: مدیریت لیست کارها
class ToDoList:
    def __init__(self, filename="tasks.csv"):
        self.tasks = []
        self.filename = filename
        self.load_from_csv()  # بارگذاری خودکار از فایل در زمان شروع

    # افزودن کار جدید
    def add_task(self, name, description, priority):
        task = Task(name, description, priority)
        self.tasks.append(task)
        self.save_to_csv()  # ذخیره خودکار بعد از هر تغییر
        print(f"✅ کار '{name}' با موفقیت اضافه شد.")

    # حذف کار با استفاده از نام
    def remove_task(self, name):
        for task in self.tasks:
            if task.name == name:
                self.tasks.remove(task)
                self.save_to_csv()
                print(f"❌ کار '{name}' حذف شد.")
                return
        print(f"⚠️ کار با نام '{name}' پیدا نشد.")

    # نمایش تمام کارها
    def show_tasks(self):
        if not self.tasks:
            print("📭 لیست کارها خالی است.")
        else:
            print("\n📋 لیست کارها:")
            for idx, task in enumerate(self.tasks, 1):
                print(f"{idx}. {task}")
        print()

    # ذخیره لیست در فایل CSV
    def save_to_csv(self):
        with open(self.filename, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["name", "description", "priority"])  # هدر
            for task in self.tasks:
                writer.writerow([task.name, task.description, task.priority])
        print(f"💾 لیست کارها در فایل '{self.filename}' ذخیره شد.")

    # بارگذاری لیست از فایل CSV
    def load_from_csv(self):
        if not os.path.exists(self.filename):
            return  # فایل وجود ندارد، شروع با لیست خالی
        with open(self.filename, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            self.tasks = []
            for row in reader:
                task = Task(row["name"], row["description"], row["priority"])
                self.tasks.append(task)
        print(f"📂 لیست کارها از فایل '{self.filename}' بارگذاری شد.")


# منوی متنی برنامه
def main():
    todo = ToDoList()

    while True:
        print("\n--- 📝 مدیریت لیست کارها (To-Do List) ---")
        print("1. اضافه کردن کار جدید")
        print("2. حذف کار")
        print("3. مشاهده لیست کارها")
        print("4. ذخیره دستی لیست (اختیاری، خودکار هم ذخیره می‌شود)")
        print("5. خروج")

        choice = input("انتخاب شما (1-5): ")

        if choice == "1":
            name = input("نام کار: ")
            description = input("توضیحات کار: ")
            print("اولویت (high / medium / low): ", end="")
            priority = input().strip().lower()
            if priority not in ["high", "medium", "low"]:
                print("⚠️ اولویت نامعتبر! تنظیم روی 'medium'")
                priority = "medium"
            todo.add_task(name, description, priority)

        elif choice == "2":
            name = input("نام کاری که می‌خواهید حذف کنید: ")
            todo.remove_task(name)

        elif choice == "3":
            todo.show_tasks()

        elif choice == "4":
            todo.save_to_csv()

        elif choice == "5":
            print("👋 خروج از برنامه. ذخیره نهایی انجام شد.")
            break

        else:
            print("❗ گزینه نامعتبر، لطفاً دوباره تلاش کنید.")


if __name__ == "__main__":
    main()