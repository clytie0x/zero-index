#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    vector<int> score;
    int x;
    while (cin >> x && x != -1) {
        score.push_back(x);
    }
    long long total = 0;
    for (int s : score) {
        total += s;
    }
    long long count = score.size();
    vector<int> above;
    for (int s : score) {
        if (s * count > total) {
            above.push_back(s);
        }
    }
    cout << above.size() << '\n';
    if (!above.empty()) {
        for (int i = 0; i < (int)above.size(); i++) {
            if (i > 0) {
                cout << ' ';
            }
            cout << above[i];
        }
        cout << '\n';
    }
    return 0;
}
