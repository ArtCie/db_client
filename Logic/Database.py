class Database:
    def __init__(self):
        self.Tables = []

    def add_table(self, table_obj):
        try:
            if self.check_name(table_obj):
                if self.check_tables(table_obj):
                    self.Tables.append(table_obj)
                else:
                    print("Raise already in db")
            else:
                print("Raise wrong name")
        except AssertionError:
            return

    def check_tables(self, table_obj):
        for table in self.Tables:
            if table.name == table_obj.name:
                return False
        return True

    @staticmethod
    def check_name(table):
        temp = table.name
        temp = temp.replace(" ", "")
        if len(temp) == 0:
            raise AssertionError
        else:
            return True

    def get_tables_names(self):
        return [table.name for table in self.Tables]

    def remove_table(self, table_obj):
        self.Tables.remove(table_obj)

    def __str__(self):
        for i in self.Tables:
            print(i)
            print(" ")
        return " "
