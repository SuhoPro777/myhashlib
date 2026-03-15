from setuptools import setup, find_packages

setup(
    name="myhashlib",           # Kutubxona nomi
    version="0.1.0",            # Versiya
    packages=find_packages(),    # Papkalarni avtomatik topadi
    description="Simple hash library",  
    author="Your Name",
    python_requires=">=3.6",
)