import math


num_of_classes = 2
test_point = (6,6)

k = 3


data = []

with open('data/sample.csv') as file:
	lines = file.readlines()
	for line in lines[1:]:
		data.append([int(x) for x in line.split(',')])


dist_list = []


compute_dist = lambda point1, point2: math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

for train_point in data:
	dist_list.append((compute_dist(train_point, test_point), train_point[2]))


dist_list.sort(key=lambda x:x[0])


class_count = dict()

for i in range(1,num_of_classes + 1):
	class_count[i] = 0
	
for c in dist_list[0:k]:
	class_count[c[1]] += 1
	
class_of_test_point = None
count = -1
for key, value in class_count.items():
	if value > count:
		count = value
		class_of_test_point = key

print('Class of Point ', test_point, ' is : ',class_of_test_point)
