# setup.py

from setuptools import setup, find_packages

setup(
    name="my_library",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        # List your dependencies here
        # 'numpy',
        # 'pandas',
    ],
    author="Sudheer Kumar",
    author_email="sudheermsdvk@gmail.com",
    description="A library for loan prediction and more.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/Sudheerbmb/my_library",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
