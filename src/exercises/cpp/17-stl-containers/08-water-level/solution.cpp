#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    cin >> n;
    vector<int> level(n);
    for (int i = 0; i < n; i++) {
        cin >> level[i];
    }
    stack<int> higher;
    for (int i = 0; i < n; i++) {
        while (!higher.empty() && level[higher.top()] <= level[i]) {
            higher.pop();
        }
        int days;
        if (higher.empty()) {
            days = i + 1;
        } else {
            days = i - higher.top();
        }
        cout << days << (i + 1 < n ? ' ' : '\n');
        higher.push(i);
    }
    return 0;
}
