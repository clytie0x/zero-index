#include <bits/stdc++.h>
using namespace std;

int main()
{
    long long n;
    cin >> n;
    long long count = 0;
    for (long long i = 1; i <= n; i++) {
        for (long long j = 1; j <= i; j *= 2) {
            count++;
        }
    }
    cout << count << '\n';
    return 0;
}
