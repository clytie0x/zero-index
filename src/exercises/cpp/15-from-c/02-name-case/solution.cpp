#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    cin >> n;
    for (int i = 0; i < n; i++) {
        string first, last;
        cin >> first >> last;
        for (char &c : first) {
            c = tolower(c);
        }
        first[0] = toupper(first[0]);
        char initial = toupper(last[0]);
        cout << first << ' ' << initial << ".\n";
    }
    return 0;
}
