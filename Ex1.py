# Перше завдання
# У вас є текстовий файл, який містить інформацію про місячні заробітні плати розробників у вашій компанії. Кожен рядок у файлі містить прізвище 
# розробника та його заробітну плату, які розділені комою без пробілів.
# Ваше завдання - розробити функцію total_salary(path), яка аналізує цей файл і повертає загальну та середню суму заробітної плати всіх розробників.

def total_salary(path):
    try:
        total = 0
        with open(path, "r", encoding = "utf-8") as fh:
            line = fh.readlines()
            amount = len(line)
            if amount == 0:
                return (0, 0)
            # print(amount)

            else:
                for i in line:
                    i = i.strip().split(",")
                    # print(i[1])
                    total = total + int(i[1])
                average = total//amount

            return (total, average)
        
    except FileNotFoundError:
        print(f"Файл за шляхом {path} не знайдено.")
        return (0, 0)
    
    except Exception as e:
        print(f"Сталася помилка: {e}")
        return (0, 0)


total, average = total_salary("salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")


