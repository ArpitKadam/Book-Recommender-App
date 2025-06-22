from setuptools import setup, find_packages
from typing import List

def get_requirements() -> List[str]:
    requirements = []
    with open('requirements.txt') as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]
        
        if '-e .' in requirements:
            requirements.remove('-e .')

    return requirements

setup(
    name = "Book Recommender App",
    version = "0.0.0",
    author = "ArpitKadam",
    author_email="arpitkadam922@gmail.com",
    description="End to End Book Recommender System",
    packages=find_packages(),
    install_requires = get_requirements(),
)