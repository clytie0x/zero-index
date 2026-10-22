#include <bits/stdc++.h>
using namespace std;

int main()
{
    string marbles;
    cin >> marbles;
    int pairs = 0;
    bool changed = true;
    while (changed) {
        changed = false;
        for (int i = 0; i + 1 < (int)marbles.size(); i++) {
            if (marbles[i] == marbles[i + 1]) {
                marbles.erase(i, 2);
                pairs++;
                changed = true;
                break;
            }
        }
    }
    cout << pairs << '\n';
    if (marbles.empty()) {
        cout << "EMPTY\n";
    } else {
        cout << marbles << '\n';
    }
    return 0;
}
