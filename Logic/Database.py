from Exceptions.Exceptions import WrongNameException
from Exceptions.Exceptions import TableNameAlreadyInDatabaseException

class Database:
    """Database class represents database object, contains list of table objects"""
    def __init__(self):
        """Constructor of database defines empty list of tables"""
        self.Tables = []

    def add_table(self, table_obj):
        """Method check whether name is valid and then add table to Tables list"""
        if self.check_name(table_obj):
            if self.check_tables(table_obj):
                self.Tables.append(table_obj)
            else:
                raise TableNameAlreadyInDatabaseException(f'Table "{table_obj.name}" is already in the table!')
        else:
            raise WrongNameException(f'{table_obj.name} name is not valid!')

    def check_tables(self, table_obj):
        """Method checks whether table object is present in Tables list"""
        for table in self.Tables:
            if table.name == table_obj.name:
                return False
        return True

    @staticmethod
    def check_name(table):
        """Method removes spaces and check if there is any sign present"""
        temp = table.name
        temp = temp.replace(" ", "")
        if len(temp) == 0:
            return False
        else:
            return True

    def get_tables_names(self):
        """Method returns list of names of tables"""
        return [table.name for table in self.Tables]

    def remove_table(self, table_obj):
        """Method removes table object from list of tables"""
        self.Tables.remove(table_obj)

    def get_active(self, name):
        """Method returns table based on name"""
        for table in self.Tables:
            if table.name == name:
                return table
        return False
