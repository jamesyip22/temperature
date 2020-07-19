from setuptools import setup, find_packages

INSTALL_REQUIRES = [
    
]

with open('README.md') as f:
    long_description = f.read()

setup(
    name='jy_temperature',
    version='0.0.1',
    packages=find_packages(exclude=('tests')),
    url='https://github.com/jamesyip22/temperature',
    author='James',
    author_email='fake@email.com',
    description='Basic temperature conversion package',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='MIT',
    install_requires=INSTALL_REQUIRES,
)