#!/usr/bin/env bash

echo "I haven't been tested yet"

_me=`readlink -f $0`
_curr_dir=`dirname $_me`

function usage() {
    echo "$_me usage:"
    echo "  build --help"
    echo "  install --help"
}

function _build() {

    function usage() {
        echo "--help    Shows this manual."
        echo "--build   Builds it."
    }

    function _build() {
        rm -rf $_curr_dir/{sdist,build}
        python3 -m build $_curr_dir
    }

    case $1 in
        "--build") _build;;
        *) usage;;
    esac

}

function _install() {
    function usage() {
        echo "--help:       Shows this manual."
        echo "--from-build  Installs from manually generated build."
    }

    function _from_build() {
        pip3 install $_curr_dir/build/*.whl
    }
}

[[ $# -lt 2 ]] && usage
while [[ $# -gt 2 ]];do
    arg=$1
    
    case $arg in
        "build")
            _build $@;;
        "install")
            _install $@;;
        *)
            usage;;
    esac
done