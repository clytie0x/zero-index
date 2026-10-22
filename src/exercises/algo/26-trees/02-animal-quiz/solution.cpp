#include <bits/stdc++.h>
using namespace std;

vector<int> left_child, right_child, visited;

void preorder(int v)
{
    if (v == 0) {
        return;
    }
    visited.push_back(v);
    preorder(left_child[v]);
    preorder(right_child[v]);
}

void inorder(int v)
{
    if (v == 0) {
        return;
    }
    inorder(left_child[v]);
    visited.push_back(v);
    inorder(right_child[v]);
}

void postorder(int v)
{
    if (v == 0) {
        return;
    }
    postorder(left_child[v]);
    postorder(right_child[v]);
    visited.push_back(v);
}

void print_and_clear()
{
    for (int i = 0; i < (int)visited.size(); i++) {
        if (i > 0) {
            cout << ' ';
        }
        cout << visited[i];
    }
    cout << '\n';
    visited.clear();
}

int main()
{
    int n;
    cin >> n;
    left_child.assign(n + 1, 0);
    right_child.assign(n + 1, 0);
    vector<bool> has_parent(n + 1, false);
    for (int v = 1; v <= n; v++) {
        cin >> left_child[v] >> right_child[v];
        has_parent[left_child[v]] = true;
        has_parent[right_child[v]] = true;
    }
    int root = 0;
    for (int v = 1; v <= n; v++) {
        if (!has_parent[v]) {
            root = v;
        }
    }
    preorder(root);
    print_and_clear();
    inorder(root);
    print_and_clear();
    postorder(root);
    print_and_clear();
    return 0;
}
