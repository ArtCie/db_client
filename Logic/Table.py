
class Table:
    """Class represents Table of database, takes Table name as argument"""
    def __init__(self, name):
        """Constructor takes name and set it as object field, it also defines empty list of columns and rows"""
        self.name = name
        self.columns = []
        self.rows = []

    def add_column(self, column_obj):
        """Method checks whether column is already in base and its name - then it adds column to column list"""
        if column_obj.check_column(self.columns):
            if self.check_name(column_obj.name):
                self.columns.append(column_obj)
            for i in self.rows:
                i.contents.append("")

    @staticmethod
    def check_name(name):
        """Method checks if name of table is empty"""
        temp = name
        temp = temp.replace(" ", "")
        if len(temp) == 0:
            raise ValueError
        return True

    def remove_column(self, column_obj):
        """Method checks whether column object is in base, then it returns it and rows associate with this column"""
        temp = 0
        for obj in self.columns:
            if obj.name == column_obj.name:
                break
            temp += 1
        else:
            return
        self.columns.remove(column_obj)
        for each_row in self.rows:
            del each_row.contents[temp]

    def add_row(self, row_obj):
        """Method add one row to table"""
        types = self.get_column_types()
        if row_obj.check_casts(types):
            self.rows.append(row_obj)
        else:
            raise ValueError

    def remove_row(self, row_obj):
        """Method removes row from database"""
        self.rows.remove(row_obj)

    def get_column_types(self):
        """Method returns list of columns types"""
        return [i.column_type for i in self.columns]

    def get_column_names(self):
        """Method returns list of columns names"""
        return [i.name for i in self.columns]

    def get_rows(self):
        """Method returns list of each row contents"""
        return [row.contents for row in self.rows]

    def get_rows_obj(self):
        """Method returns rows list"""
        return self.rows

    def get_obj(self, content):
        """Method checks whether row object is in table, return it or False if it is not present"""
        for i in self.rows:
            if i.contents == content:
                return i
        return False

    def get_col(self, new_col):
        """Method returns column object if it is present in the list, else it returns None"""
        for i in self.columns:
            if i.name == new_col.name and i.column_type == new_col.column_type:
                return i
        return None

    def query(self, query):
            """Method parse lambda expression and returns result"""
        # try:
            result = []
            for i in self.rows:
                row = self.get_dict(i)
                res = eval(query)
                if res(row) is True:
                    result.append(i.contents)
            return result
        # except SyntaxError:
            # return False

    def get_dict(self, row):
        """Method returns dictionary for lambda expression"""
        row_dict = {}
        for i, j in enumerate(row.contents):
            row_dict[self.columns[i].name] = j
        return row_dict

