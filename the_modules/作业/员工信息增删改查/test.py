COLUMNS = ["id", "name", "age", "phone", "occupation", "hire_data"]
staff_table = "employee_info.txt"


def print_log(msg,log_type = 'info'):
    if log_type == 'info':
        print(msg)
    elif log_type == 'error':
        print("\033[31;1m%s\032[0m"%msg)

def load_tab(file):  #加载文件，以指定的格式进行加载。
    data = {}
    for i in COLUMNS:
        data[i] = []
        data_mark = COLUMNS.index(i)
        with open(file, 'r', encoding='utf-8') as f:
            for line in f:
                data[i].append(line.strip().split(',')[data_mark])
    return data
staff_data = load_tab(staff_table)

print(type(staff_data['age'](0)))
