from setuptools import setup, find_packages

setup(
    name="st-flexible-callout-elements",
    version="0.2.0",
    description="A Streamlit package for flexible, customizable status elements",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="João L. Neto",
    url="https://github.com/jlnetosci/st-flexible-callout-elements",
    packages=find_packages(),
    install_requires=[
        "streamlit>=1.13.0",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
