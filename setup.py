import setuptools

setuptools.setup(
    include_package_data=True,
    name='python_logging',
    version='0.0.2',
    description='Python logging tool for .log files',
    url='https://github.com/RoyalGr4pe/python_logging',
    author="Royal Gr4pe",
    author_email="njames.programming@gmail.com",
    packages=setuptools.find_packages(),
    install_requires=['loguru'],
    long_description="Python logging tool for .log file",
    license='MIT'
)
