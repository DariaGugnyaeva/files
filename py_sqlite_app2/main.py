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
                    
                case "update-user" | "обновление пользователя":
                    pattern = args[1]
                    user = session.query(User).filter_by(id=id).one()
                    if '@' in pattern:
                        user.email = pattern
                    else:
                        user.username = pattern
                    session.commit()

                case "update-prof" | "обновление профиля":
                    pattern = ' '.join(args[1:])
                    prof = session.query(Profile).filter_by(id=id).one()
                    if all(character.isdigit() for character in pattern):
                        user.phone = pattern
                    else:
                        prof.bio = pattern
                    session.commit()
        
                case "update-proj" | "проект выполнен" | "проект изменился" | "проект не выполнен":
                    pattern = ' '.join(args[1:])
                    proj = session.query(Project).filter_by(id=id).one()
                    if ' ' in pattern:
                        proj.description = pattern
                    else:
                        proj.title = pattern  # напоминаю, через _
                    session.commit()
                    
    
                case "update-task" | "задача выполнена" | "задача изменилась" | "переделать" | "задача не выполнена":
                    pattern = ' '.join(args[1:])
                    task = session.query(Task).filter_by(id=id).one()
                    if pattern in ['True', True, 'False', False]:
                        task.status = bool(pattern)
                    # хорошую задачу 1 словом назовёшь, но не опишешь...
                    elif ' ' not in pattern:
                        task.title = pattern
                    else:
                        task.desription = pattern
                    session.commit()

                case "delete-user" | "d-u" | "удалить пользователя и его профиль":
                    id = args[1]
                    user_id = User.get(id)
                    user_to_delete = session.query(User).delete(user_id)
                    # в Profile есть столбец user_id. Что делать?
                    profile_to_delete = session.query(Profile).delete(user_id)
                    session.delete(user_to_delete)
                    session.delete(profile_to_delete)
                    session.commit()

                case "delete-proj" | "d-proj" | "удалить проект":
                    # title and description
                    id = args[1]
                    proj_id = Project.get(id)
                    proj_to_delete = session.query(Project).delete(proj_id)
                    session.delete(proj_to_delete)
                    session.commit()

                case "delete-task" | "d-t" | "удалить задачу":
                    id = args[1]
                    task_id = Task.get(id)
                    task_to_delete = session.query(Task).delete(task_id)
                    session.delete(task_to_delete)
                    session.commit()

                case "quit" | "q" | "exit":
                    break

                case _:
                    raise ValueError("invalid command-line argument")

    except EOFError:
        pass


if __name__ == "__main__":
    main()
