name = []
name.append("old.river")
name.append("rain")
name.extend(["jack","shanshan","peiqi","black_girl"])
name.insert(5,"alex")
name[3]="姗姗"
name.insert(2,["oldboy","oldgirl"])
A = name.index("peiqi")
B = [1,2,3,4,2,5,6,2]
name.extend(B)
C = name[4:7]
D = name[2:10:2]
E = name[-3:]
count = 0
for each in name:
    if count % 2 == 0:
        each = -1
    count += 1
    print(each,count)

    还有其他的方式




