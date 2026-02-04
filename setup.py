from setuptools import setup, find_packages

setup(
    name="sn-orchestra",
    version="1.0.0",
    description="The Unified Intelligence Layer for Bittensor",
    author="Your Name/Organization",
    packages=find_packages(),
    install_requires=[
        "bittensor>=7.0.0",
        "pydantic>=2.0.0",
        "numpy",
    ],
    python_requires=">=3.10",
)
