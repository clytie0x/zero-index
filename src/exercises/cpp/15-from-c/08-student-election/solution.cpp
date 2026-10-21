#include <bits/stdc++.h>
using namespace std;

string name[10];
int votes[10];

void make_lower(string &word)
{
    for (char &c : word) {
        c = tolower(c);
    }
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int k;
    cin >> k;
    for (int i = 0; i < k; i++) {
        cin >> name[i];
    }
    int n;
    cin >> n;
    int invalid = 0;
    for (int b = 0; b < n; b++) {
        string ballot;
        cin >> ballot;
        make_lower(ballot);
        bool counted = false;
        for (int i = 0; i < k; i++) {
            if (ballot == name[i]) {
                votes[i]++;
                counted = true;
            }
        }
        if (!counted) {
            invalid++;
        }
    }
    int best = 0;
    for (int i = 0; i < k; i++) {
        cout << name[i] << ' ' << votes[i] << '\n';
        if (votes[i] > votes[best]) {
            best = i;
        }
    }
    cout << "invalid " << invalid << '\n';
    int winners = 0;
    for (int i = 0; i < k; i++) {
        if (votes[i] == votes[best]) {
            winners++;
        }
    }
    if (winners == 1) {
        cout << name[best] << '\n';
    } else {
        cout << "TIE\n";
    }
    return 0;
}
