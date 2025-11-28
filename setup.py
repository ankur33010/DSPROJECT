from setuptools import setup, find_packages
from typing import List

def get_requiements(file_path: str) -> list[str]:
    with open(file_path) as file:
        requirements = file.readlines()
        requirements = [req.strip() for req in requirements if req.strip() and not req.startswith("#") and not req.startswith("-") ]
    return requirements



setup(
name="DSPROJECT",
version="1.0.0",
author="Ankur",
author_email="ankurtyagi33010@gmail.com",
packages=find_packages(),
install_requires=get_requiements("requirements.txt"))

