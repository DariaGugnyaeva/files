from db.models import Library

def main():
    db_path = "./library.db"
    task_table = Library(db_path)
    try:
        while user_input := input():
            args = user_input.split()
            match args[0]:
                case "create-lib" | "cr-lib":
                    name_book, author, year_created = args[1], args[2], int(args[3])
                    edition, num_book_case, num_shell = int(args[4]), int(args[5]), int(args[6])
                    status = args[7]
                    task_table.objects_1.create(name_book, author, year_created, edition, num_book_case, num_shell, status)

                case "create-vis" | "cr-vis":
                    name, surname, patr_name = args[1], args[2], args[3]
                    num_reader_card, address = args[4], args[5]
                    task_table.objects_2.create(name, surname, patr_name, num_reader_card, address)
                
                case "create-read" | "cr-read":
                    id_book, num_reader_card = args[1], args[2]
                    task_table.objects_3.create(id_book, num_reader_card)

                case "all-lib" | "a-lib":
                    tasks = task_table.objects_1.all()
                    for task in tasks:
                        print(f"name_book: {task[0]}, author: {task[1]}, year_created: {task[2]},")
                        print(f"edition: {task[3]}, num_book_case: {task[4]}, num_shell: {task[5]},")
                        print(f"status: {task[6]}")
                
                case "all-vis" | "a-vis":
                    tasks = task_table.objects_2.all()
                    for task in tasks:
                        print(f"name: {task[0]}, surname: {task[1]},")
                        print(f"patr_name: {task[2]}, num_reader_card: {task[3]},")
                        print(f"address: {task[4]}")

                case "all-read" | "a-read":
                    tasks = task_table.objects_3.all()
                    for task in tasks:
                        print(f"num_reader_card: {task[0]}, name: {task[1]},")
                        print(f"surname: {task[2]}, name_book: {task[3]}")
                
                case "find-lib" | "search-lib" | "f-lib" | "s-lib":
                    pattern = args[1]
                    tasks = task_table.objects_1.search(pattern)
                    print(f'Found {len(tasks)} book(s)')
                    for task in tasks:
                        print(f'id of book is {task[0]}')
                        print(f"name_book: {task[1]}, author: {task[2]}, year_created: {task[3]},")
                        print(f"edition: {task[4]}, num_book_case: {task[5]},")
                        print(f"num_shell: {task[6]}, status: {task[7]}")
                
                case "find-vis" | "search-vis" | "f-vis" | "s-vis":
                    pattern = args[1]
                    tasks = task_table.objects_2.search(pattern)
                    print(f"Found {len(tasks)} visitor(s)")
                    for task in tasks:
                        print(f'id of visitor is {task[0]}')
                        print(f"name: {task[1]}, surname: {task[2]}, patr_name: {task[3]}")
                        print(f"num_reader_card: {task[4]}")
                
                case "complete" | "co" | "c":
                    id = args[1]
                    task_table.objects_1.complete(id)

                case "delete-lib" | "d-lib":
                    id = int(args[1])
                    task_table.objects_1.delete(id)

                case "delete-vis" | "d-vis":
                    id = int(args[1])
                    task_table.objects_2.delete(id)

                case "delete-read" | "d-read":
                    id = int(args[1])
                    task_table.objects_3.delete(id)

                case "quit" | "q" | "exit":
                    break

                case _:
                    raise ValueError("invalid command-line argument")

    except EOFError:
        pass


if __name__ == "__main__":
    main()
