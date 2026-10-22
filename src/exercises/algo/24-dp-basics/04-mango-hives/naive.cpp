#include <bits/stdc++.h>
using namespace std;

vector<long long> fruits;

long long most(int tree)
{
    if (tree <= 0) {
        return 0;
    }
    return max(most(tree - 1), most(tree - 2) + fruits[tree]);
}

int main()
{
    int n;
    cin >> n;
    fruits = vector<long long>(n + 1);
    for (int i = 1; i <= n; i++) {
        cin >> fruits[i];
    }
    cout << most(n) << '\n';
    return 0;
}
