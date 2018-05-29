# # COLUMNS = ["id", "name", "age", "phone", "occupation", "hire_data"]
# # staff_table = "employee_info.txt"
# # def load_tab(file):
# #     data = {}
# #     with open(file, 'r', encoding='utf-8') as f:
# #         for i in COLUMNS:
# #             data[i] = []
# #             #data_mark = COLUMNS.index(i)
# #         for line in f:
# #             #data[i].append(data_mark)
# #             staff_id,name,age,phone,occupation,hire_data = line.split(',')
# #             data["id"].append(staff_id)
# #             data["age"].append(age)
# #             data["name"].append(name)
# #             data["phone"].append(phone)
# #             data["occupation"].append(occupation)
# #             data["hire_data"].append(hire_data)
# #         print(data)
# # load_tab(staff_table)
#
#
# # find name,age from staff_table where age > 20
# find * from staff_table where age > 22
# find * from staff_table where occupation = 运维
# find name,age from staff_table where hire_data like 2013
# find name,age from staff_table where occupation = HR
a = age > 2
find name,age from staff_table where age = 20
#     print(i)
update staff_table set age=25 where age=20
