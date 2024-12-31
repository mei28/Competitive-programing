use proconio::input;

fn main() {
    input! {mut s:String}
    // replace s from "00" into "0"
    s = s.replace("00", "0");
    println!("{}", s.len());
}
