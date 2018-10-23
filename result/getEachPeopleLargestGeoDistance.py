# -------------------------------
# Yongkang Liu 849892
# this program is used to get the largest geo ditance of each user in top10
# -------------------------------
from math import radians, cos, sin, asin, sqrt
import csv


result=[]
def geodistance(lng1,lat1,lng2,lat2):
    radlat1=radians(lat1)
    radlat2=radians(lat2)
    a=radlat1-radlat2
    b=radians(lng1)-radians(lng2)
    s=2*asin(sqrt(pow(sin(a/2),2)+cos(radlat1)*cos(radlat2)*pow(sin(b/2),2)))
    earth_radius=6378.137
    s=s*earth_radius
    result.append(s)
    return result


with open('/Users/mushroom/PycharmProjects/test/venv/distance/geodistance10.csv', 'r') as f:
    reader = csv.reader(f)
    header = f.readline()
    for line in f:
        col = line.split(',')
        col[0] = float(col[0][:])
        col[1] = float(col[1][:])
        lng1 = col[0]
        lat1 = col[1]
        lat2 = -37.808163434
        lng2 = 144.957829502
        result = geodistance(lng1,lat1,lng2,lat2)
    a = max(result)
    b = result.index(max(result))
    l1=[]
    l1.append(a)
    l1.append(b)


with open('/Users/mushroom/PycharmProjects/test/venv/largestdistance.csv', 'a+') as f1:
    # f1.write(a)
    # f1.write(b)
    writer = csv.writer(f1)
    # writer.writerow(["distance", "index"])
    writer.writerow(l1)


