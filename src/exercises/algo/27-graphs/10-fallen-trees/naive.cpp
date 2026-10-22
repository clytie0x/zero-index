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
    vector<vector<int>> cuts(rows, vector<int>(cols, -1));
    int goal_r = 0, goal_c = 0;
    for (int r = 0; r < rows; r++) {
        for (int c = 0; c < cols; c++) {
            if (grid[r][c] == 'S') {
                cuts[r][c] = 0;
            } else if (grid[r][c] == 'E') {
                goal_r = r;
                goal_c = c;
            }
        }
    }
    for (int k = 0; cuts[goal_r][goal_c] == -1; k++) {
        queue<pair<int, int>> waiting;
        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                if (cuts[r][c] == k) {
                    waiting.push({r, c});
                }
            }
        }
        if (waiting.empty()) {
            break;
        }
        vector<pair<int, int>> level;
        while (!waiting.empty()) {
            auto [r, c] = waiting.front();
            waiting.pop();
            level.push_back({r, c});
            for (int d = 0; d < 4; d++) {
                int nr = r + dr[d];
                int nc = c + dc[d];
                if (nr >= 0 && nr < rows && nc >= 0 && nc < cols && grid[nr][nc] != '#' && grid[nr][nc] != 'T' && cuts[nr][nc] == -1) {
                    cuts[nr][nc] = k;
                    waiting.push({nr, nc});
                }
            }
        }
        for (auto [r, c] : level) {
            for (int d = 0; d < 4; d++) {
                int nr = r + dr[d];
                int nc = c + dc[d];
                if (nr >= 0 && nr < rows && nc >= 0 && nc < cols && grid[nr][nc] == 'T' && cuts[nr][nc] == -1) {
                    cuts[nr][nc] = k + 1;
                }
            }
        }
    }
    cout << cuts[goal_r][goal_c] << '\n';
    return 0;
}
