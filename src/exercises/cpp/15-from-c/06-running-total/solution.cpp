#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    cin >> n;
    long long total = 0;
    for (int i = 0; i < n; i++) {
        int amount;
        cin >> amount;
        total += amount;
        cout << total << '\n';
    }
    return 0;
}
