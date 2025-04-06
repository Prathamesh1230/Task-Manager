class Task:
    def __init__(self, title, description, status="Pending"):
        self.title = title
        self.description = description
        self.status = status

    def __str__(self):
        return f"{self.title} - {self.status}"
