#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    string cloth;
    cin >> cloth;
    int n = cloth.size();
    vector<int> border(n, 0);
    for (int i = 1; i < n; i++) {
        int j = border[i - 1];
        while (j > 0 && cloth[i] != cloth[j]) {
            j = border[j - 1];
        }
        if (cloth[i] == cloth[j]) {
            j++;
        }
        border[i] = j;
    }
    cout << n - border[n - 1] << '\n';
    return 0;
}
