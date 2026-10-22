#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int rows, cols;
    cin >> rows >> cols;
    vector<vector<long long>> to_end(rows, vector<long long>(cols));
    for (int r = 0; r < rows; r++) {
        for (int c = 0; c < cols; c++) {
            cin >> to_end[r][c];
        }
    }
    for (int r = rows - 1; r >= 0; r--) {
        for (int c = cols - 1; c >= 0; c--) {
            if (r == rows - 1 && c == cols - 1) {
                continue;
            }
            if (r == rows - 1) {
                to_end[r][c] += to_end[r][c + 1];
            } else if (c == cols - 1) {
                to_end[r][c] += to_end[r + 1][c];
            } else {
                to_end[r][c] += max(to_end[r + 1][c], to_end[r][c + 1]);
            }
        }
    }
    string path;
    int r = 0, c = 0;
    while (r < rows - 1 || c < cols - 1) {
        if (c == cols - 1 || (r < rows - 1 && to_end[r + 1][c] >= to_end[r][c + 1])) {
            path += 'D';
            r++;
        } else {
            path += 'R';
            c++;
        }
    }
    cout << to_end[0][0] << '\n' << path << '\n';
    return 0;
}
