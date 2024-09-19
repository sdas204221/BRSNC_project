from setuptools import setup, find_packages

# Read dependencies from requirements.txt
def parse_requirements(filename):
    with open(filename, 'r') as f:
        return f.read().splitlines()

setup(
    name='image_encryption_project',
    version='0.1',
    packages=find_packages(where="src"),  # Specify 'src' where your packages are located
    package_dir={"": "src"},  # Set 'src' as the root directory for the package
    install_requires=parse_requirements('requirements.txt'),  # Dynamically read requirements
)
