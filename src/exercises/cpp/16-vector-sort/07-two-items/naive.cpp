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
    long long ways = 0;
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            if ((long long)size[i] + size[j] <= space) {
                ways++;
            }
        }
    }
    cout << ways << '\n';
    return 0;
}
