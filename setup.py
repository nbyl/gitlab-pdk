import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pdk-nbyl",
    version="0.0.1",
    author="Nicolas Byl",
    author_email="nico@nicolas-byl.eu",
    scripts=['bin/pdk'],
    description="A pipeline development kit (PDK) for gitlab pipelines",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nbyl/gitlab-pdk",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache License",
        "Operating System :: OS Independent",
    ],
)
