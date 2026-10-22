#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    string marbles;
    cin >> marbles;
    string rail;
    int pairs = 0;
    for (char c : marbles) {
        if (!rail.empty() && rail.back() == c) {
            rail.pop_back();
            pairs++;
        } else {
            rail.push_back(c);
        }
    }
    cout << pairs << '\n';
    if (rail.empty()) {
        cout << "EMPTY\n";
    } else {
        cout << rail << '\n';
    }
    return 0;
}
