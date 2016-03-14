from setuptools import setup,find_packages

setup(
        name='src',
        version='0.1',
        py_modules=find_packages('src'),
        install_requires=['Click', 'bitstruct'],
        entry_points= '''
        [console_scripts]
        test2=src.instruction.instrstruct:test
        as=src.as:cli
        '''
        )
