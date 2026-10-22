#include <bits/stdc++.h>
using namespace std;

int dr[4] = {-1, 1, 0, 0};
int dc[4] = {0, 0, -1, 1};

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    map<string, int> moves;
    queue<string> waiting;
    moves["123456780"] = 0;
    waiting.push("123456780");
    while (!waiting.empty()) {
        string board = waiting.front();
        waiting.pop();
        size_t blank = board.find('0');
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
    int t;
    cin >> t;
    for (int i = 0; i < t; i++) {
        string board;
        cin >> board;
        auto it = moves.find(board);
        cout << (it == moves.end() ? -1 : it->second) << '\n';
    }
    return 0;
}
