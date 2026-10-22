#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, k;
    cin >> n >> k;
    vector<int> score(n);
    for (int i = 0; i < n; i++) {
        cin >> score[i];
    }
    long long pairs = 0;
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            if (score[i] + score[j] == k) {
                pairs++;
            }
        }
    }
    cout << pairs << '\n';
    return 0;
}
