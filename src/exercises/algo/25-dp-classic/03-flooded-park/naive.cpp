#include <bits/stdc++.h>
using namespace std;

int rows, cols;
vector<string> grid;

long long count_paths(int r, int c)
{
    if (r >= rows || c >= cols || grid[r][c] == '#') {
        return 0;
    }
    if (r == rows - 1 && c == cols - 1) {
        return 1;
    }
    return count_paths(r + 1, c) + count_paths(r, c + 1);
}

int main()
{
    cin >> rows >> cols;
    grid.resize(rows);
    for (int r = 0; r < rows; r++) {
        cin >> grid[r];
    }
    cout << count_paths(0, 0) % 1000000007 << '\n';
    return 0;
}
