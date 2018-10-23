# -------------------------------
# Yongkang Liu 849892
# this program is used clearn the harvest tweets
# -------------------------------
import csv


file_list = {
    '/Users/mushroom/PycharmProjects/test/venv/top10 tweets users/1.csv'
    '/Users/mushroom/PycharmProjects/test/venv/top10 tweets users/2.csv'
    '/Users/mushroom/PycharmProjects/test/venv/top10 tweets users/3.csv'
    '/Users/mushroom/PycharmProjects/test/venv/top10 tweets users/4.csv'
    '/Users/mushroom/PycharmProjects/test/venv/top10 tweets users/5.csv'
    '/Users/mushroom/PycharmProjects/test/venv/top10 tweets users/6.csv'
    '/Users/mushroom/PycharmProjects/test/venv/top10 tweets users/7.csv'
    '/Users/mushroom/PycharmProjects/test/venv/top10 tweets users/8.csv'
    '/Users/mushroom/PycharmProjects/test/venv/top10 tweets users/9.csv'
    '/Users/mushroom/PycharmProjects/test/venv/top10 tweets users/10.csv'
    }


for f in file_list:
    with open(f,'r') as f:
        reader = csv.reader(f)
        header = f.readline()
        column = [row[2] for row in reader]
        column1 = [x for x in column if x != '']

    with open('/Users/liuyongkang/Downloads/test/venv/geodistance.csv', 'w') as f1:
        writer = csv.writer(f1)
        writer.writerow(["lng","lat"])

        for i in range(len(column1)):
            new = []
            col = eval(column1[i])
            value = list(col.values())[1]
            new.append(value)
            writer.writerows(new)





