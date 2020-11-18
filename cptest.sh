#!/bin/bash

task_name=$1
test_dir=tests/${task_name}
base_url=${task_name%_*}

# make test directory
if [ ! -e ${test_dir} ]; then
    oj dl -d ${test_dir} https://atcoder.jp/contests/${base_url}/tasks/${task_name//-/_}
fi

oj test -c "python3 tasks/${task_name}.py" -d ${test_dir}
