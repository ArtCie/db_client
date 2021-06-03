from Column import Column
from Database import Database
from Row import Row


class Table:

    def __init__(self, name):
        self.name = name
        self.columns = []
        self.rows = []

    def add_column(self, column_obj):
        try:
            if column_obj.check_column(self.columns):
                if self.check_name(column_obj.name):
                    self.columns.append(column_obj)
        except AssertionError:
            return

    @staticmethod
    def check_name(name):
        temp = name
        temp = temp.replace(" ", "")
        if len(temp) == 0:
            raise AssertionError
        return True

    def remove_column(self, column_obj):
        self.columns.remove(column_obj)

    def add_row(self, row_obj):
        types = self.get_column_types()
        if row_obj.check_casts(types):
            self.rows.append(row_obj)
        else:
            raise ValueError

    def get_column_types(self):
        return [i.column_type for i in self.columns]

    def get_column_names(self):
        return [i.name for i in self.columns]

    def get_rows(self):
        return [row.contents for row in self.rows]

    def remove_row(self, row_obj):
        self.rows.remove(row_obj)

    def query(self, query):
        result = []
        for i in self.rows:
            row = self.get_dict(i)
            res = eval(query)
            if res(row) is True:
                result.append(i.contents)
        return result

    def get_dict(self, row):
        row_dict = {}
        for i, j in enumerate(row.contents):
            row_dict[self.columns[i].name] = j
        return row_dict

    def __str__(self):
        print(f"Table: {self.name}")
        for i in self.columns:
            print(f"{i.name}-{i.column_type.__name__}", end=" ")
        print(" ")
        for rows in self.rows:
            for content in rows.contents:
                print(f"{content}", end=" ")
            print(" ")
        return ""


# column = Column(int, "Ilosc")
# column1 = Column(str, "Nazwa")
# column2 = Column(float, "Cena")
# row = Row(["Telewizor", "5", "2145.23"])
# row1 = Row(["Komputer", "6", "2435.12"])
# row2 = Row(["Telefon", "4", "1400.21"])
#
# table1 = Table("Produkty")
# table1.add_column(column1)
# table1.add_column(column)
# table1.add_column(column2)
# table1.add_row(row)
# table1.add_row(row1)
# table1.add_row(row2)
#
# x = table1.query("lambda row: row['Ilosc'] > 2 and row['Cena'] < 2500.23")
# # print(x)
#
# table2 = Table("Uzytkownicy")
# column2 = Column(str, "Username")
# column3 = Column(str, "password")
# row = Row(["Piotr", "2137"])
# row1 = Row(["Arti", "1488"])
#
#
# table2.add_column(column2)
# table2.add_column(column3)
# table2.add_row(row)
# table2.add_row(row1)
#
# database = Database()
# database.add_table(table1)
# database.add_table(table2)
# # print(database)
#
# print(table2.get_column_names())
# table2.remove_column(column2)
# print(table2.get_column_names())