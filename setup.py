# setup.py
from pathlib import Path
from setuptools import find_namespace_packages, setup

# Load packages from requirements.txt
BASE_DIR = Path(__file__).parent
with open(Path(BASE_DIR, "requirements.txt"), "r") as file:
    required_packages = [ln.strip() for ln in file.readlines()]

# Define our package
setup(
    name="tagifai",
    version=0.1,
    description="Classify machine learning projects.",
    author="Ganesh Jainarain",
    author_email="GaneshJ2399@gmail.com",
    python_requires=">=3.7",
    packages=find_namespace_packages(),
    install_requires=[required_packages],
)