#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, k;
    string digits;
    cin >> n >> k >> digits;
    string kept;
    for (char c : digits) {
        while (k > 0 && !kept.empty() && kept.back() > c) {
            kept.pop_back();
            k--;
        }
        kept.push_back(c);
    }
    while (k > 0) {
        kept.pop_back();
        k--;
    }
    int start = 0;
    while (start + 1 < (int)kept.size() && kept[start] == '0') {
        start++;
    }
    cout << kept.substr(start) << '\n';
    return 0;
}
