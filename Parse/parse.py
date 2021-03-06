from json import load
from Logic import Table, Row, Column


def establish_connection(file_name):
    """Function try to open file and returns it's content"""
    with open(file_name, "r+") as db_file:
        return load(db_file)


def add_tables(db, content):
    """Function loads table names from file to Database class object"""
    for i in content.keys():
        new_table = Table.Table(i)
        db.add_table(new_table)


def add_columns(db, content):
    """Function loads table columns with types to Database class object"""
    for i, j in enumerate(content.values()):
        for col in j["columns"]:
            db.Tables[i].add_column(Column.Column(eval(col[0]), col[1]))


def add_rows(db, content):
    """Function loads table rows with types to Database class object"""
    for i, j in enumerate(content.values()):
        for row in j["rows"]:
            db.Tables[i].add_row(Row.Row(row))


def get_json(db):
    """Function takes contents of table from Database class and parses it into dictionary"""
    dump_dict = {}
    for i in db.Tables:
        columns = []
        for j in zip(i.get_column_types(), i.get_column_names()):
            columns.append([j[0].__name__, j[1]])
        append_rows = []
        for rows in i.rows:
            append_rows.append(rows.contents)
        temp_dict = {'columns': columns, 'rows': append_rows}
        dump_dict[i.name] = temp_dict
    return dump_dict
