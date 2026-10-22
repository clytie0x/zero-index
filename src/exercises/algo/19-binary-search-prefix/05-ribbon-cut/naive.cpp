#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    long long k;
    cin >> n >> k;
    vector<int> lengths(n);
    int longest = 0;
    for (int i = 0; i < n; i++) {
        cin >> lengths[i];
        longest = max(longest, lengths[i]);
    }
    int answer = 0;
    for (int cut = longest; cut >= 1; cut--) {
        long long total = 0;
        for (int i = 0; i < n; i++) {
            total += lengths[i] / cut;
        }
        if (total >= k) {
            answer = cut;
            break;
        }
    }
    cout << answer << '\n';
    return 0;
}
