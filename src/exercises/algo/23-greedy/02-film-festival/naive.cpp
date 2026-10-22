#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    long long gap;
    cin >> n >> gap;
    vector<long long> start(n), finish(n);
    for (int i = 0; i < n; i++) {
        cin >> start[i] >> finish[i];
    }
    vector<bool> seen(n, false);
    int count = 0;
    long long ready = 0;
    while (true) {
        int pick = -1;
        for (int i = 0; i < n; i++) {
            if (!seen[i] && start[i] >= ready && (pick == -1 || finish[i] < finish[pick])) {
                pick = i;
            }
        }
        if (pick == -1) {
            break;
        }
        seen[pick] = true;
        count++;
        ready = finish[pick] + gap;
    }
    cout << count << '\n';
    return 0;
}
