#include <bits/stdc++.h>
using namespace std;

int dr[4] = {-1, 1, 0, 0};
int dc[4] = {0, 0, -1, 1};
int rows, cols;
vector<string> grid;

int minutes_between(char from, char to)
{
    vector<vector<bool>> reached(rows, vector<bool>(cols, false));
    for (int r = 0; r < rows; r++) {
        for (int c = 0; c < cols; c++) {
            if (grid[r][c] == from) {
                reached[r][c] = true;
            }
        }
    }
    for (int minute = 0; ; minute++) {
        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                if (grid[r][c] == to && reached[r][c]) {
                    return minute;
                }
            }
        }
        vector<vector<bool>> next_minute = reached;
        bool changed = false;
        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                if (grid[r][c] == '#' || reached[r][c]) {
                    continue;
                }
                for (int d = 0; d < 4; d++) {
                    int nr = r + dr[d];
                    int nc = c + dc[d];
                    if (nr >= 0 && nr < rows && nc >= 0 && nc < cols && reached[nr][nc]) {
                        next_minute[r][c] = true;
                        changed = true;
                        break;
                    }
                }
            }
        }
        if (!changed) {
            return -1;
        }
        reached = next_minute;
    }
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cin >> rows >> cols;
    grid.resize(rows);
    for (int r = 0; r < rows; r++) {
        cin >> grid[r];
    }
    int first = minutes_between('S', 'P');
    int second = minutes_between('P', 'E');
    if (first == -1 || second == -1) {
        cout << -1 << '\n';
    } else {
        cout << first + second << '\n';
    }
    return 0;
}
