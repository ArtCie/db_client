class Error(Exception):
    pass


class WrongNameException(Error):
    def __init__(self, message):
        self.message = message


class UnableToCastException(Error):
    def __init__(self, message):
        self.message = message


class TableNameAlreadyInDatabaseException(Error):
    def __init__(self, message):
        self.message = message


class ColumnNameAlreadyInTableException(Error):
    def __init__(self, message):
        self.message = message


class SyntaxErrorException(Error):
    def __init__(self, message):
        self.message = message