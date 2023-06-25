#![allow(non_snake_case)]

use bitset_fixed::BitSet;
use proconio::*;
use std::collections::HashSet;

pub struct Input {
    pub gs: Vec<i32>,
}
pub type Output = Vec<((usize, usize), (usize, usize))>;

const N: usize = 30;
const N2: usize = N * (N + 1) / 2;

struct State {
    gs: Vec<i32>,
    id: usize,
    score: (i32, i32),
    used: BitSet,
}

fn id(x: usize, y: usize) -> usize {
    x * (x + 1) / 2 + y
}

struct Trace {
    log: Vec<(((usize, usize), (usize, usize)), usize)>,
}

impl Trace {
    fn new() -> Self {
        Trace { log: vec![] }
    }

    fn add(&mut self, c: ((usize, usize), (usize, usize)), p: usize) -> usize {
        self.log.push((c, p));
        self.log.len() - 1
    }

    fn get(&self, mut i: usize) -> Vec<((usize, usize), (usize, usize))> {
        let mut out = vec![];
        while i != !0 {
            out.push(self.log[i].0);
            i = self.log[i].1;
        }
        out.reverse();
        out
    }
}

fn main() {
    get_time();
    let input = read_input();
    let out = solve(&input);
    write_output(&out);
    eprintln!("Time: {:.3}", get_time());
}

pub fn get_time() -> f64 {
    static mut STIME: f64 = -1.0;
    let t = std::time::SystemTime::now()
        .duration_since(std::time::UNIX_EPOCH)
        .unwrap();
    let ms = t.as_secs() as f64 + t.subsec_nanos() as f64 * 1e-9;
    unsafe {
        if STIME < 0.0 {
            STIME = ms;
        }
        // ローカル環境とジャッジ環境の実行速度差はget_timeで吸収しておくと便利
        #[cfg(feature = "local")]
        {
            (ms - STIME) * 1.3
        }
        #[cfg(not(feature = "local"))]
        {
            ms - STIME
        }
    }
}

pub fn write_output(out: &Output) {
    println!("{}", out.len());
    for &((x1, y1), (x2, y2)) in out {
        println!("{} {} {} {}", x1, y1, x2, y2)
    }
}

pub fn read_input() -> Input {
    input! {
        gs:[i32;N2]
    }
    Input { gs }
}

fn pos(gs: &Vec<i32>, i: i32) -> (usize, usize) {
    for x in 0..N {
        for y in 0..=x {
            if gs[id(x, y)] == i {
                return (x, y);
            }
        }
    }
    panic!();
}

const W: usize = 700;

fn solve(input: &Input) -> Output {
    let mut beam = vec![State {
        gs: input.gs.clone(),
        id: !0,
        score: (0, 0),
        used: BitSet::new(N2),
    }];
    let mut trace = Trace::new();
    for i in 0..N2 as i32 {
        eprintln!("{}: {}", i, beam[0].score.0);
        let mut next_move = vec![];
        let mut dists = vec![];
        for b in 0..beam.len() {
            let gs = &beam[b].gs;
            let (x, y) = pos(&gs, i);
            let mut ok = [true; N2];
            for x in 1..N {
                for y in 0..=x {
                    if y > 0 && (gs[id(x - 1, y - 1)] >= i || !ok[id(x - 1, y - 1)]) {
                        ok[id(x, y)] = false;
                    }
                    if y <= x - 1 && (gs[id(x - 1, y)] >= i || !ok[id(x - 1, y)]) {
                        ok[id(x, y)] = false;
                    }
                }
            }
            let mut dist = [(1000000000, 0, !0); N2];
            dist[id(x, y)] = (0, 0, !0);
            if ok[id(x, y)] {
                dists.push(dist);
                next_move.push((beam[b].score, b, x, y));
                continue;
            }
            for x in (0..x).rev() {
                for y in 0..=x {
                    if gs[id(x, y)] < i {
                        continue;
                    }
                    let d2 = dist[id(x + 1, y)];
                    dist[id(x, y)].setmin((d2.0 + 1, d2.1 - gs[id(x, y)], 0));
                    let d2 = dist[id(x + 1, y + 1)];
                    dist[id(x, y)].setmin((d2.0 + 1, d2.1 - gs[id(x, y)], 1));
                }
            }
            for x in 0..x {
                for y in 0..=x {
                    if ok[id(x, y)] && dist[id(x, y)].0 < 1000000000 {
                        next_move.push((
                            (
                                beam[b].score.0 + dist[id(x, y)].0,
                                beam[b].score.1 + dist[id(x, y)].1,
                            ),
                            b,
                            x,
                            y,
                        ));
                    }
                }
            }
            dists.push(dist);
        }
        next_move.sort_by_key(|a| a.0);
        let mut next = vec![];
        let mut set = HashSet::new();
        for (score, b, mut x, mut y) in next_move {
            let mut used = beam[b].used.clone();
            used.set(id(x, y), true);
            if !set.insert(used.clone()) {
                continue;
            }
            let mut gs = beam[b].gs.clone();
            let mut tmp = vec![];
            loop {
                let dy = dists[b][id(x, y)].2;
                if dy == !0 {
                    break;
                }
                tmp.push(((x, y), (x + 1, y + dy)));
                x += 1;
                y += dy;
            }
            tmp.reverse();
            for &((x1, y1), (x2, y2)) in &tmp {
                gs.swap(id(x1, y1), id(x2, y2));
            }
            let mut id = beam[b].id;
            for &mv in &tmp {
                id = trace.add(mv, id);
            }
            next.push(State {
                score,
                gs,
                id,
                used,
            });
            if next.len() == W {
                break;
            }
        }
        beam = next;
    }
    trace.get(beam[0].id)
}

pub trait SetMinMax {
    fn setmin(&mut self, v: Self) -> bool;
    fn setmax(&mut self, v: Self) -> bool;
}
impl<T> SetMinMax for T
where
    T: PartialOrd,
{
    fn setmin(&mut self, v: T) -> bool {
        *self > v && {
            *self = v;
            true
        }
    }
    fn setmax(&mut self, v: T) -> bool {
        *self < v && {
            *self = v;
            true
        }
    }
}

#[macro_export]
macro_rules! mat {
	($($e:expr),*) => { vec![$($e),*] };
	($($e:expr,)*) => { vec![$($e),*] };
	($e:expr; $d:expr) => { vec![$e; $d] };
	($e:expr; $d:expr $(; $ds:expr)+) => { vec![mat![$e $(; $ds)*]; $d] };
}
