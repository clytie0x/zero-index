#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    cin >> n;
    vector<int> volume(n);
    for (int i = 0; i < n; i++) {
        cin >> volume[i];
    }
    long long ways = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (i != j && volume[j] % volume[i] == 0) {
                ways++;
            }
        }
    }
    cout << ways << '\n';
    return 0;
}
