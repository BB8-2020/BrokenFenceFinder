from setuptools import find_packages, setup

install_requires = [
]

setup(
    name='BrokenFenceFinder',
    version='0.0',
    description='Broken fence finder model for parrot drones',
    author='David Demmers',
    author_email='david.demmers@student.hu.nl',
    packages=find_packages(),
    install_requires=install_requires,
    dependency_links=[
        "git+https://github.com/BB8-2020/BrokenFenceFinder",
    ],
)
