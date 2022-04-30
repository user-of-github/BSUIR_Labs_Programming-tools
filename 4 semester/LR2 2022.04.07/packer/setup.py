from setuptools import setup, find_packages


setup(
    name='packer',
    version='0.1.0',
    description='Packer library',
    long_description='Task for 2d lab of Programming Tools subject',
    long_description_content_type='text/markdown',
    url='https://github.com/user-of-github/BSUIR_Labs_Programming-tools/tree/master/4%20semester',
    author='Slutskiy Nikita',
    author_email='nikitosminsk100@gmail.com',
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3.9'
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=['PyYAML', 'toml']
)
