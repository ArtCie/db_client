from Exceptions.Exceptions import ColumnNameAlreadyInTableException


class Column:
    """class represents Column object"""
    def __init__(self, column_type, name):
        """Constructor takes column type and name and set object attributes"""
        self.column_type = column_type
        self.name = name

    def check_column(self, columns):
        """Method go through all columns and try to find one with name matching"""
        for i in columns:
            if i.name == self.name:
                raise ColumnNameAlreadyInTableException(f'Column "{self.name}" is already in the table!')
        return True

    def get_types(self):
        """Getter of column type"""
        return self.column_type
