#include <bits/stdc++.h>
using namespace std;

long long count_swaps(vector<int> &height, vector<int> &temp, int lo, int hi)
{
    if (hi - lo <= 1) {
        return 0;
    }
    int mid = (lo + hi) / 2;
    long long swaps = count_swaps(height, temp, lo, mid) + count_swaps(height, temp, mid, hi);
    int i = lo, j = mid, k = lo;
    while (i < mid && j < hi) {
        if (height[i] <= height[j]) {
            temp[k] = height[i];
            i++;
        } else {
            temp[k] = height[j];
            j++;
            swaps += mid - i;
        }
        k++;
    }
    while (i < mid) {
        temp[k] = height[i];
        i++;
        k++;
    }
    while (j < hi) {
        temp[k] = height[j];
        j++;
        k++;
    }
    for (int t = lo; t < hi; t++) {
        height[t] = temp[t];
    }
    return swaps;
}

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
    vector<int> temp(n);
    cout << count_swaps(height, temp, 0, n) << '\n';
    return 0;
}
