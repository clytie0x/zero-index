#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    cin >> n;
    vector<int> height(n);
    for (int i = 0; i < n; i++) {
        cin >> height[i];
    }
    vector<int> left_lower(n), right_lower(n);
    stack<int> boards;
    for (int i = 0; i < n; i++) {
        while (!boards.empty() && height[boards.top()] >= height[i]) {
            boards.pop();
        }
        if (boards.empty()) {
            left_lower[i] = -1;
        } else {
            left_lower[i] = boards.top();
        }
        boards.push(i);
    }
    while (!boards.empty()) {
        boards.pop();
    }
    for (int i = n - 1; i >= 0; i--) {
        while (!boards.empty() && height[boards.top()] >= height[i]) {
            boards.pop();
        }
        if (boards.empty()) {
            right_lower[i] = n;
        } else {
            right_lower[i] = boards.top();
        }
        boards.push(i);
    }
    long long best = 0;
    for (int i = 0; i < n; i++) {
        long long width = right_lower[i] - left_lower[i] - 1;
        best = max(best, width * height[i]);
    }
    cout << best << '\n';
    return 0;
}
