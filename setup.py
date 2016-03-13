from setuptools import setup,find_packages

setup(
        name='src',
        version='0.1',
        py_modules=find_packages('src'),
        install_requires=['Click'],
        entry_points= '''
        [console_scripts]
        as=src.as:cli
        '''
        )
