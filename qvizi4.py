male = 0
female = 0
total = 0
fst_class = 0

with open('titanick.txt', 'r') as f1:
    header = f1.readline()
    for line in f1:
        data = line.strip().split(',')

        if len(data) > 4:
            gender = data[4]
            if gender == 'female':
                female += 1
            elif gender == 'male':
                male += 1
            total += 1

if total > 0:
    female_p = (female / total) * 100
    male_p = (male / total) * 100
else:
    female_p = male_p = 0

    if len(data) > 3:
        cls = data[3]
        if cls == '1':
            fst_class += 1
print(fst_class)

# dict = {
#     'passanger amount':
#         {
#             'female':314
#             'male':577
#             'female%':34%
#             'male%':64%
#             '1klasis mgzavrebi':
#         }
# }








#თეორია
#1)w, r, a,
#2)ახალი ფაილი შეიქმნება
#3)
#4)key