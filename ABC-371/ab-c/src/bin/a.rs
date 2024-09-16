use proconio::{input, marker::Chars}; // Add this import for using Itertools

fn main() {
    let m = {
        let mut n = vec![];
        for _ in 0..3 {
            input! {
                a: char
            }
            n.push(a);
        }
        n
    };

    // covert c++ to rust
    // int main() {
    //     char a, b, c;
    //     cin >> a >> b >> c;
    //     if(a != b)
    //         cout << "A" << endl;
    //     else if(a == c)
    //         cout << "B" << endl;
    //     else
    //         cout << "C" << endl;
    // }

    if m[0] != m[1] {
        println!("A");
    } else if m[0] == m[2] {
        println!("B");
    } else {
        println!("C");
    }
}
