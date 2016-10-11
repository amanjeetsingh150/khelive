from setuptools import setup, find_packages

setup(
    name='khelive',
    version='0.0',
    description='Live cricket and football scores',
    author='amanjeetsingh',
    license='MIT',
    author_email='amanjeetsingh150@gmail.com',
    url='https://github.com/amanjeetsingh150/khelive',
    packages=find_packages(),
    install_requires=[
    "beautifulsoup4",
    "urllib2"
    ],
    entry_points={
    'console_scripts': [
    'khelive = khelive.main:main'
    ],
    }
)    
