from key_gen import KeyGen
import logging

class SDES:
	def __init__(self):
		
		self.s0 = [['01', '00', '11', '10'], 
			['11', '10', '01', '00'], 
			['00', '10', '01', '11'], 
			['11', '01', '11', '10']]
		self.s1 = [['00', '01', '10', '11'], 
			['10', '00', '01', '11'], 
			['11', '00', '10', '00'], 
			['10', '01', '00', '11']]
		
	
	def IP(self, text):
		text_list = list(str(text))
		holder = []
		holder.append(text_list[1])
		holder.append(text_list[5])
		holder.append(text_list[2])
		holder.append(text_list[0])
		holder.append(text_list[3])
		holder.append(text_list[7])
		holder.append(text_list[4])
		holder.append(text_list[6])
		
		gen_text = str(''.join(holder))
		
		logging.info(f'IP function on {text} gives {gen_text}')
		
		return gen_text
		
	def IPinverse(self, text):
		text_list = list(str(text))
		holder = []
		holder.append(text_list[3])
		holder.append(text_list[0])
		holder.append(text_list[2])
		holder.append(text_list[4])
		holder.append(text_list[6])
		holder.append(text_list[1])
		holder.append(text_list[7])
		holder.append(text_list[5])
		
		gen_text = str(''.join(holder))
		
		logging.info(f'IP-1 function on {text} gives {gen_text}')
		
		return gen_text
		
	def f(self, text, subkey):
		# Expansion permutation
		text_list = list(str(text))
		key_list = list(str(subkey))
		
		text_holder = []
		text_holder.append(text_list[3])
		text_holder.append(text_list[0])
		text_holder.append(text_list[1])
		text_holder.append(text_list[2])
		text_holder.append(text_list[1])
		text_holder.append(text_list[2])
		text_holder.append(text_list[3])
		text_holder.append(text_list[0])
		
		# change datatypes of lists
		text_holder = [int(x) for x in text_holder]
		key_list = [int(x) for x in key_list]
		
		# EXOR of subkey
		
		for i in range(len(key_list)):
			text_holder[i] ^= key_list[i]
			
		# Calculate S_box values
		s0_row, s0_col = int(str(text_holder[0])+str(text_holder[3]), 2), int(str(text_holder[1])+str(text_holder[2]), 2)
		
		s0_bin_value = self.s0[s0_row][s0_col]
		
		s1_row, s1_col = int(str(text_holder[4])+str(text_holder[7]), 2), int(str(text_holder[5])+str(text_holder[6]), 2)
		
		s1_bin_value = self.s1[s1_row][s1_col]
		
		s_block_value = s0_bin_value+s1_bin_value
		
		# Permute bits
		
		s_block_value_holder = list(s_block_value)
		gen_holder = []
		gen_holder.append(s_block_value_holder[1])
		gen_holder.append(s_block_value_holder[3])
		gen_holder.append(s_block_value_holder[2])
		gen_holder.append(s_block_value_holder[0])
		logging.info(f'gen_holder: {gen_holder}')
		
		gen_text = ''.join(gen_holder)
		
		logging.info(f'f function for {text} and subkey {subkey} is {gen_text}')
		
		return gen_text

	def fk(self, text, subkey):
		
		# fk(L, R) = (L ^ f(R, SK), R)
		
		l = text[:4]
		r = text[4:]
		logging.info(f'l = {l}, r = {r}')
		f_holder = self.f(r, subkey)
		logging.info(f'f_holder: {f_holder}')
		l = list(map(int, list(l)))
		
		f_holder = list(map(int, f_holder))
		
		l = [str(x^y) for x, y in zip(l, f_holder)]
		l = ''.join(l)
		
		logging.info(f'fK of text {text} on subkey {subkey} gives {l+r}')
		
		return l+r
		
	def switch(self, text):
		
		# Interchange left and right 4 bits
		l = text[:4]
		r = text[4:]
		
		logging.info(f'SW on {text} gives {r+l}')
		
		return r+l
		
	def encrypt(self, plain_text):
		'''
		Note: for function fk, the key order is k1 then k2
		
		'''
		kg = KeyGen('1110111010')
		k1 = kg.generate_k1()
		k2 = kg.generate_k2()
		
		ip_output = self.IP(plain_text)
		fk1 = self.fk(ip_output, k1)
		sw = self.switch(fk1)
		fk2 = self.fk(sw, k2)
		ip_inv_output = self.IPinverse(fk2)
		
		final_op = ip_inv_output
		
		print(f'Final encrypted output for {plain_text} is {final_op}')
		
		return final_op
		
	def decrypt(self, cipher):
		'''
		Note: For functions fk, the key order is k2 then k1		
		'''
		kg = KeyGen('1110111010')
		k1 = kg.generate_k1()
		k2 = kg.generate_k2()
		
		ip_output = self.IP(cipher)
		fk1 = self.fk(ip_output, k2)
		sw = self.switch(fk1)
		fk2 = self.fk(sw, k1)
		ip_inv_output = self.IPinverse(fk2)
		final_op = ip_inv_output
		
		'''
		ip_inv_output = self.IPinverse(cipher)
		fk2 = self.fk(ip_inv_output, k2)
		sw = self.switch(fk2)
		fk1 = self.fk(sw, k1)
		ip_output = self.IP(fk1)
		final_op = ip_output
		'''
		print(f'Final decrypted output for {cipher} is {final_op}')
		
		return final_op
		
		
# Testing

def convert_sentence_to_8_bit_stream(sentence):
	stream = []
	for letter in sentence:
		ascii_val = ord(letter)
		bin_val = bin(ascii_val)[2:]
		bin_val = '0'*(8-len(list(bin_val))) + bin_val
		stream.append(bin_val)
	print(stream)
	return stream
	
def encrypt_stream(stream):
	enc = SDES()
	encryption = []
	for binary_val in stream:
		encryption.append(enc.encrypt(binary_val))
		
	print(f'Encrypted val: {encryption}')
	return encryption
	
def decrypt_stream(encrypted_stream):
	enc = SDES()
	decryption = []
	for binary_val in encrypted_stream:
		decryption.append(enc.decrypt(binary_val))
	print(f'Decrypted val: {decryption}')
	return decryption
			
def convert_8_bit_stream_to_sentence(stream):
	ascii_list = []
	for binary in stream:
		ascii_list.append(chr(int(binary,2)))
	print(ascii_list)
	return ''.join(ascii_list)
	
if __name__ == '__main__':
	#logging.basicConfig(level=logging.DEBUG)
	
	bin_stream = convert_sentence_to_8_bit_stream(input())
	encryption = encrypt_stream(bin_stream)
	decryption = decrypt_stream(encryption)
	final_output = convert_8_bit_stream_to_sentence(decryption)
	print(final_output)
	'''
	ency = SDES()
	cipher = ency.encrypt('11111000')
	ency.decrypt(cipher)
	'''
		
	
		
