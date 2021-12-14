#include <bits/stdc++.h>
using namespace std;

int main() {
    int x;
    cin >> x;
    bool flag = false;
    for (int i = 2; i < x; i++) {
        if (x % i == 0) {
            flag = true;
        }
    }
    if (flag == true || x == 1)
        cout << "No" << endl;
    else
        cout << "Yes" << endl;
}