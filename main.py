import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is ", now)

while True:
    user_actions = input("Type add, show, edit, complete or exit: ")
    user_actions = user_actions.strip()

    if user_actions.startswith("add"):
        todo = user_actions[4:]

        todos = functions.get_todos()

        todos.append(todo + "\n")

        functions.write_todos(todos)

    elif user_actions.startswith("show"):
        todos = functions.get_todos()

        for index, item in enumerate(todos):
            item = item.strip("\n")
            row = f"{index + 1}.{item}"
            print(row)

    elif user_actions.startswith("edit"):
        try:
            number = int(user_actions[5:])
            number = number-1
            new_todo = input("Enter New Todo:")

            todos = functions.get_todos()

            todos[number] = new_todo +"\n"

            functions.write_todos(todos)
        except ValueError:
            print(" Given Command is not valid")
            continue
    elif user_actions.startswith("complete"):
        try:
            number = int(user_actions[9:])

            todos = functions.get_todos()
            index = number-1
            todo_to_remove = todos[index].strip("\n")
            todos.pop(index)

            functions.write_todos(todos)
            message = f"Todo {todo_to_remove} was removed from the list"
            print(message)
        except IndexError:
            print("There is no item with that number.")
            continue

    elif user_actions.startswith("exit"):
        break
    else:
        print("Given command is not valid.")

print("Bye!")
