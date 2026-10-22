#include <bits/stdc++.h>
using namespace std;

int main()
{
    string digits;
    int k;
    cin >> digits >> k;
    sort(digits.begin(), digits.end());
    int count = 0;
    int smallest = -1;
    do {
        if (digits.size() > 1 && digits[0] == '0') {
            continue;
        }
        int value = 0;
        for (char ch : digits) {
            value = value * 10 + (ch - '0');
        }
        if (value % k == 0) {
            count++;
            if (smallest == -1) {
                smallest = value;
            }
        }
    } while (next_permutation(digits.begin(), digits.end()));
    cout << count << '\n';
    cout << smallest << '\n';
    return 0;
}
