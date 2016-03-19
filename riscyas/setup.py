from setuptools import setup,find_packages

setup(
        name='src',
        version='0.1',
        py_modules=find_packages('riscyas'),
        install_requires=['Click', 'bitstruct'],
        #TODO: Add selftest entrypoints.
        #selftest=riscyas.instruction.instrstruct:test
        #selftest=riscyas.instruction.util.parse:test
        entry_points= '''
        [console_scripts]
        riscy-as=riscyas.assemble:cli
        ''',
        test_suite='nose.collector',
        tests_require=['nose']
        )
