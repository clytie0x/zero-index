#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, q;
    cin >> n >> q;
    vector<int> pages(n + 1);
    for (int day = 1; day <= n; day++) {
        cin >> pages[day];
    }
    for (int k = 0; k < q; k++) {
        int start;
        long long target;
        cin >> start >> target;
        long long total = 0;
        int answer = -1;
        for (int day = start; day <= n; day++) {
            total += pages[day];
            if (total >= target) {
                answer = day;
                break;
            }
        }
        cout << answer << '\n';
    }
    return 0;
}
