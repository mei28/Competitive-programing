#!/bin/bash

function oj_d() {
    # set -euC
    
    function show_help() {
        echo -e "usage: oj_d <contest_id> <problem_id>"
        echo -e "contest_id:\t(ex. abc297)"
        echo -e "problem_id:\t(ex. c)"
    }

    if [[ $# == 0 ]]; then
        show_help
        return 1
    fi

    if [[ "${1}" == "https://"* ]]; then
        if [[ $# != 1 ]]; then
            show_help
            return 1
        fi
        if [[ -d ./test ]]; then
            rm -r ./test
        fi
        url="${1}"
    else
        if [[ $# != 2 ]]; then
            show_help
            return 1
        fi
        if [[ -d ./test ]]; then
            rm -r ./test
        fi
        url=$(acc url "${1}" "${1}_${2}")
    fi

    oj d "${url}"
}
