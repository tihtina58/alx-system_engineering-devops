#!/usr/bin/python3
"""Module fetches employe tasks and display on stdout."""


class Fetch:
    """Class provides fetch services."""

    def __init__(self, userId):
        """Initialize fetch instance."""

        payload = {"userId": userId}

        self.userName = requests.get(
            "https://jsonplaceholder.typicode.com/users/{:s}".format(
                userId
            )
        ).json().get("name")

        self.todos = requests.get(
            "https://jsonplaceholder.typicode.com/todos/",
            params=payload
        ).json()
        return None

    def task_one(self):
        """Returns information about employee TODO list progress
        Args:
            self (object): <class 'main.Fetch'> type object
        Returns:
            Comperhensive string of employee TODO list progress
        """
        brief = "Employee {:s} is done with tasks ({:d}/{:d}):\n".format(
            self.userName,
            len(Fetch.__tasks_count(self.todos).get("complete")),
            len(self.todos)
        )
        completed = Fetch.__completed_tasks(
            Fetch.__tasks_count(self.todos).get("complete")
        )
        return [brief, completed]

    @staticmethod
    def __tasks_count(tasks_list):
        """returns dictionary of task lists acording to completeness.
        Args:
            tasks_list (list): List of tasks fetched.
            status (str): `finished` or `unfinished`.
        Returns:
            dictionary of completed and uncompleted task lists.
        """
        status_dict = {
            "complete": [],
            "incomplete": []
        }

        for elem in tasks_list:
            if elem.get("completed") is True:
                status_dict.get("complete").append(elem)
        for elem in tasks_list:
            if elem not in status_dict["complete"]:
                status_dict.get("incomplete").append(elem)
        return status_dict

    @staticmethod
    def __completed_tasks(tasks_list):
        """Returns string representation of all tasks in provided list
        Args:
            tasks_list (list): List of tasks fetched.
        Returns:
            Tabulated list of completed tasks
        """
        brief = ""
        for elem in tasks_list:
            brief += "\t {:s}\n".format(elem.get("title"))
        return brief
    pass


if __name__ == "__main__":
    import requests
    import sys

    fetch = Fetch(sys.argv[1])
    for elem in fetch.task_one():
        print(elem, end="")
