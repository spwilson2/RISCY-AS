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


export PYTHONPATH=$SRCDIR:$PYTHONPATH

[ -z "${VENV_DIR:-}" ] && export VENV_DIR="$DIR/venv"

[ -z "${PYTHON_BIN:-}" ] && export PYTHON_BIN="python3"

if $PYTHON_BIN == "python3" 
then
    PIP_BIN=pip3
else
    PIP_BIN=pip
fi


# Check for pip and virtualenv
command $PIP_BIN -v >/dev/null 2>&1 || 
{ echo >&2 "$PIP_BIN not installed.  Aborting."; exit 1; }

command virtualenv -v >/dev/null 2>&1 || 
{ echo >&2 "virtualenv not installed. Try $PIP_BIN install virtualenv."; exit 1; }


# Install the required packages.
{
    echo Creating virtual environment directory \"venv\"

    virtualenv -q $VENV_DIR #1> /dev/null

    source ${VENV_DIR}/bin/activate

    echo Installing required packages to \"venv\"

    $PIP_BIN install --compile --upgrade -r pip-require.txt

}

# Run the program.
cd $SRCDIR && $PYTHON_BIN as.py $@

exit
