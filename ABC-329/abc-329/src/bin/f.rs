use proconio::{input, marker::Usize1};
use std::collections::HashSet;


fn main(){
    input!{
        n:usize,
        q:usize,
        c: [Usize1; n],
        query:[(Usize1,Usize1);q],
    }

    let mut v = vec![HashSet::new();n];
    for i in 0..n{
        v[i].insert(c[i]);
    }

    for (a,b) in query{
        if v[a].len()< v[b].len(){
            let temp = v[a].clone();
            for x in temp{
                v[b].insert(x);
            }
            v[a].clear();
        }else{
            let temp = v[b].clone();
            for x in temp {
                v[a].insert(x);
            }
            v[b].clear();
            v.swap(a,b);
        }
        println!("{}",v[b].len());
    }
}
