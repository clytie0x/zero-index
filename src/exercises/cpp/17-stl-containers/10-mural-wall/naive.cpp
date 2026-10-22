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
    long long best = 0;
    for (int i = 0; i < n; i++) {
        int left = i;
        while (left > 0 && height[left - 1] >= height[i]) {
            left--;
        }
        int right = i;
        while (right < n - 1 && height[right + 1] >= height[i]) {
            right++;
        }
        long long width = right - left + 1;
        best = max(best, width * height[i]);
    }
    cout << best << '\n';
    return 0;
}
