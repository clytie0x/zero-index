#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    long long target;
    cin >> n >> target;
    map<long long, int> seen;
    seen[0] = 1;
    long long prefix = 0;
    long long answer = 0;
    for (int i = 0; i < n; i++) {
        long long profit;
        cin >> profit;
        prefix += profit;
        auto it = seen.find(prefix - target);
        if (it != seen.end()) {
            answer += it->second;
        }
        seen[prefix]++;
    }
    cout << answer << '\n';
    return 0;
}
