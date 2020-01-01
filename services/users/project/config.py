

class BaseConfig:
	"""Base configuration"""
	TESTING = False
	# DEBUG = True

class DevelopmentConfig(BaseConfig):
	"""Development configuration"""
	pass

class TestingConfig(BaseConfig):
	"""Testing configuration"""
	TESTING = True

class ProductionConfig(BaseConfig):
	"""Production configuration"""
	# DEBUG = False
	pass
