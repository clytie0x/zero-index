#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    long long gap;
    cin >> n >> gap;
    vector<pair<long long, long long>> films(n);
    for (int i = 0; i < n; i++) {
        long long start, finish;
        cin >> start >> finish;
        films[i] = {finish, start};
    }
    sort(films.begin(), films.end());
    int count = 0;
    long long ready = 0;
    for (int i = 0; i < n; i++) {
        long long finish = films[i].first;
        long long start = films[i].second;
        if (start >= ready) {
            count++;
            ready = finish + gap;
        }
    }
    cout << count << '\n';
    return 0;
}
