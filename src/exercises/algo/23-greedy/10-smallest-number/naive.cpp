#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n, k;
    string digits;
    cin >> n >> k >> digits;
    for (int round = 0; round < k; round++) {
        int remove = (int)digits.size() - 1;
        for (int i = 0; i + 1 < (int)digits.size(); i++) {
            if (digits[i] > digits[i + 1]) {
                remove = i;
                break;
            }
        }
        digits.erase(remove, 1);
    }
    int start = 0;
    while (start + 1 < (int)digits.size() && digits[start] == '0') {
        start++;
    }
    cout << digits.substr(start) << '\n';
    return 0;
}
