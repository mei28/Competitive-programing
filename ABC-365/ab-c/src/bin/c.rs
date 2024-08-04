use proconio::input;

fn main() {
    input! {n:isize, m:isize, aa:[isize; n]}

    // Initialize binary search bounds
    let mut ok = 0;
    let mut ng = std::isize::MAX;

    // Perform binary search
    while ng - ok > 1 {
        let mid = ok + (ng - ok) / 2;

        // Calculate the total sum with the current mid value as the cap
        let sum: isize = aa.iter().map(|&a| a.min(mid)).sum();

        // Update the search bounds based on the sum
        if sum <= m {
            ok = mid;
        } else {
            ng = mid;
        }
    }

    // Check if the result is effectively infinite
    if ok == std::isize::MAX - 1 {
        println!("infinite");
    } else {
        println!("{}", ok);
    }
}

