#!/bin/bash

function oj_t() {
    # set -euC
    cargo build --release --bin solve
    oj t -c ./target/release/solve
}
