from setuptools import setup, find_packages

setup(
    name="discord-logger-handler",
    version="0.1.2",
    description="A logging handler that sends log messages to Discord via webhooks.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Tharakeshavan Parthasarathy",
    author_email="ptharak01@gmail.com",
    url="https://github.com/Tharak01/Discord-Logger-Handler",
    packages=find_packages(),
    install_requires=[
        "requests>=2.20.0",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
