#!/bin/bash

function oj_t() {
    # set -euC
    function show_help() {
        echo -e "usage: oj_t <problem_id>"
        echo -e "problem_id:\t(ex. c)"
    }

    if [[ $# -eq 0 ]]; then
        show_help
        return 1
    fi
    cargo build --release --bin ${1}
    oj t -c ./target/release/${1}
}
