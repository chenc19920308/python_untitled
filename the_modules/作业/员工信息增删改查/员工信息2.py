import os
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

def save_db():
    """
    把内存数据存入硬盘
    :return:
    """
    f = open("%s.new"%staff_table ,'w',encoding='utf-8')
    for index,staff_id in enumerate(staff_data['id']):
        row = []
        for col in COLUMNS:
            row.append(staff_data[col][index])
        f.write(",".join(row))
    f.close()
    os.rename("%s.new"%staff_table,staff_table )

def syntax_find(matched_data,statement):
    #finf name,age from staff_table   # 解析cmd 头部信息，并执行。
    # 第一步:得到["name","age"] 形式。
    obj_val = statement.strip().split("from")[0][4:].strip().split(",")
    print(obj_val)
    if '*' in obj_val:
        for g in matched_data:
            print(g)
    # 获取 staff_data中name，age对应的信息。
    else:
        finall_data = []
        for row in matched_data:
            filter_val = []
            for val in obj_val:
                val_index = COLUMNS.index(val)
                filter_val.append(row[val_index])
            finall_data.append(filter_val)
        for k in finall_data:
            print(k)
    print_log("Match %s data"%len(matched_data))
def syntax_add(matched_data,statement):
    pass
def syntax_delete(matched_data,statement):
    pass
def syntax_update(matched_data,statement):
    """
    :param matched_data: [['1','Alex Li',……],[],……[]]
    :param statement: update staff_table set age = 25
    :return:
    """
    formula_row = statement.split('set')
    if len(formula_row) > 1:  # have 'set'
        col_name,col_value = formula_row[1].strip().split('=')  #age   25
        for v in matched_data:
            staff_id = v[0]
            staff_id_index = staff_data['id'].index(staff_id)
            staff_data[col_name][staff_id_index] = col_value
        print(staff_data)
        save_db()
    else:
        print('Wrong grammer:No keyword of "set"',"error")
    print_log("Match %s data" % len(matched_data))

def op_gt(value,condition):  # age  22
    matched_data = []
    for index,item_val in enumerate(staff_data[value.strip()]):
        if float(item_val) > float(condition):
            records = []
            for val in COLUMNS:
                records.append(staff_data[val][index])
            matched_data.append(records)
    print("matched:",matched_data)
    return matched_data
def op_lt(value,condition):
    matched_data = []
    for index, item_val in enumerate(staff_data[value.strip()]):
        if float(item_val) < float(condition):
            records = []
            for val in COLUMNS:
                records.append(staff_data[val][index])
            matched_data.append(records)
    print("matched:", matched_data)
    return matched_data
def op_eq(value,condition):
    matched_data = []
    for index, item_val in enumerate(staff_data[value.strip()]):
        if item_val == condition:  # 思考为什么要这样写？
            records = []
            for val in COLUMNS:
                records.append(staff_data[val][index])
            matched_data.append(records)
    print("matched:", matched_data)
    return matched_data
def op_like(value,condition):
    matched_data = []
    for index, item_val in enumerate(staff_data[value.strip()]):
        if condition in item_val:   #这样的也是可以的？？
            records = []
            for val in COLUMNS:
                records.append(staff_data[val][index])
            matched_data.append(records)
    print("matched:", matched_data)
    return matched_data

def syntax_where(statement):  #   age > 22    #解析where条件语句
    operator = {">":op_gt,
                "<":op_lt,
                "=":op_eq,
                "like":op_like}
    for select_type,select_val in operator.items():
        if select_type in statement:
            main_condit, remain_condit = statement.strip().split(select_type)
            matched_data = select_val(main_condit.strip(),remain_condit.strip())
    return matched_data

def syntax_parser(statement):  #解析输入语句，并执行相关操作
    "'语法格式：[find,"
     # find name,age from staff_table where age > 22
    syntax_list = {"find":syntax_find,
                   "del":syntax_delete,
                   "updata": syntax_update,
                   "add":syntax_add}
    if statement.split(" ")[0] in ("find", "update", "add", "del"):
        if 'where' in statement:
            main_clause,remain_clause = statement.split('where')
            matched_data = syntax_where(remain_clause)
            syntax_find(matched_data, main_clause)
        else:
            matched_data = []
            for index,staff_id in enumerate(staff_data['id']):
                record = []
                for col in COLUMNS:
                    record.append(staff_data[col][index])
                matched_data.append(record)
            main_clause = statement
        cmd_action = main_clause.split()[0]
        if cmd_action in syntax_list:
            syntax_list[cmd_action](matched_data,main_clause )
    else:
        print_log("Wrong grammer")

def main():  #主程序逻辑
    '"让用户输入语句，并不断得循环执行"'
    while True:
        cmd = input("statement_iuput:").strip()
        if not cmd: continue
        else:
            syntax_parser(cmd)
main()



