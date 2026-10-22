#include <bits/stdc++.h>
using namespace std;

const int MAX_SCORE = 1000000;
int seen[MAX_SCORE + 1];

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, k;
    cin >> n >> k;
    long long pairs = 0;
    for (int i = 0; i < n; i++) {
        int x;
        cin >> x;
        int need = k - x;
        if (need >= 1 && need <= MAX_SCORE) {
            pairs += seen[need];
        }
        seen[x]++;
    }
    cout << pairs << '\n';
    return 0;
}
