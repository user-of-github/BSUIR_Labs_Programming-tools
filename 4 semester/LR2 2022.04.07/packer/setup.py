from setuptools import setup


setup(
    name='packer',
    version='1.0.0',
    description='My completed lab 2 - AutoPacker for different kinds of Python objects',
    packages=['packer',
              'packer/formats',
              'packer/formats/dictionary',
              'packer/formats/json',
              'packer/formats/yaml',
              'packer/formats/toml',
              'packer/utils'],
    author='Slutski Nikita | @user-of-github',
    install_requires=['PyYaml == 6.0',
                      'toml == 0.10.2'],
    entry_points={
        'console_scripts': [
            'console_utility = packer.console_utility:main'
        ]}
)
