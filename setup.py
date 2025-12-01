from setuptools import setup, find_packages

setup(
    name='snowflake-intelligence-agent',
    version='0.1.0',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'snowflake-snowpark-python',
        'snowflake-cortex',
        'snowflake-connector-python',
        'pandas',
    ],
    author='Your Name',
    author_email='your.email@example.com',
    description='A self-directed, multi-modal AI system for Snowflake.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/your-username/snowflake-intelligence-agent-v2',
    license='MIT',
)
