import time
import logging
class KeyGen:
	def __init__(self, initial_key='1111111111'):
		self.__key = initial_key
		
	def P10(self, key):
		key_list = list(str(key))
		key_holder = []
		key_holder.append(key_list[2])
		key_holder.append(key_list[4])
		key_holder.append(key_list[1])
		key_holder.append(key_list[6])
		key_holder.append(key_list[3])
		key_holder.append(key_list[9])
		key_holder.append(key_list[0])
		key_holder.append(key_list[8])
		key_holder.append(key_list[7])
		key_holder.append(key_list[5])
		generated_key = str(''.join(key_holder))
		
		logging.info(f'P10 generated key for {key} is {generated_key}')
		
		return generated_key
		
	def P8(self, key):
		key_list = list(str(key))
		key_holder = []
		key_holder.append(key_list[5])
		key_holder.append(key_list[2])
		key_holder.append(key_list[6])
		key_holder.append(key_list[3])
		key_holder.append(key_list[7])
		key_holder.append(key_list[4])
		key_holder.append(key_list[9])
		key_holder.append(key_list[8])
		generated_key = str(''.join(key_holder))
		
		logging.info(f'P8 generated key for {key} is {generated_key}')
		
		return generated_key
		
	def FiveBitLeftShift(self, key):
		key_list = list(str(key))
		
		holder_bit = key_list[0]
		del key_list[0]
		key_list.insert(4, holder_bit)
		
		holder_bit = key_list[5]
		del key_list[5]
		key_list.insert(9, holder_bit)
		
		generated_key = str(''.join(key_list))
		
		logging.info(f'5 bit left shift for {key} is {generated_key}')
		
		return generated_key
		
	def generate_k1(self):
		
		key = self.__key
		k1_key = self.P8(self.FiveBitLeftShift(self.P10(key)))
		
		logging.debug(f'K1 generated key for {key} is {k1_key}')
		
		return k1_key
		
	def generate_k2(self):
		
		key = self.__key
		k2_key = self.P8(self.FiveBitLeftShift(self.FiveBitLeftShift(self.P10(key))))
		
		logging.debug(f'K2 generated key for {key} is {k2_key}')
		
		return k2_key
		

# Testing
'''
if __name__ == '__main__':
	logging.basicConfig(level=logging.DEBUG)
	kg = KeyGen(1010000010)
	k1_key = kg.generate_k1()
	k2_key = kg.generate_k2()
'''		
