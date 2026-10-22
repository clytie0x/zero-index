#include <bits/stdc++.h>
using namespace std;

int rows, cols;
vector<vector<long long>> score;
long long best_total;
string best_path, path;
bool found = false;

void walk(int r, int c, long long total)
{
    total += score[r][c];
    if (r == rows - 1 && c == cols - 1) {
        if (!found || total > best_total) {
            found = true;
            best_total = total;
            best_path = path;
        }
        return;
    }
    if (r + 1 < rows) {
        path += 'D';
        walk(r + 1, c, total);
        path.pop_back();
    }
    if (c + 1 < cols) {
        path += 'R';
        walk(r, c + 1, total);
        path.pop_back();
    }
}

int main()
{
    cin >> rows >> cols;
    score.assign(rows, vector<long long>(cols));
    for (int r = 0; r < rows; r++) {
        for (int c = 0; c < cols; c++) {
            cin >> score[r][c];
        }
    }
    walk(0, 0, 0);
    cout << best_total << '\n' << best_path << '\n';
    return 0;
}
