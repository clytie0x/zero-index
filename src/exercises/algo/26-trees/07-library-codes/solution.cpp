#include <bits/stdc++.h>
using namespace std;

struct Node {
    int key;
    Node *left;
    Node *right;
};

Node *insert(Node *root, int key)
{
    Node *node = new Node;
    node->key = key;
    node->left = nullptr;
    node->right = nullptr;
    if (root == nullptr) {
        return node;
    }
    Node *cur = root;
    while (true) {
        if (key < cur->key) {
            if (cur->left == nullptr) {
                cur->left = node;
                break;
            }
            cur = cur->left;
        } else {
            if (cur->right == nullptr) {
                cur->right = node;
                break;
            }
            cur = cur->right;
        }
    }
    return root;
}

Node *erase(Node *node, int key)
{
    if (node == nullptr) {
        return nullptr;
    }
    if (key < node->key) {
        node->left = erase(node->left, key);
        return node;
    }
    if (key > node->key) {
        node->right = erase(node->right, key);
        return node;
    }
    if (node->left == nullptr) {
        Node *child = node->right;
        delete node;
        return child;
    }
    if (node->right == nullptr) {
        Node *child = node->left;
        delete node;
        return child;
    }
    Node *next = node->right;
    while (next->left != nullptr) {
        next = next->left;
    }
    node->key = next->key;
    node->right = erase(node->right, next->key);
    return node;
}

int depth_of(Node *root, int key)
{
    int depth = 0;
    Node *cur = root;
    while (cur != nullptr) {
        if (key == cur->key) {
            return depth;
        }
        if (key < cur->key) {
            cur = cur->left;
        } else {
            cur = cur->right;
        }
        depth++;
    }
    return -1;
}

void preorder(Node *node, vector<int> &keys)
{
    if (node == nullptr) {
        return;
    }
    keys.push_back(node->key);
    preorder(node->left, keys);
    preorder(node->right, keys);
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int q;
    cin >> q;
    Node *root = nullptr;
    for (int k = 0; k < q; k++) {
        char op;
        int x;
        cin >> op >> x;
        if (op == '+') {
            root = insert(root, x);
        } else if (op == '-') {
            root = erase(root, x);
        } else {
            cout << depth_of(root, x) << '\n';
        }
    }
    vector<int> keys;
    preorder(root, keys);
    if (keys.empty()) {
        cout << "empty";
    }
    for (int i = 0; i < (int)keys.size(); i++) {
        if (i > 0) {
            cout << ' ';
        }
        cout << keys[i];
    }
    cout << '\n';
    return 0;
}
