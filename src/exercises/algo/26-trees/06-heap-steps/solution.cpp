#include <bits/stdc++.h>
using namespace std;

vector<int> heap = {0};

void sift_up(int i)
{
    while (i > 1 && heap[i / 2] < heap[i]) {
        swap(heap[i / 2], heap[i]);
        i /= 2;
    }
}

void sift_down(int i)
{
    int n = (int)heap.size() - 1;
    while (2 * i <= n) {
        int child = 2 * i;
        if (child + 1 <= n && heap[child + 1] > heap[child]) {
            child++;
        }
        if (heap[i] >= heap[child]) {
            break;
        }
        swap(heap[i], heap[child]);
        i = child;
    }
}

void print_heap()
{
    if (heap.size() == 1) {
        cout << "empty\n";
        return;
    }
    for (int i = 1; i < (int)heap.size(); i++) {
        if (i > 1) {
            cout << ' ';
        }
        cout << heap[i];
    }
    cout << '\n';
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    cin >> n;
    heap.resize(n + 1);
    for (int i = 1; i <= n; i++) {
        cin >> heap[i];
    }
    for (int i = n / 2; i >= 1; i--) {
        sift_down(i);
    }
    print_heap();
    int q;
    cin >> q;
    for (int k = 0; k < q; k++) {
        char op;
        cin >> op;
        if (op == '+') {
            int x;
            cin >> x;
            heap.push_back(x);
            sift_up((int)heap.size() - 1);
        } else {
            cout << heap[1] << '\n';
            heap[1] = heap.back();
            heap.pop_back();
            if (heap.size() > 1) {
                sift_down(1);
            }
        }
    }
    print_heap();
    return 0;
}
