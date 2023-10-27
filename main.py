import argparse
import sys
from auth.rally_config import load_rally_config
from auth.rally_connection import connect_to_rally
from functions.__init__ import display_billable_tasks, export_to_csv


def main():
    parser = argparse.ArgumentParser(description='Rally operations')
    parser.add_argument('--display-billable',
                        action='store_true', help='Display billable tasks')
    parser.add_argument('--export-csv', action='store_true',
                        help='Export data to CSV')

    args = parser.parse_args()

    config = load_rally_config()
    rally = connect_to_rally(
        config['APIKEY'], config['WORKSPACE'], config['SERVER'])

    if not rally:
        sys.exit(1)

    # Extracting the required values from the config dictionary
    PROJECTS = config['PROJECTS']
    iterationSetting = config['ITERATION_SETTING'] + \
        f" {config['WEEK_NUMBER']}"

    if args.display_billable:
        print("\nDisplaying all billable tasks for a specific iteration and project:")
        display_billable_tasks(
            rally, project=PROJECTS[0], iteration=iterationSetting)

        print("\nDisplaying all billable tasks for a specific iteration, project, and task name substring:")
        display_billable_tasks(
            rally, project=PROJECTS[0], iteration=iterationSetting, project_name_substring="priority")

    if args.export_csv:
        for project in PROJECTS:
            print(f"Exporting data for project: {project}")
            export_to_csv(rally, 'HierarchicalRequirement', 'exported_Stories_All.csv',
                          {'Artifact Type': 'User Story', 'Company': 'C1'}, project, iterationSetting, 'a')
            export_to_csv(rally, 'Task', 'exported_Task_All.csv',
                          {'Artifact Type': 'Task', 'Company': 'C1'}, project, iterationSetting, 'a')
    else:
        # print("Invalid operation specified. Use --help for more information.")
        print('End')


if __name__ == "__main__":
    main()
