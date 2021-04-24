from setuptools import setup
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
setup(
    name='Test_Load',
    version='1.0.0',
    packages=setup.find_packages(where="src"),
    url='https://github.com/huynhquoc1990/Test_Load.git',
    license='MIT',
    author='Quoc',
    author_email='huynhquoc1990@gmail.com',
    description='Demo Load Code To Pypi',
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    python_requires=">=3.6"
)
