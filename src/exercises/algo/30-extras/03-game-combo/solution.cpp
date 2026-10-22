#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    string presses, combo;
    cin >> presses >> combo;
    int m = combo.size();
    string joined = combo + "#" + presses;
    int total = joined.size();
    vector<int> border(total, 0);
    long long count = 0;
    int first = -1;
    for (int i = 1; i < total; i++) {
        int j = border[i - 1];
        while (j > 0 && joined[i] != joined[j]) {
            j = border[j - 1];
        }
        if (joined[i] == joined[j]) {
            j++;
        }
        border[i] = j;
        if (j == m) {
            count++;
            if (first == -1) {
                first = i - 2 * m + 1;
            }
        }
    }
    cout << count << '\n' << first << '\n';
    return 0;
}
