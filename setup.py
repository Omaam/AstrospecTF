"""Setup.
"""
from setuptools import find_packages
from setuptools import setup

setup(
    name="astrospectf",
    version="0.0.1",
    description="Astronoycal Energy Spectrum Analysis in TensorFlow",
    author="Tomoki Omama",
    packages=find_packages(),
    install_requires=[
        "astropy",
        "tensorflow",
    ],
    classifiers=[
        "Development Status :: 1 - Planning"
    ],
)
