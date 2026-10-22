#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    long long space;
    cin >> n >> space;
    vector<int> size(n);
    for (int &s : size) {
        cin >> s;
    }
    sort(size.begin(), size.end());
    long long ways = 0;
    for (int i = 0; i < n; i++) {
        long long left = space - size[i];
        auto start = size.begin() + i + 1;
        ways += upper_bound(start, size.end(), left) - start;
    }
    cout << ways << '\n';
    return 0;
}
