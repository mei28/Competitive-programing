use petgraph::algo::toposort;
use petgraph::graph::{DiGraph, NodeIndex};
use proconio::input;

fn main() {
    input! {
        n: usize,
        m: usize,
        conditions: [(usize, usize); m],
    }

    // Initialize a graph with `n` vertices and no edges
    let mut graph = DiGraph::new();

    // Explicitly add nodes to the graph to ensure the indices are valid
    for i in 0..n {
        graph.add_node(i);
    }

    // Add edges to the graph based on the conditions
    for (a, b) in conditions {
        // Ensure that the indices are 0-based for the graph
        graph.add_edge(NodeIndex::new(a - 1), NodeIndex::new(b - 1), ());
    }

    // Attempt to topologically sort the graph
    match toposort(&graph, None) {
        Ok(sorted) => {
            // If the sort is successful, output the sorted node indices
            for node_index in sorted {
                println!("{}", node_index.index() + 1); // Convert back to 1-based index
            }
        }
        Err(_) => {
            // If there is a cycle, output -1
            println!("-1");
        }
    }
}

