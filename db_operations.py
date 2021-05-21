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


def get_data(active_table):
    columns = list(active_table.keys())
    length = len(active_table[columns[0]]['data'])
    serialized_data = [[] for _ in range(length)]
    for i in active_table.values():
        counter = 0
        for each_value in i['data']:
            serialized_data[counter].append(each_value)
            counter += 1
    return serialized_data


def get_types(active_table):
    types = [(i['type']) for i in active_table.values()]
    return types


def get_columns_names(active_table):
    return list(active_table.keys())


def parse_input(entered, types):
    for index, value in enumerate(entered):
        if types[index] == "int" and int_cast(value) is False:
            return f'Unable to cast "{value}" to "{types[index]}"'
        elif types[index] == "float" and float_cast(value) is False:
            return f'Unable to cast "{value}" to "{types[index]}"'
    return True


def float_cast(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


def int_cast(num):
    try:
        int(num)
        return True
    except ValueError:
        return False


def insert(content, active_base, types_, entered):
    i = 0
    active_base = content[active_base]
    for key, column_name in active_base.items():
        column_name['data'].append(eval(types_[i])(entered[i]))
        i += 1