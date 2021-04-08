from setuptools import find_packages, setup

DEVELOPER = True

install_requires = []

if DEVELOPER:
    with open('requirements-dev.txt') as file:
        install_requires.extend(file.read().splitlines())

with open('requirements.txt') as file:
    install_requires.extend(file.read().splitlines())


setup(
    name='BrokenFenceFinder',
    version='0.0',
    description='Broken fence finder model for parrot drones',
    author='David Demmers',
    author_email='david.demmers@student.hu.nl',
    packages=find_packages(),
    install_requires=install_requires
)
