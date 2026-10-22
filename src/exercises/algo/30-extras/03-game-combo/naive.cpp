#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    string presses, combo;
    cin >> presses >> combo;
    int n = presses.size();
    int m = combo.size();
    long long count = 0;
    int first = -1;
    for (int i = 0; i + m <= n; i++) {
        int j = 0;
        while (j < m && presses[i + j] == combo[j]) {
            j++;
        }
        if (j == m) {
            count++;
            if (first == -1) {
                first = i + 1;
            }
        }
    }
    cout << count << '\n' << first << '\n';
    return 0;
}
