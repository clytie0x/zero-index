#include <bits/stdc++.h>
using namespace std;

long long a, m;

pair<long long, long long> jar(long long n)
{
    if (n == 0) {
        return make_pair(0, 1 % m);
    }
    if (n % 2 == 1) {
        pair<long long, long long> before = jar(n - 1);
        long long total = (before.first + before.second) % m;
        long long power = before.second * a % m;
        return make_pair(total, power);
    }
    pair<long long, long long> half = jar(n / 2);
    long long total = half.first * ((1 + half.second) % m) % m;
    long long power = half.second * half.second % m;
    return make_pair(total, power);
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int t;
    cin >> t;
    for (int c = 0; c < t; c++) {
        long long n;
        cin >> a >> n >> m;
        a %= m;
        cout << jar(n).first << '\n';
    }
    return 0;
}
