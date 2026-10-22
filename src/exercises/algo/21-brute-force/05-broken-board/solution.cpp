#include <bits/stdc++.h>
using namespace std;

int n;
vector<string> board;
bool col_used[12], diag1_used[23], diag2_used[23];
int ways = 0;

void place(int row)
{
    if (row == n) {
        ways++;
        return;
    }
    for (int c = 0; c < n; c++) {
        int d1 = row + c, d2 = row - c + n - 1;
        if (board[row][c] == '#' || col_used[c] || diag1_used[d1] || diag2_used[d2]) {
            continue;
        }
        col_used[c] = diag1_used[d1] = diag2_used[d2] = true;
        place(row + 1);
        col_used[c] = diag1_used[d1] = diag2_used[d2] = false;
    }
}

int main()
{
    cin >> n;
    board.resize(n);
    for (int i = 0; i < n; i++) {
        cin >> board[i];
    }
    place(0);
    cout << ways << '\n';
    return 0;
}
