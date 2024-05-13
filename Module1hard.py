Students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
Students = sorted(list(Students))
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
avg_grades = [sum(int(el) for el in i) for i in grades]
len_grades = [len(i) for i in grades]
for i in range(len(avg_grades)):
    avg_grades[i] = avg_grades[i] / len_grades[i]
print(dict(zip(Students, avg_grades)))
