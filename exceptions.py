class Error(Exception):
    def __init__(self, mess):
        self.mess = mess

    def __str__(self):
        return self.mess


class WrongTypeError(Error):
    def __init__(self, expected_type, column_val):
        self.mess = f'Cannot cast "{column_val}" into type "{expected_type}"'
