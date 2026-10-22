#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    cin >> n;
    vector<long long> score(n + 1);
    for (int i = 1; i <= n; i++) {
        cin >> score[i];
    }
    long long answer = LLONG_MIN;
    for (int l = 1; l <= n; l++) {
        long long sum = 0;
        long long lowest = LLONG_MAX;
        for (int r = l; r <= n; r++) {
            sum += score[r];
            lowest = min(lowest, score[r]);
            answer = max(answer, sum);
            if (r > l) {
                answer = max(answer, sum - lowest);
            }
        }
    }
    cout << answer << '\n';
    return 0;
}
