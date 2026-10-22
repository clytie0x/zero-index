#include <bits/stdc++.h>
using namespace std;

long long drop;

long long count_drops(vector<long long> &price, vector<long long> &temp, int lo, int hi)
{
    if (hi - lo <= 1) {
        return 0;
    }
    int mid = (lo + hi) / 2;
    long long count = count_drops(price, temp, lo, mid) + count_drops(price, temp, mid, hi);
    int i = lo;
    for (int j = mid; j < hi; j++) {
        while (i < mid && price[i] <= price[j] + drop) {
            i++;
        }
        count += mid - i;
    }
    i = lo;
    int j = mid, k = lo;
    while (i < mid && j < hi) {
        if (price[i] <= price[j]) {
            temp[k] = price[i];
            i++;
        } else {
            temp[k] = price[j];
            j++;
        }
        k++;
    }
    while (i < mid) {
        temp[k] = price[i];
        i++;
        k++;
    }
    while (j < hi) {
        temp[k] = price[j];
        j++;
        k++;
    }
    for (int t = lo; t < hi; t++) {
        price[t] = temp[t];
    }
    return count;
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    cin >> n >> drop;
    vector<long long> price(n);
    for (int i = 0; i < n; i++) {
        cin >> price[i];
    }
    vector<long long> temp(n);
    cout << count_drops(price, temp, 0, n) << '\n';
    return 0;
}
