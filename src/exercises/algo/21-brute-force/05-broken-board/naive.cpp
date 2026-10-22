#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n;
    cin >> n;
    vector<string> board(n);
    for (int i = 0; i < n; i++) {
        cin >> board[i];
    }
    vector<int> col(n);
    for (int i = 0; i < n; i++) {
        col[i] = i;
    }
    int ways = 0;
    do {
        bool ok = true;
        for (int i = 0; i < n && ok; i++) {
            if (board[i][col[i]] == '#') {
                ok = false;
            }
            for (int j = i + 1; j < n && ok; j++) {
                if (abs(col[i] - col[j]) == j - i) {
                    ok = false;
                }
            }
        }
        if (ok) {
            ways++;
        }
    } while (next_permutation(col.begin(), col.end()));
    cout << ways << '\n';
    return 0;
}
