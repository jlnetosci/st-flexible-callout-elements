from setuptools import setup, find_packages

setup(
    name="st-flexible-status-elements",
    version="0.1.0",
    description="A Streamlit package for flexible, customizable status elements",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Your Name",
    author_email="your.email@example.com",
    url="https://github.com/yourusername/st-flexible-status-elements",
    packages=find_packages(),
    install_requires=[
        "streamlit>=0.87",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
