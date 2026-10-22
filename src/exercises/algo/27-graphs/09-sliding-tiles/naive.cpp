#include <bits/stdc++.h>
using namespace std;

int dr[4] = {-1, 1, 0, 0};
int dc[4] = {0, 0, -1, 1};

int solve(const string &start)
{
    map<string, int> moves;
    queue<string> waiting;
    moves[start] = 0;
    waiting.push(start);
    while (!waiting.empty()) {
        string board = waiting.front();
        waiting.pop();
        if (board == "123456780") {
            return moves[board];
        }
        int blank = board.find('0');
        int r = blank / 3, c = blank % 3;
        for (int d = 0; d < 4; d++) {
            int nr = r + dr[d];
            int nc = c + dc[d];
            if (nr < 0 || nr >= 3 || nc < 0 || nc >= 3) {
                continue;
            }
            string next = board;
            swap(next[blank], next[nr * 3 + nc]);
            if (moves.count(next) == 0) {
                moves[next] = moves[board] + 1;
                waiting.push(next);
            }
        }
    }
    return -1;
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int t;
    cin >> t;
    for (int i = 0; i < t; i++) {
        string board;
        cin >> board;
        cout << solve(board) << '\n';
    }
    return 0;
}
