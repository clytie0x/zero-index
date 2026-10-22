#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int rows, cols;
    cin >> rows >> cols;
    vector<vector<int>> photo(rows, vector<int>(cols));
    for (int r = 0; r < rows; r++) {
        for (int c = 0; c < cols; c++) {
            cin >> photo[r][c];
        }
    }
    for (int c = 0; c < cols; c++) {
        for (int r = rows - 1; r >= 0; r--) {
            cout << photo[r][c];
            if (r > 0) {
                cout << ' ';
            }
        }
        cout << '\n';
    }
    return 0;
}
