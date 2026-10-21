#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    cin >> n;
    int total = 0;
    int best_score = -1;
    string best_name;
    for (int i = 0; i < n; i++) {
        string name;
        int score;
        cin >> name >> score;
        total += score;
        if (score > best_score) {
            best_score = score;
            best_name = name;
        }
    }
    cout << fixed << setprecision(2);
    cout << (double)total / n << '\n';
    cout << best_name << '\n';
    return 0;
}
