from setuptools import setup
setup(
	name='GalvanizeApp',
	version='1.0',
	py_modules=['create-galvanize-app'],
	install_requires=[
		'Click'
	],
	entry_points='''
		[console_scripts]
		create-galvanize-app=app:cli
	'''
)