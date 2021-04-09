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
    echo "toto"

    function usage() {
        echo "--help    Shows this manual."
        echo "--build   Builds it."
    }

    function _build() {
        rm -rf $_curr_dir/{sdist,build}
        cd $_curr_dir
        python3 setup.py sdist
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
        pip3 install $_curr_dir/dist/*.tar.gz
    }

   case $1 in
       "--from-build") _from_build;;
       *) usage;;
   esac
}

[[ $# -lt 2 ]] && usage

while [[ $# -ge 2 ]];do
    arg=$1
    echo $arg
    case $arg in
        "build")
             shift
            _build $@;;
        "install")
            shift
            _install $@;;
        *)
            usage;;
    esac; shift
done
