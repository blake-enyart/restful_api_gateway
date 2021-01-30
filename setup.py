import setuptools


with open("README.md") as fp:
    long_description = fp.read()


setuptools.setup(
    name="restful_api_gateway",
    version="0.0.1",
    description="A FastAPI, CDK, and Docker RESTful API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Blake Enyart",
    package_dir={"": "restful_api_gateway"},
    packages=setuptools.find_packages(where="restful_api_gateway"),
    install_requires=[
        "aws-cdk.core==1.76.0",
    ],
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Software Development :: Code Generators",
        "Topic :: Utilities",
        "Typing :: Typed",
    ],
)
