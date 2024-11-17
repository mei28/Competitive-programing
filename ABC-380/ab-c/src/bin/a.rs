use permutohedron::LexicalPermutation;
use proconio::input;

fn main() {
    input! {n:String}

    let mut a = vec!['1', '2', '2', '3', '3', '3'];

    while a.next_permutation() {
        let t = a.iter().collect::<String>();
        if t == n {
            println!("Yes");
            return;
        }
    }
    println!("No");
}
