from setuptools import setup,find_packages

setup(
        name='src',
        version='0.1',
        py_modules=find_packages('riscyas'),
        install_requires=['Click', 'bitstruct'],
        #TODO: Add selftest entrypoints.
        entry_points= '''
        [console_scripts]
        selftest=riscyas.instruction.instrstruct:test
        as=riscyas.as:cli
        '''
        )
