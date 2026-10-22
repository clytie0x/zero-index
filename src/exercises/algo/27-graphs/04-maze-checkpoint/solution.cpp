#include <bits/stdc++.h>
using namespace std;

int dr[4] = {-1, 1, 0, 0};
int dc[4] = {0, 0, -1, 1};
int rows, cols;
vector<string> grid;

int steps_between(char from, char to)
{
    vector<vector<int>> dist(rows, vector<int>(cols, -1));
    queue<pair<int, int>> waiting;
    for (int r = 0; r < rows; r++) {
        for (int c = 0; c < cols; c++) {
            if (grid[r][c] == from) {
                dist[r][c] = 0;
                waiting.push({r, c});
            }
        }
    }
    while (!waiting.empty()) {
        auto [r, c] = waiting.front();
        waiting.pop();
        if (grid[r][c] == to) {
            return dist[r][c];
        }
        for (int d = 0; d < 4; d++) {
            int nr = r + dr[d];
            int nc = c + dc[d];
            if (nr >= 0 && nr < rows && nc >= 0 && nc < cols && grid[nr][nc] != '#' && dist[nr][nc] == -1) {
                dist[nr][nc] = dist[r][c] + 1;
                waiting.push({nr, nc});
            }
        }
    }
    return -1;
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
    int first = steps_between('S', 'P');
    int second = steps_between('P', 'E');
    if (first == -1 || second == -1) {
        cout << -1 << '\n';
    } else {
        cout << first + second << '\n';
    }
    return 0;
}
