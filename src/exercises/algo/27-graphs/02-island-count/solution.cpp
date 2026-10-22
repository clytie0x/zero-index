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
    vector<vector<bool>> seen(rows, vector<bool>(cols, false));
    int islands = 0, largest = 0;
    for (int r = 0; r < rows; r++) {
        for (int c = 0; c < cols; c++) {
            if (grid[r][c] != '#' || seen[r][c]) {
                continue;
            }
            islands++;
            int cells = 0;
            queue<pair<int, int>> waiting;
            seen[r][c] = true;
            waiting.push({r, c});
            while (!waiting.empty()) {
                auto [cr, cc] = waiting.front();
                waiting.pop();
                cells++;
                for (int d = 0; d < 4; d++) {
                    int nr = cr + dr[d];
                    int nc = cc + dc[d];
                    if (nr >= 0 && nr < rows && nc >= 0 && nc < cols && grid[nr][nc] == '#' && !seen[nr][nc]) {
                        seen[nr][nc] = true;
                        waiting.push({nr, nc});
                    }
                }
            }
            largest = max(largest, cells);
        }
    }
    cout << islands << ' ' << largest << '\n';
    return 0;
}
