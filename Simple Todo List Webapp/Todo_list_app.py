import streamlit as st
from datetime import datetime


def main():
    st.title("Todo List App")
    tasks = st.session_state.get('tasks', [])  # Retrieve tasks from session state

    # Add a new task
    new_task = st.text_input("Add a new task:")
    if st.button("Add"):
        tasks.append({'task': new_task, 'completed': False, 'time': datetime.now()})
        st.session_state.tasks = tasks
        new_task = ''

    # Show the list of tasks
    for i, task in enumerate(tasks):
        task_text = task['task']
        completed = task['completed']
        time = task['time']

        # Display checkbox for completed tasks
        if st.checkbox(task_text, value=completed, key=i):
            tasks[i]['completed'] = True
            tasks[i]['time'] = datetime.now()
        else:
            tasks[i]['completed'] = False

    # Display clock
    now = datetime.now()
    st.sidebar.title("Current Time")
    st.sidebar.write(now.strftime("%H:%M:%S"))


if __name__ == "__main__":
    main()
