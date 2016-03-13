#!/bin/bash 

LINELENGTH=80
#TODO: Get the Line length param in there...
LINEBAR="$(perl -e 'print "#" x 80')"

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
SRCDIR="$DIR/src"

cat << EOF
$LINEBAR
### This script is not implemented yet! ### 
$LINEBAR
EOF

#TODO: Add detection for pip.

export PYTHONPATH=$SRCDIR:$PYTHONPATH

[ -z "${VENV_DIR:-}" ] && export VENV_DIR="$DIR/venv"

[ -z "${PYTHON_BIN:-}" ] && export PYTHON_BIN="python3"


# Install the required packages.
{
    echo Creating virtual environment directory \"venv\"

    virtualenv -q $VENV_DIR #1> /dev/null

    source ${VENV_DIR}/bin/activate

    echo Installing required packages to \"venv\"

    pip install --compile --upgrade -r pip-require.txt

}

cd $SRCDIR && $PYTHON_BIN as.py

exit
