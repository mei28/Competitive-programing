use proconio::{input, marker::Chars};

fn check_board(field: &Vec<Vec<char>>) -> &str {
    let lines = vec![
        field[0].clone(),
        field[1].clone(),
        field[2].clone(),
        vec![field[0][0], field[1][0], field[2][0]],
        vec![field[0][1], field[1][1], field[2][1]],
        vec![field[0][2], field[1][2], field[2][2]],
        vec![field[0][0], field[1][1], field[2][2]],
        vec![field[0][2], field[1][1], field[2][0]],
    ];

    for line in lines {
        if line.iter().all(|&x| x == 'T') {
            return "Takahashi";
        }
        if line.iter().all(|&x| x == 'A') {
            return "Aoki";
        }
    }

    return "";
}

fn minimax(
    field: &Vec<Vec<char>>,
    depth: usize,
    is_maximizing: bool,
    scores: usize,
    takahashi_score: usize,
    aoki_score: usize,
) -> String {
    match check_board(field) {
        "Takahashi" => return "Takahashi".to_string(),
        "Aoki" => return "Aoki".to_string(),
        _ => (),
    }

    if depth == 0 || field.iter().all(|row| row.iter().all(|&x| x != ' ')) {
        if takahashi_score > aoki_score {
            return "Takahashi".to_string();
        } else if aoki_score > takahashi_score {
            return "Aoki".to_string();
        } else {
            return "Draw".to_string();
        }
    }

    if is_maximizing {
        let mut best_score = std::usize::MIN;
        for i in 0..3{
            for j in 0..3{
                if field[i][j] == ' '{
                    field[i][j] = 'A';
                    let result = minimax(
                        field,
                        depth - 1,
                        true,
                        scores + 1,
                        takahashi_score,
                        aoki_score,
                    );
                    field[i][j] = ' ';

                    if result == "Aoki".to_string() {
                        return result;
                    }
                }

            }
        }
        

    return "".to_string();
}

fn main() {
    input! {
        field: [Chars; 3]
    }
}
