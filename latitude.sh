DIR="$( cd -P "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
PYTHON=`which python`
cd $DIR
$PYTHON latitude $@
