from setuptools import setup, find_packages
from typing import List

def get_requirements(file_path: str) -> List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements]
        if 'HYPEN_E_DOT' in requirements:  # Assuming 'HYPEN_E_DOT' is a string you're checking for
            requirements.remove('HYPEN_E_DOT')
    return requirements

setup (
    name='ml_project',
    version='0.0.1',
    author='Divyansh',
    author_email='bt22cse003@iiitn.ac.in',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
