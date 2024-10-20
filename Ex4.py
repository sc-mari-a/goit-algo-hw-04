# Четверте завдання
# Напишіть консольного бота помічника, який розпізнаватиме команди, що вводяться з клавіатури, та буде відповідати відповідно 
# до введеної команди.

# На першому етапі наш бот-асистент повинен вміти зберігати ім'я та номер телефону, знаходити номер телефону за ім'ям, 
# змінювати записаний номер телефону, виводити в консоль всі записи, які зберіг. Щоб реалізувати таку нескладну логіку, 
# скористаємося словником. У словнику будемо зберігати ім'я користувача, як ключ, і номер телефону як значення.

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    name, phone = args
    if name in contacts:
        contacts.update({name: phone})
        return "Contact updated."
    else:
        return "Name not found."

def show_phone(args, contacts):
    name, = args
    if name in contacts:
        phone = contacts[name]
        return phone
    else:
        return "Name not found."

def show_all(contacts):
    return contacts

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))

        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":      
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
            
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
