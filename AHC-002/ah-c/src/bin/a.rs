use proconio::input;
use rand::rngs::StdRng;
use rand::{Rng, SeedableRng};

const H: usize = 50;
const W: usize = 50;
const TILE_N: usize = 2500;

struct Random {
    rng: StdRng,
}

impl Random {
    fn new(seed: u64) -> Self {
        Self {
            rng: StdRng::seed_from_u64(seed),
        }
    }

    fn next_int(&mut self, m: usize) -> usize {
        self.rng.gen_range(0..m)
    }
}

struct DfsSolver {
    visiteds: Vec<bool>,
    path: Vec<usize>,
    best_path: Vec<usize>,
    best_score: i32,
    score: i32,
    remining_search_cnt: usize,
}

impl DfsSolver {
    fn new() -> Self {
        Self {
            visiteds: vec![false; TILE_N],
            path: Vec::new(),
            best_path: Vec::new(),
            best_score: 0,
            score: 0,
            remaining_search_cnt: 4000,
        }
    }

    fn start(
        &mut self,
        first_coord: usize,
        points: &[i32],
        tiles: &[usize],
        next_coords: &[Vec<usize>],
    ) {
        self.dfs(first_coord, points, tiles, next_coords);
    }

    fn dfs(&mut self, coord: usize, points: &[i32], tiles: &[usize], next_coords: &[Vec<usize>]) {
        self.path.push(coord);
        self.score += points[coord];
        self.visiteds[tiles[coord]] = true;

        if self.best_score < self.score {
            self.best_score = self.score;
            self.best_path = self.path.clone();
        }

        self.remaining_search_cnt -= 1;
        if self.remaining_search_cnt == 0 {
            return;
        }

        let legal_next_coords: Vec<usize> = next_coords[coord]
            .iter()
            .copied()
            .filter(|&next_coord| !self.visiteds[tiles[next_coord]])
            .collect();

        for &next_coord in &legal_next_coords {
            self.dfs(next_coord, points, tiles, next_coords);
            if self.remaining_search_cnt == 0 {
                return;
            }
        }

        self.path.pop();
        self.score -= points[coord];
        self.visiteds[tiles[coord]] = false;
    }
}

struct State {
    now_path: Vec<usize>,
}

impl State {
    fn new() -> Self {
        Self {
            now_path: Vec::new(),
        }
    }

    fn solve_first(
        &mut self,
        first_coord: usize,
        points: &[i32],
        tiles: &[usize],
        next_coords: &[Vec<usize>],
    ) {
        let mut dfs_solver = DfsSolver::new();
        dfs_solver.start(first_coord, points, tiles, next_coords);
        self.now_path = dfs_solver.best_path;
    }

    fn input() -> (usize, Vec<usize>, Vec<i32>) {
        input! {
            sy: usize, sx: usize,
            tiles: [[usize; W]; H],
            points: [[i32; W]; H],
        }

        let first_coord = sy * W + sx;
        let tiles = tiles.into_iter().flatten().collect();
        let points = points.into_iter().flatten().collect();

        (first_coord, tiles, points)
    }

    fn output(&self) {
        let mut res = String::new();
        for i in 0..self.now_path.len() - 1 {
            let diff = self.now_path[i + 1] as isize - self.now_path[i] as isize;
            res.push(match diff {
                1 => 'R',
                -1 => 'L',
                d if d == W as isize => 'D',
                u if u == -(W as isize) => 'U',
                _ => '?',
            });
        }
        println!("{}", res);
    }
}

fn initialize_global_info(tiles: &[usize]) -> Vec<Vec<usize>> {
    let mut next_coords = vec![Vec::new(); H * W];
    let directions: [(isize, isize); 4] = [(1, 0), (0, 1), (-1, 0), (0, -1)];

    for y in 0..H {
        for x in 0..W {
            let coord = y * W + x;
            for &(dy, dx) in &directions {
                let ty = y as isize + dy;
                let tx = x as isize + dx;
                if (0..H as isize).contains(&ty) && (0..W as isize).contains(&tx) {
                    let tcoord = (ty as usize) * W + (tx as usize);
                    if tiles[coord] != tiles[tcoord] {
                        next_coords[coord].push(tcoord);
                    }
                }
            }
        }
    }
    next_coords
}

fn main() {
    let (first_coord, tiles, points) = State::input();
    let next_coords = initialize_global_info(&tiles);
    let mut state = State::new();
    state.solve_first(first_coord, &points, &tiles, &next_coords);
    state.output();
}
