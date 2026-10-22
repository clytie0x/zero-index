#include <bits/stdc++.h>
using namespace std;

int grid[6][6];

bool can_put(int r, int c, int d)
{
    for (int k = 0; k < 6; k++) {
        if ((k != c && grid[r][k] == d) || (k != r && grid[k][c] == d)) {
            return false;
        }
    }
    int top = r / 2 * 2, left = c / 3 * 3;
    for (int i = top; i < top + 2; i++) {
        for (int j = left; j < left + 3; j++) {
            if ((i != r || j != c) && grid[i][j] == d) {
                return false;
            }
        }
    }
    return true;
}

bool solve(int pos)
{
    if (pos == 36) {
        return true;
    }
    int r = pos / 6, c = pos % 6;
    if (grid[r][c] != 0) {
        return solve(pos + 1);
    }
    for (int d = 1; d <= 6; d++) {
        if (can_put(r, c, d)) {
            grid[r][c] = d;
            if (solve(pos + 1)) {
                return true;
            }
            grid[r][c] = 0;
        }
    }
    return false;
}

int main()
{
    for (int r = 0; r < 6; r++) {
        for (int c = 0; c < 6; c++) {
            cin >> grid[r][c];
        }
    }
    bool ok = true;
    for (int r = 0; r < 6; r++) {
        for (int c = 0; c < 6; c++) {
            if (grid[r][c] != 0 && !can_put(r, c, grid[r][c])) {
                ok = false;
            }
        }
    }
    if (!ok || !solve(0)) {
        cout << "NO\n";
        return 0;
    }
    for (int r = 0; r < 6; r++) {
        for (int c = 0; c < 6; c++) {
            cout << grid[r][c] << (c < 5 ? ' ' : '\n');
        }
    }
    return 0;
}
