from setuptools import setup


setup(
    name="packerByUserOfGithub",
    packages=[
        "packer",
        "packer/utils",
        "packer/formats",
        "packer/formats/dictionary",
        "packer/formats/dictionary",
        "packer/formats/json",
        "packer/formats/yaml",
        "packer/formats/toml",
    ],
    version="1.0.0",
    author="Nikita Slutski (user-of-github)",
    scripts=["bin/packerByUserOfGithub"]
)