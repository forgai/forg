import re
from pathlib import Path

from setuptools import find_packages, setup


def get_version(package: str) -> str:
    version = (Path("src") / package / "__init__.py").read_text()
    match = re.search("__version__ = ['\"]([^'\"]+)['\"]", version)
    assert match is not None
    return match.group(1)


setup(
    name="forgai,
    description=(
        "Deploy serverless AI agents in the cloud. "
        "Orchestrate collaboration between agents via the Forg Python SDK."
    ),
    version=get_version("forgai),
    packages=find_packages("src"),
    package_dir={"": "src"},
    include_package_data=True,
    zip_safe=False,
    python_requires=">=3.8",
    install_requires=["requests==2.31.0", "websockets==12.0"],
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
)
