from setuptools import setup,find_packages

setup(
        name='src',
        version='0.1',
        py_modules=find_packages('src'),
        install_requires=['Click', 'bitstruct'],
        #TODO: Add selftest entrypoints.
        entry_points= '''
        [console_scripts]
        selftest=src.instruction.instrstruct:test
        as=src.as:cli
        '''
        )
