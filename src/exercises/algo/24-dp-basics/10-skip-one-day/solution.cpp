#include <bits/stdc++.h>
using namespace std;

const long long NEG_INF = LLONG_MIN / 2;

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
    vector<long long> keep(n + 1), cut(n + 1);
    keep[1] = score[1];
    cut[1] = NEG_INF;
    long long answer = keep[1];
    for (int i = 2; i <= n; i++) {
        keep[i] = max(score[i], keep[i - 1] + score[i]);
        cut[i] = max(keep[i - 1], cut[i - 1] + score[i]);
        answer = max(answer, max(keep[i], cut[i]));
    }
    cout << answer << '\n';
    return 0;
}
