#include <bits/stdc++.h>
using namespace std;

int main()
{
    int a, b, c, money;
    cin >> a >> b >> c >> money;
    long long ways = 0;
    for (int x = 0; x <= money / a; x++) {
        for (int y = 0; y <= money / b; y++) {
            for (int z = 0; z <= money / c; z++) {
                if (a * x + b * y + c * z == money) {
                    ways++;
                }
            }
        }
    }
    cout << ways << '\n';
    return 0;
}
