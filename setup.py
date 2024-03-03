import setuptools

#UTF-8 is one of the most commonly used encodings, and Python often defaults to using it.
#UTF stands for “Unicode Transformation Format”, and the '8' means that 8-bit values are used in the encoding
with open("README.md", "r",encoding='utf-8') as f:
    long_description = f.read()

__version__ ="0.0.0"

REPO_NAME = "NLP-projects"
AUTHOR_USER_NAME = "salonib2301"
SRC_REPO = "nlp_summarizer" # in files src write the project name mentioned there 
AUTHOR_EMAIL = "salonib2301@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="NLP Projects",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/salonib2301/NLP-projects",
    project_urls={
        "Bug Tracker": "https://github.com/salonib2301/NLP-projects/issues",
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src"),
)