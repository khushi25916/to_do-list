import streamlit as st

# Initialize session state for tasks
if 'tasks' not in st.session_state:
    st.session_state.tasks = []

def main():
    st.title("To-Do List")

    # Input field for adding tasks
    with st.form("task_form"):
        task = st.text_input("Add a task")
        submit_button = st.form_submit_button("Add Task")

    if submit_button:
        if task:
            st.session_state.tasks.append({"task_name": task, "completed": False})
            
   
    # Display tasks and checkboxes for completion
    for i, t in enumerate(st.session_state.tasks):
        completed = st.checkbox(f"{i + 1}. {t['task_name']}", key=f"task_{i}")
        # Handle the 'completed' status here (e.g., update your data)
    

    #  button for deletion
    if st.button("Delete All Tasks", key="delete_all"):
        st.session_state.tasks = []

def display_tasks(completed=False):
    st.write("# Tasks")
    for i, t in enumerate(st.session_state.tasks):
        if t["completed"] == completed:
            st.checkbox(f"{i + 1}. {t['task_name']}", key=f"task_{i}")


if __name__ == "__main__":
    main()
