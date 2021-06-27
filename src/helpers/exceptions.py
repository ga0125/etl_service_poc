class GenericException(Exception):
    """
    Data already persist on the database custom exception.
    """

    def __init__(self, msg: str):
        self.msg = f"An unexpected error has ocurred. Detail: {msg}"

    def __str__(self):
        return self.msg

    def __repr__(self):
        return f"GenericException({self.msg})"


class FileNotFound(Exception):
    """
    File not found custom exception.
    """

    def __init__(self):
        self.msg = "There is no file to extract."

    def __str__(self):
        return self.msg

    def __repr__(self):
        return f"FileNotFound({self.msg})"


class DataAlreadyPersisted(Exception):
    """
    Data already persist on the database custom exception.
    """

    def __init__(self):
        self.msg = "The data has already been persisted. Please, run docker-compose down --volumes to to clear the DB volume."

    def __str__(self):
        return self.msg

    def __repr__(self):
        return f"DataAlreadyPersisted({self.msg})"
