class Column:
    def __init__(self, column_type, name):
        self.column_type = column_type
        self.name = name

    def check_column(self, columns):
        for i in columns:
            if i.name == self.name:
                raise AssertionError
        return True

    def get_types(self):
        return self.column_type