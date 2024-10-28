from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="path_friendly_filename_generator",
    version="0.1.0",
    author="Sammy",
    author_email="dussinsa01@esj.org",
    description="A package to generate path-friendly filenames across different operating systems.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/greenstorm5417/path_friendly_filename_generator",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[], 
)
