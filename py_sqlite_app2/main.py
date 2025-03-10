from sqlalchemy import or_
from sqlalchemy import update
from db.models import User, Profile, Project, Task
from db import Session


def main():
    session=Session()
    try:
        while user_input := input():
            args = user_input.split()
            match args[0]:
                case "create-user-proj" | "cr-u-pr" | "добавить-пользователя-на-проект":
                    new_relation = association_table(user_id=args[0], proj_id=args[1])
                    session.add(new_relation)
                    session.commit()  # как с этим жить, я так и не поняла

                case "create-user" | "cr-u" | "добавить-пользователя":
                    new_user = User(id=args[1], username=args[2], email=args[3])
                    session.add(new_user)
                    session.commit()

                case "create-profile" | "cr-prof" | "создать-профиль":
                    new_prof = Profile(bio=' '.join(args[3:]), phone=args[1], user_id=args[2])
                    session.add(new_prof)
                    session.commit()

                case "create-project" | "cr-proj" | "добавить-проект":
                    new_proj = Project(id=args[1], title=args[2], description=' '.join(args[3:]))
                    session.add(new_proj)
                    session.commit()
                
                case "create-task" | "cr-t" | "добавить-задачу":
                    if args[2] in ['True', True, 1]:
                        st = True
                    else:
                        st = False
                    new_task = Task(title=args[1], status=st, project_id=args[3])
                    session.add(new_task)
                    session.commit()

                case "all-user" | "a-u" | "вывести-пользователей":
                    tasks = session.query(User).all()
                    print(f"Found {len(tasks)} user(s)")
                    for task in tasks:
                        print(
                            f"username: {task.username}, email: {task.email}"
                        )

                case "all-profile" | "a-prof" | "вывести-профили":
                    tasks = session.query(Profile).all()
                    print(f"Found {len(tasks)} profile(s)")
                    for task in tasks:
                        print(
                            f"id of profile: {task.id}\n",
                            f"bio: {task.bio}, email: {task.phone}, user_id: {task.user_id};"
                        )

                case "all-project" | "a-proj" | "вывести-проекты":
                    tasks = session.query(Project).all()
                    print(f"Found {len(tasks)} project(s)")
                    for task in tasks:
                        print(
                            f"id of project: {task.id}\n"
                            f"title: {task.title}, description: {task.description};"
                        )
                
                case "all-task" | "a-t" | "вывести-задачи":
                    tasks = session.query(Task).all()
                    print(f"Found {len(tasks)} task(s)")
                    for task in tasks:
                        print(
                            f"id of task: {task.id}\n"
                            f"title: {task.title}, status: {task.status}, project_id: {task.project_id};"
                        )
                    
                case "update-user" | "обновление-пользователя":
                    id, pattern = args[1], args[2]
                    user = session.query(User).filter_by(id=id).one()
                    if '@' in pattern:
                        user.email = pattern
                    else:
                        user.username = pattern
                    session.commit()

                case "update-prof" | "обновление-профиля":
                    id, pattern = args[1], ' '.join(args[2:])
                    prof = session.query(Profile).filter_by(id=id).one()
                    if all(character.isdigit() for character in pattern):
                        # номер без плюсика записывать
                        user.phone = pattern
                    else:
                        prof.bio = pattern
                    session.commit()
        
                case "update-proj" | "проект-выполнен" | "проект-изменился" | "проект-не-выполнен" | "обновление-проекта":
                    id, pattern = args[1], ' '.join(args[2:])
                    proj = session.query(Project).filter_by(id=id).one()
                    if ' ' in pattern:
                        proj.description = pattern
                    else:
                        proj.title = pattern  # напоминаю, через _
                    session.commit()
                    
    
                case "update-task" | "задача-выполнена" | "задача-изменилась" | "переделать" | "задача-не-выполнена":
                    id, pattern = args[1], ' '.join(args[3:])
                    task = session.query(Task).filter_by(id=id).one()
                    if args[2] == 'status':  # придётся указать, что хотите статус менять
                        if pattern in ['True', True, 1]:
                            task.status = True
                        else:
                            task.status = False
                    else:
                        task.title = pattern
                    session.commit()

                case "delete-user" | "d-u" | "удалить-пользователя-и-его-профиль":
                    id = args[1]
                    # user_id = User.get(id)
                    user_to_delete = session.query(User).filter_by(id=id).first()
                    profile_to_delete = session.query(Profile).filter_by(id=id).first()
                    session.delete(user_to_delete)
                    session.delete(profile_to_delete)
                    session.commit()

                case "delete-proj" | "d-proj" | "удалить-проект":
                    id = args[1]
                    tasks = session.query(Task).filter_by(project_id=id)
                    for task in tasks:
                        session.delete(task)
#                    session.commit()

                    new = session.query(Project).filter_by(id=id).first()
                    session.delete(new)
                    session.commit()

                    # session=Session()


                case "delete-task" | "d-t" | "удалить-задачу":
                    id = args[1]
                    task_to_delete = session.query(Task).filter_by(id=id).first()
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
