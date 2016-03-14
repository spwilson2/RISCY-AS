#!/bin/bash 

export BIN=$1

LINELENGTH=80
#TODO: Get the Line length param in there...
LINEBAR="$(perl -e 'print "#" x 80')"

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
SRCDIR="$DIR/src"



# Optionally clean the tree.
if [ "$1" = "clean" ]; then

cat << EOF
$LINEBAR
### Cleaning. ### 
$LINEBAR
EOF

TO_CLEAN="src.egg-info venv"
PYC_FILES="`find | grep -E -e "*.pyc$" -e "__pycache__" -e "*.out"`"
TO_CLEAN="$PYC_FILES $TO_CLEAN"
rm -rf $TO_CLEAN; exit $?;

fi


export PYTHONPATH=$SRCDIR:$PYTHONPATH

[ -z "${VENV_DIR:-}" ] && export VENV_DIR="$DIR/venv"

[ -z "${PYTHON_BIN:-}" ] && export PYTHON_BIN="python3"

if [ $PYTHON_BIN = "python3" ] 
then
    PIP_BIN=pip3
else
    PIP_BIN=pip
fi

# Check for pip and virtualenv
command $PIP_BIN -v >/dev/null 2>&1 || 
{ echo >&2 "$PIP_BIN not installed.  Aborting."; exit 1; }

command virtualenv --version >/dev/null  || 
{ echo >&2 "virtualenv not installed. Try $PIP_BIN install virtualenv."; exit 1; }


# Install the required packages.
(
    echo Creating virtual environment directory \"venv\"

    virtualenv -p $PYTHON_BIN $VENV_DIR #1> /dev/null

    echo $VENV_DIR

    source $VENV_DIR/bin/activate

    #TODO: On release will need to change from editable too...?
    $PIP_BIN install --editable $DIR

    # Run the program.
    $BIN "${@:2}"
)

exit
