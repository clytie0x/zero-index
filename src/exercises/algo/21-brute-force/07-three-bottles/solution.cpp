#include <bits/stdc++.h>
using namespace std;

int cap[3];
int total;
bool visited[101][101];
bool a_possible[101];
int states = 0;

void dfs(int a, int b)
{
    visited[a][b] = true;
    states++;
    a_possible[a] = true;
    int water[3] = {a, b, total - a - b};
    for (int from = 0; from < 3; from++) {
        for (int to = 0; to < 3; to++) {
            if (from == to) {
                continue;
            }
            int amount = min(water[from], cap[to] - water[to]);
            int next[3] = {water[0], water[1], water[2]};
            next[from] -= amount;
            next[to] += amount;
            if (!visited[next[0]][next[1]]) {
                dfs(next[0], next[1]);
            }
        }
    }
}

int main()
{
    int a, b, c;
    cin >> cap[0] >> cap[1] >> cap[2];
    cin >> a >> b >> c;
    total = a + b + c;
    dfs(a, b);
    cout << states << '\n';
    bool first = true;
    for (int x = 0; x <= cap[0]; x++) {
        if (a_possible[x]) {
            cout << (first ? "" : " ") << x;
            first = false;
        }
    }
    cout << '\n';
    return 0;
}
