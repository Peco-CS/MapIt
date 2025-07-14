from setuptools import setup, find_packages

setup(
    name='MapIt',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,  # This ensures non-Python files are included
    install_requires=[
        'dash',
        'dash-bootstrap-components',
    ],
)