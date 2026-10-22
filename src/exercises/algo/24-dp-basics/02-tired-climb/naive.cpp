#include <bits/stdc++.h>
using namespace std;

vector<long long> cost;

long long least(int step)
{
    if (step == 0) {
        return 0;
    }
    if (step == 1) {
        return cost[1];
    }
    return cost[step] + min(least(step - 1), least(step - 2));
}

int main()
{
    int n;
    cin >> n;
    cost = vector<long long>(n + 1);
    for (int i = 1; i <= n; i++) {
        cin >> cost[i];
    }
    cout << least(n) << '\n';
    return 0;
}
