import math


class KNN(object):
	def __init__(self,k):
		self.num_of_classes = 2
		self.test_point = None
		self.k = k
		self.data = []
		
		self.dist_list = []
		self.class_count = dict()
		
	def read_data(self, file_path):
		with open('data/sample.csv') as file:
			lines = file.readlines()
			for line in lines[1:]:
				self.data.append([int(x) for x in line.split(',')])
				
	def compute_distances(self):
		compute_dist = lambda point1, point2: math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

		for train_point in self.data:
			self.dist_list.append((compute_dist(train_point, self.test_point), train_point[2]))


		self.dist_list.sort(key=lambda x:x[0])
		
		
	def calculate_class_count(self):
		for i in range(1, self.num_of_classes + 1):
			self.class_count[i] = 0
	
		for c in self.dist_list[0:self.k]:
			self.class_count[c[1]] += 1
			
			
			
	def predict(self, test_point):
		self.test_point = test_point
		self.compute_distances()
		self.calculate_class_count()
		class_of_test_point = None
		count = -1
		for key, value in self.class_count.items():
			if value > count:
				count = value
				class_of_test_point = key
				
		print('Class of Point ', test_point, ' is : ',class_of_test_point)
		
if __name__ == '__main__':
	test_point = (6,6)
	
	classifier = KNN(3)
	classifier.read_data('data/sample.csv')
	classifier.predict(test_point)
	
			
