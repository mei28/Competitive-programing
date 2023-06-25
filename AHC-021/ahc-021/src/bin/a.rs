use proconio::{fastout, input};
use std::cmp::max;
use std::io::{self, BufRead};
use std::mem::swap;

#[derive(PartialEq, Eq, PartialOrd, Ord, Clone, Debug)]
pub struct Node {
    value: i32,
    left: Option<Box<Node>>,
    right: Option<Box<Node>>,
    depth: usize,
    position: (usize, usize),
}

impl Node {
    pub fn new(
        value: i32,
        left: Option<Box<Node>>,
        right: Option<Box<Node>>,
        depth: usize,
        position: (usize, usize),
    ) -> Self {
        Node {
            value,
            left,
            right,
            depth,
            position,
        }
    }
}
pub fn construct_tree(
    values: &Vec<i32>,
    start: usize,
    end: usize,
    depth: usize,
    position: (usize, usize),
) -> Option<Box<Node>> {
    if start >= end {
        return None;
    }

    let root_value = values[start];
    let mut i = start + 1;
    let mut next_depth_count = 1;

    while i + next_depth_count <= end {
        i += next_depth_count;
        next_depth_count += 1;
    }

    let left_child = construct_tree(values, start + 1, i, depth + 1, (depth + 1, position.1));
    let right_child = construct_tree(values, i, end, depth + 1, (depth + 1, position.1 + 1));

    Some(Box::new(Node::new(
        root_value,
        left_child,
        right_child,
        depth,
        position,
    )))
}
pub fn sort_tree(node: &mut Node) -> Vec<((usize, usize), (usize, usize))> {
    let mut swaps = Vec::new();
    let mut swapped = true;

    while swapped {
        swapped = sort_tree_recursive(node, &mut swaps, false);
    }

    swaps
}

fn sort_tree_recursive(
    node: &mut Node,
    swaps: &mut Vec<((usize, usize), (usize, usize))>,
    from_left: bool,
) -> bool {
    let mut swapped = false;

    if let Some(right) = node.right.as_mut() {
        swapped |= sort_tree_recursive(right, swaps, false);
        if !from_left && right.value > node.value {
            swaps.push((node.position, right.position));
            swap(&mut node.value, &mut right.value);
            swapped = true;
        }
    }

    if let Some(left) = node.left.as_mut() {
        swapped |= sort_tree_recursive(left, swaps, true);
        if left.value > node.value {
            swaps.push((node.position, left.position));
            swap(&mut node.value, &mut left.value);
            swapped = true;
        }
    }

    if swapped {
        if let Some(right) = node.right.as_mut() {
            swapped |= sort_tree_recursive(right, swaps, false);
        }
    }

    swapped
}

#[fastout]
fn main() {
    let mut pyramid_values = Vec::new();

    let stdin = io::stdin();

    for line in stdin.lock().lines().take(30) {
        let numbers: Vec<i32> = line
            .unwrap()
            .split_whitespace()
            .map(|s| s.parse().expect("parse error"))
            .collect();
        pyramid_values.extend(numbers);
    }

    let mut root = construct_tree(&pyramid_values, 0, pyramid_values.len(), 0, (0, 0))
        .expect("Tree could not be constructed");

    let mut swaps = Vec::new();
    let mut total_swaps = 0;

    for i in 0..pyramid_values.len() {
        let mut root = construct_tree(&pyramid_values, i, pyramid_values.len(), 0, (0, 0))
            .expect("Tree could not be constructed");

        let new_swaps = sort_tree(&mut root);
        if total_swaps + new_swaps.len() >= 10000 {
            swaps.extend(new_swaps.into_iter().take(10000 - total_swaps));
            break;
        }
        total_swaps += new_swaps.len();
        swaps.extend(new_swaps);
    }

    println!("{}", swaps.len());
    for swap in swaps {
        println!("{} {} {} {}", swap.0 .0, swap.0 .1, swap.1 .0, swap.1 .1);
    }
}
