#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    cin >> n;
    long long total = 0;
    long long lowest = 0;
    for (int i = 0; i < n; i++) {
        int amount;
        cin >> amount;
        total += amount;
        if (i == 0 || total < lowest) {
            lowest = total;
        }
        cout << total << ' ' << lowest << '\n';
    }
    return 0;
}
