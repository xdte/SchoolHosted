#include <bits/stdc++.h>
using namespace std;

int main() {
    vector<int> a;
    while (true) {
        double f;
        cin >> f;
        if (f == -1) break;
        a.push_back(f);
    }
    double ans = 0;
    for (int i = 0; i < a.size(); i++) {
        ans += a[i];
    }
    double ansans = ans / a.size();
    cout << setprecision(6) << fixed << ansans << endl;