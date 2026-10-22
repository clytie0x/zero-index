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
    vector<vector<int>> cuts(rows, vector<int>(cols, INT_MAX));
    deque<pair<int, int>> waiting;
    int goal_r = 0, goal_c = 0;
    for (int r = 0; r < rows; r++) {
        for (int c = 0; c < cols; c++) {
            if (grid[r][c] == 'S') {
                cuts[r][c] = 0;
                waiting.push_back({r, c});
            } else if (grid[r][c] == 'E') {
                goal_r = r;
                goal_c = c;
            }
        }
    }
    while (!waiting.empty()) {
        auto [r, c] = waiting.front();
        waiting.pop_front();
        for (int d = 0; d < 4; d++) {
            int nr = r + dr[d];
            int nc = c + dc[d];
            if (nr < 0 || nr >= rows || nc < 0 || nc >= cols || grid[nr][nc] == '#') {
                continue;
            }
            int cost = (grid[nr][nc] == 'T' ? 1 : 0);
            if (cuts[r][c] + cost < cuts[nr][nc]) {
                cuts[nr][nc] = cuts[r][c] + cost;
                if (cost == 0) {
                    waiting.push_front({nr, nc});
                } else {
                    waiting.push_back({nr, nc});
                }
            }
        }
    }
    int answer = cuts[goal_r][goal_c];
    cout << (answer == INT_MAX ? -1 : answer) << '\n';
    return 0;
}
