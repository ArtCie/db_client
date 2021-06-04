from json import dump, load
from Logic import Table, Row, Column


def establish_connection(file_name):
    with open(file_name, "r+") as db_file:
        return load(db_file)


def add_tables(db, content):
    for i in content.keys():
        new_table = Table.Table(i)
        db.add_table(new_table)


def add_columns(db, content):
    for i, j in enumerate(content.values()):
        for col in j["columns"]:
            db.Tables[i].add_column(Column.Column(eval(col[0]), col[1]))


def add_rows(db, content):
    for i, j in enumerate(content.values()):
        for row in j["rows"]:
            db.Tables[i].add_row(Row.Row(row))

#
# def get_data(active_table):
#     columns = list(active_table.keys())
#     length = len(active_table[columns[0]]['data'])
#     serialized_data = [[] for _ in range(length)]
#     for i in active_table.values():
#         counter = 0
#         for each_value in i['data']:
#             serialized_data[counter].append(each_value)
#             counter += 1
#     return serialized_data
