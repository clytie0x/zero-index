#include <bits/stdc++.h>
using namespace std;

const int MOD = 1000000007;

string code;

long long decode(int pos)
{
    if (pos == (int)code.size()) {
        return 1;
    }
    if (code[pos] == '0') {
        return 0;
    }
    long long total = decode(pos + 1);
    if (pos + 1 < (int)code.size()) {
        int two = (code[pos] - '0') * 10 + (code[pos + 1] - '0');
        if (two <= 26) {
            total += decode(pos + 2);
        }
    }
    return total % MOD;
}

int main()
{
    cin >> code;
    cout << decode(0) << '\n';
    return 0;
}
