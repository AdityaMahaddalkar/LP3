class DiffieHellman(object):
	def __init__(self, p, g, private_key, name):
		self.p = p
		self.g = g
		self.private_key = private_key
		self.name = name
	
	def generate_public_key(self):
		self.public_key = (self.g**self.private_key) % self.p
		
		return self.public_key
		
	def generate_shared_secret(self, received_public_key):
		self.key_received = received_public_key
		
		self.shared_secret = (received_public_key**self.private_key) % self.p
		
	def print_details(self):
		print('\nName          : {}'.format(self.name))
		print('P & G         : {} {}'.format(self.p, self.g))
		print('Public Key    : {}'.format(self.public_key))
		print('Shared Secret : {}\n'.format(self.shared_secret))
		

if __name__ == '__main__':
	
	a = DiffieHellman(23, 9, 4, 'a')
	b = DiffieHellman(23, 9, 3, 'b')
	
	key_received_at_b = a.generate_public_key()
	key_received_at_a = b.generate_public_key()
	
	a.generate_shared_secret(key_received_at_a)
	b.generate_shared_secret(key_received_at_b)
	
	a.print_details()
	b.print_details()
