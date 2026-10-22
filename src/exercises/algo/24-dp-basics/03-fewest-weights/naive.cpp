#include <bits/stdc++.h>
using namespace std;

const int INF = 1000000000;

vector<int> weights;

int fewest(int x)
{
    if (x == 0) {
        return 0;
    }
    int best = INF;
    for (int w : weights) {
        if (w <= x) {
            best = min(best, fewest(x - w) + 1);
        }
    }
    return best;
}

int main()
{
    int n, target;
    cin >> n >> target;
    weights = vector<int>(n);
    for (int i = 0; i < n; i++) {
        cin >> weights[i];
    }
    int answer = fewest(target);
    if (answer >= INF) {
        cout << -1 << '\n';
    } else {
        cout << answer << '\n';
    }
    return 0;
}
