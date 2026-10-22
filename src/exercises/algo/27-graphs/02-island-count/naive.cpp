#include <bits/stdc++.h>
using namespace std;

int dr[4] = {-1, 1, 0, 0};
int dc[4] = {0, 0, -1, 1};

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int rows, cols;
    cin >> rows >> cols;
    vector<string> grid(rows);
    for (int r = 0; r < rows; r++) {
        cin >> grid[r];
    }
    vector<vector<int>> label(rows, vector<int>(cols, -1));
    for (int r = 0; r < rows; r++) {
        for (int c = 0; c < cols; c++) {
            if (grid[r][c] == '#') {
                label[r][c] = r * cols + c;
            }
        }
    }
    bool changed = true;
    while (changed) {
        changed = false;
        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                if (label[r][c] == -1) {
                    continue;
                }
                for (int d = 0; d < 4; d++) {
                    int nr = r + dr[d];
                    int nc = c + dc[d];
                    if (nr >= 0 && nr < rows && nc >= 0 && nc < cols && label[nr][nc] != -1 && label[nr][nc] < label[r][c]) {
                        label[r][c] = label[nr][nc];
                        changed = true;
                    }
                }
            }
        }
    }
    vector<int> cells(rows * cols, 0);
    vector<bool> on_edge(rows * cols, false);
    for (int r = 0; r < rows; r++) {
        for (int c = 0; c < cols; c++) {
            if (label[r][c] != -1) {
                cells[label[r][c]]++;
                if (r == 0 || r == rows - 1 || c == 0 || c == cols - 1) {
                    on_edge[label[r][c]] = true;
                }
            }
        }
    }
    int islands = 0, largest = 0;
    for (int i = 0; i < rows * cols; i++) {
        if (cells[i] > 0 && !on_edge[i]) {
            islands++;
            largest = max(largest, cells[i]);
        }
    }
    cout << islands << ' ' << largest << '\n';
    return 0;
}
