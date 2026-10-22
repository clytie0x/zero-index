#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    cin >> n;
    priority_queue<long long, vector<long long>, greater<long long>> piles;
    for (int i = 0; i < n; i++) {
        long long weight;
        cin >> weight;
        piles.push(weight);
    }
    long long cost = 0;
    while (piles.size() > 1) {
        long long a = piles.top();
        piles.pop();
        long long b = piles.top();
        piles.pop();
        cost += a + b;
        piles.push(a + b);
    }
    cout << cost << '\n';
    return 0;
}
