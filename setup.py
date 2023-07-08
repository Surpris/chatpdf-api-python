from setuptools import setup, find_packages

setup(
    name='chatpdf-api-python',
    version='0.1.0',
    description='Python wrapper for the ChatPDF API',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Surpris/chatpdf-api-python',
    author='Surpris',
    author_email='take90-it09-easy27@outlook.jp',
    license='Apache 2.0',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache 2.0',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
