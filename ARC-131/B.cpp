#include <iostream>
using namespace std;

// 隣接するマスの情報
int dx[4] = { 1, 0, -1, 0 };
int dy[4] = { 0, 1, 0, -1 };

// 入出力、マス目の情報
int H, W;
int d[709][709];

int main() {
	// Step #1. 入力
	cin >> H >> W;
	for (int i = 1; i <= H; i++) {
		for (int j = 1; j <= W; j++) {
			char c; cin >> c;
			if (c == '.') { d[i][j] = 0; } // 塗られていない場合
			if (c == '1') { d[i][j] = 1; } // 色 1 の場合
			if (c == '2') { d[i][j] = 2; } // 色 2 の場合
			if (c == '3') { d[i][j] = 3; } // 色 3 の場合
			if (c == '4') { d[i][j] = 4; } // 色 4 の場合
			if (c == '5') { d[i][j] = 5; } // 色 5 の場合
		}
	}

	// Step #2. シミュレーション
	for (int i = 1; i <= H; i++) {
		for (int j = 1; j <= W; j++) {
			if (d[i][j] != 0) {
				// すでに塗られている場合、新たに塗る必要はない
				continue;
			}

			// 変数 used[k] は色 k が隣接マスに存在するかを表す
			bool used[6] = { false, false, false, false, false, false };
			for (int k = 0; k < 4; k++) {
				int sx = i + dx[k];
				int sy = j + dy[k];
				used[d[sx][sy]] = true;
			}

			// どの色で塗れるかを探す
			// このプログラムは、どの隣接するマスとも異なる色のうち番号が最小の色で塗っている
			for (int k = 1; k <= 5; k++) {
				if (used[k] == true) continue;
				d[i][j] = k;
				break;
			}
		}
	}

	// Step #3. 出力
	for (int i = 1; i <= H; i++) {
		for (int j = 1; j <= W; j++) {
			cout << d[i][j];
		}
		cout << endl;
	}
	return 0;
}
