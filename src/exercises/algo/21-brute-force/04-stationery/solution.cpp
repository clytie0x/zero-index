#include <bits/stdc++.h>
using namespace std;

int main()
{
    int a, b, c, money;
    cin >> a >> b >> c >> money;
    long long ways = 0;
    for (int x = 0; a * x <= money; x++) {
        for (int y = 0; a * x + b * y <= money; y++) {
            int left = money - a * x - b * y;
            if (left % c == 0) {
                ways++;
            }
        }
    }
    cout << ways << '\n';
    return 0;
}
