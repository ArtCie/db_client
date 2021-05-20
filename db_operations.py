from json import dump, load


def establish_connection(file_name):
    with open(file_name, "r+") as db_file:
        db_content = load(db_file)
        return db_content


def get_tables(content):
    tables = []
    for i in content.keys():
        tables.append(i)
    return tables