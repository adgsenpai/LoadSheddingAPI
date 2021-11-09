from setuptools import setup, find_packages

setup(
    name="EskomAPI",
    version="0.0.1",
    author="Ashlin Darius Govindasamy",
    author_email="adgrules@hotmail.com",
    url="https://adgstudios.co.za",
    description="Eskom RestAPI for LoadShedding in Python",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    license='MIT', 
    install_requires=["requests","BeautifulSoup"]
)