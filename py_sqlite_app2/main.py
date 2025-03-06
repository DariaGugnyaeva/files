from sqlalchemy import or_
from db.models import User, Profile, Project, Task
from db import Session


def main():
    session=Session()
    try:
        while user_input := input():
            args = user_input.split()
            match args[0]:
                case "create-user" | "cr-u":
                    username = args[1]
                    email = args[2]
                    new_user = User(username=username, email=email)
                    session.add(new_user)
                    session.commit()

                case "create-profile" | "cr-prof":
                    bio = args[3:]
                    phone = args[1]
                    user_id = args[2]
                    new_prof = Profile(bio=bio, phone=phone, user_id=user_id)
                    session.add(new_prof)
                    session.commit()

                case "create-project" | "cr-proj":
                    title = args[1]  # через нижнее подчёркивание слова
                    description = args[2:]
                    new_proj = Project(username=username, email=email)
                    session.add(new_proj)
                    session.commit()
                
                case "create-task" | "cr-t":
                    title = args[1]
                    status = args[2]
                    project_id = args[3]
                    new_task = Task(title=title, status=status, project_id=project_id)
                    session.add(new_task)
                    session.commit()

                case "all-user" | "a-u":
                    tasks = session.query(User).all()
                    print(f"Found {len(tasks)} user(s)")
                    for task in tasks:
                        print(
                            f"username: {task.username}, email: {task.email}"
                        )

                case "all-profile" | "a-prof":
                    tasks = session.query(Profile).all()
                    print(f"Found {len(tasks)} profile(s)")
                    for task in tasks:
                        print(
                            f"id of profile: {task.id}",
                            f"bio: {task.bio}, email: {task.phone}, user_id: {task.user_id}"
                        )

                case "all-project" | "a-proj":
                    tasks = session.query(Project).all()
                    print(f"Found {len(tasks)} project(s)")
                    for task in tasks:
                        print(
                            f"id of project: {task.id}"
                            f"title: {task.title}, description: {task.description}"
                        )
                
                case "all-task" | "a-t":
                    tasks = session.query(Task).all()
                    print(f"Found {len(tasks)} task(s)")
                    for task in tasks:
                        print(
                            f"id of task: {task.id}"
                            f"title: {task.title}, status: {task.status}, project_id: {task.project_id}"
                        )
                    
                case "find" | "search" | "f" | "s":
                    pattern = " ".join(args[1:])
                    tasks = session.query(Task).filter(or_(Task.name.contains(pattern), Task.description.contains(pattern))).all()
                    print(f"Found {len(tasks)} task(s)")
                    for task in tasks:
                        print(
                            f"id: {task.id}, name: {task.name}, description: '{task.description}', completed: {task.completed}"
                        )

                case "complete" | "co" | "c":
                    id = int(args[1])
                    task = session.query(Task).filter_by(id=id).one()
                    task.completed = True
                    session.commit()

                case "delete" | "d":
                    id = int(args[1])
                    task = Task.get(id)
                    session.delete(task)
                    session.commit()

                case "quit" | "q" | "exit":
                    break

                case _:
                    raise ValueError("invalid command-line argument")

    except EOFError:
        pass


if __name__ == "__main__":
    main()
