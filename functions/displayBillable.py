
from datetime import datetime


def display_billable_tasks(rally, project=None, iteration=None, project_name_substring=None):
    query_criteria = 'c_Billable = True'
    if iteration:
        query_criteria += f' and Iteration.Name = "{iteration}"'
        print(f"Displaying billable tasks for Iteration: {iteration}")
        print("=" * 130)

    tasks = rally.get('Task', fetch="TimeSpent,WorkProduct,Iteration",
                      query=query_criteria, project=project, pagesize=200)

    total_billable_time = 0

    print(f"{'Story Name': <40} {'Task Name': <40} {
          'Iteration': <20} {'Time Spent (hours)': >20}")
    print("=" * 120)

    for task in tasks:
        story_name = task.WorkProduct.Name if task.WorkProduct else 'No Story'
        story_name = (story_name[:37] +
                      '...') if len(story_name) > 40 else story_name

        iteration_name = task.Iteration.Name if task.Iteration else 'No Iteration'
        if project_name_substring and project_name_substring.lower() not in story_name.lower():
            continue
        time_spent = task.TimeSpent if task.TimeSpent else 0
        total_billable_time += time_spent

        task_name = task.Name
        task_name = (task_name[:37] +
                     '...') if len(task_name) > 40 else task_name

        print(f"{story_name: <40} {task_name: <40} {
              iteration_name: <20} {time_spent: >20}")

    print("=" * 120)
    print(f"{'Total Billable Time': <100} {total_billable_time: >20} hours")
