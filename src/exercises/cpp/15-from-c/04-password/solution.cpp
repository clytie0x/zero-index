#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    cin >> n;
    for (int i = 0; i < n; i++) {
        string password;
        cin >> password;
        bool has_upper = false, has_lower = false, has_digit = false;
        for (char c : password) {
            if (c >= 'A' && c <= 'Z') {
                has_upper = true;
            } else if (c >= 'a' && c <= 'z') {
                has_lower = true;
            } else if (c >= '0' && c <= '9') {
                has_digit = true;
            }
        }
        if ((int)password.size() < 8) {
            cout << "TOO SHORT\n";
        } else if (!has_upper) {
            cout << "NO UPPERCASE\n";
        } else if (!has_lower) {
            cout << "NO LOWERCASE\n";
        } else if (!has_digit) {
            cout << "NO DIGIT\n";
        } else {
            cout << "OK\n";
        }
    }
    return 0;
}
