#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    long long capacity;
    cin >> n >> capacity;
    vector<pair<long long, long long>> fruit(n);
    for (int i = 0; i < n; i++) {
        cin >> fruit[i].first >> fruit[i].second;
    }
    sort(fruit.begin(), fruit.end(), [](const pair<long long, long long> &a, const pair<long long, long long> &b) {
        return a.second * b.first > b.second * a.first;
    });
    long long room = capacity, whole = 0;
    double part = 0;
    for (int i = 0; i < n && room > 0; i++) {
        long long grams = fruit[i].first, price = fruit[i].second;
        if (grams <= room) {
            whole += price;
            room -= grams;
        } else {
            part = (double)price * room / grams;
            room = 0;
        }
    }
    cout << fixed << setprecision(2) << whole + part << '\n';
    return 0;
}
