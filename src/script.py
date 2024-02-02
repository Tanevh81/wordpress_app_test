import os

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f'Task "{task}" added.')

    def view_tasks(self):
        if not self.tasks:
            print('No tasks in the to-do list.')
        else:
            print('To-Do List:')
            for index, task in enumerate(self.tasks, start=1):
                print(f'{index}. {task}')

    def mark_completed(self, index):
        if 1 <= index <= len(self.tasks):
            completed_task = self.tasks.pop(index - 1)
            print(f'Task "{completed_task}" marked as completed.')
        else:
            print('Invalid task index.')

def main():
    todo_list = ToDoList()

    while True:
        print('\nMenu:')
        print('1. Add Task')
        print('2. View Tasks')
        print('3. Mark Task as Completed')
        print('4. Exit')

        choice = input('Enter your choice: ')

        if choice == '1':
            task = input('Enter the task: ')
            todo_list.add_task(task)
        elif choice == '2':
            todo_list.view_tasks()
        elif choice == '3':
            index = int(input('Enter the task index to mark as completed: '))
            todo_list.mark_completed(index)
        elif choice == '4':
            print('Exiting the to-do list application. Goodbye!')
            break
        else:
            print('Invalid choice. Please choose a valid option.')

if __name__ == "__main__":
    main()
