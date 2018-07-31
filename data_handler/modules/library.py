from time import time

def timer(func):
	"""
	Decorator to time function run time.
	Useful for testing efficiency later.
	"""
	def wrapper():
		before = time()
		val = func(*args, **kwargs)
		after = time()
		print('Elapsed Time: {0:5f}'.format(after - before))
		return val
	return wrapper