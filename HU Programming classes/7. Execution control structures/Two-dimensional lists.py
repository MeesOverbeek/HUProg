studentencijfers = [ [95, 92, 86],[66, 75, 54],[89, 72, 100],[34, 0, 0] ]
def gemiddelde_per_student(studentencijfers):
    list1 = []
    for grade in studentencijfers:
        list1.append(int(sum(grade)/int(len(grade))))
    return list1

def gemiddelde_van_alle_studenten(studentencijfers):
    list2 = []
    for grade in studentencijfers:
        for s in grade:
            list2.append(s)
    gem = int(sum(list2)/int(len(list2)))
    return gem
print(gemiddelde_per_student(studentencijfers))
print(gemiddelde_van_alle_studenten(studentencijfers))