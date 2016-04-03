#!/bin/bash
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

clean () {

EXTRA="`find "$DIR" | grep -E -e ".*[.]{1}egg.*" -e "__pycache__" `"

rm -rf *.egg-info build dist venv $EXTRA

}

if [ "$1" = 'clean' ]; then
clean

else

virtualenv --clear -p /usr/bin/python3 venv --no-site-packages &&

source venv/bin/activate  &&

pip3 install -e $DIR &&

alias test_package='python $DIR/setup.py test' &&
alias develop='source $DIR/develop.sh'  &&

printf "
==================================================================
SUCCESS

    You are now running a virtual environment for RISCY-AS run 
    'deactivate' to leave the environment. Run 'develop clean' to
    clean up.

==================================================================
"

fi
