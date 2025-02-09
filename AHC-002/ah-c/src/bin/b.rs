use proconio::input;
use rand::rngs::StdRng;
use rand::{Rng, SeedableRng};
use std::time::Instant;

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

struct HillClimbingSolver {
    now_path: Vec<usize>,
}

impl HillClimbingSolver {
    fn new() -> Self {
        Self {
            now_path: Vec::new(),
        }
    }

    fn hill_climb(
        &mut self,
        first_coord: usize,
        points: &[i32],
        tiles: &[usize],
        next_coords: &[Vec<usize>],
        time_threshold: u128,
    ) {
        let start_time = Instant::now();
        self.solve_first(first_coord, points, tiles, next_coords);

        let mut rng = Random::new(0);
        let mut now_visiteds = vec![false; TILE_N];
        for &coord in &self.now_path {
            now_visiteds[tiles[coord]] = true;
        }

        while start_time.elapsed().as_millis() < time_threshold {
            let delete_path_length = rng.next_int(1 + self.now_path.len() / 20);
            let start_path_id = rng.next_int(self.now_path.len() - delete_path_length);
            let end_path_id = start_path_id + delete_path_length;

            let mut next_visiteds = now_visiteds.clone();
            let mut now_score = 0;
            for i in start_path_id + 1..end_path_id {
                now_score += points[self.now_path[i]];
                next_visiteds[tiles[self.now_path[i]]] = false;
            }

            let next_path = self.partial_dfs(
                self.now_path[start_path_id],
                self.now_path[end_path_id],
                &next_visiteds,
                4 * delete_path_length,
                points,
                tiles,
                next_coords,
            );

            if !next_path.is_empty() {
                self.now_path.splice(start_path_id..end_path_id, next_path);
            }
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

    fn partial_dfs(
        &self,
        start: usize,
        goal: usize,
        visiteds: &[bool],
        search_limit: usize,
        points: &[i32],
        tiles: &[usize],
        next_coords: &[Vec<usize>],
    ) -> Vec<usize> {
        let mut best_path = Vec::new();
        let mut best_score = 0;
        let mut stack = vec![(start, vec![start], 0, visiteds.to_vec())];

        while let Some((coord, path, score, mut visited)) = stack.pop() {
            if coord == goal {
                if score > best_score {
                    best_score = score;
                    best_path = path.clone();
                }
                continue;
            }
            if path.len() >= search_limit {
                continue;
            }
            visited[tiles[coord]] = true;
            for &next_coord in &next_coords[coord] {
                if !visited[tiles[next_coord]] {
                    let mut new_path = path.clone();
                    new_path.push(next_coord);
                    stack.push((
                        next_coord,
                        new_path,
                        score + points[next_coord],
                        visited.clone(),
                    ));
                }
            }
        }
        best_path
    }
}

fn main() {
    let (first_coord, tiles, points) = State::input();
    let next_coords = initialize_global_info(&tiles);
    let mut solver = HillClimbingSolver::new();
    solver.hill_climb(first_coord, &points, &tiles, &next_coords, 1950);
    solver.output();
}

