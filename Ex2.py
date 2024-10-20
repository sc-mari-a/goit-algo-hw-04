# Друге завдання
# У вас є текстовий файл, який містить інформацію про котів. Кожен рядок файлу містить унікальний ідентифікатор кота, його ім'я та вік, розділені комою.
# Ваше завдання - розробити функцію get_cats_info(path), яка читає цей файл та повертає список словників з інформацією про кожного кота.

def get_cats_info(path):
    try:
        list_cats_info = []
        with open(path, "r", encoding = "utf-8") as fh:
            line = fh.readlines()
            amount = len(line)
            if amount == 0:
                return list_cats_info

            else:
                for i in line:
                    i = i.strip().split(",")
                    list_cats_info.append({"id": i[0], "name": i[1], "age": i[2]})

            return list_cats_info
        
    except FileNotFoundError:
        print(f"Файл за шляхом {path} не знайдено.")
        return []
    
    except Exception as e:
        print(f"Сталася помилка: {e}")
        return []

cats_info = get_cats_info("cats_file.txt")
print(cats_info)
