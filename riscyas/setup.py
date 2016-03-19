from setuptools import setup, find_packages

setup(
        name='src',
        version='0.5',
        py_modules=find_packages('riscyas'),
        install_requires=['Click', 'bitstruct'],
        entry_points= '''
        [console_scripts]
        riscy-as=riscyas.assemble:cli
        ''',
        test_suite='nose.collector',
        tests_require=['nose']
        )
