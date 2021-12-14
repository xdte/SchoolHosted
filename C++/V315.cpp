#include <bits/stdc++.h>
using namespace std;
int main() {
  int max = 101;
  int n;
  cin >> n;
  while (n--) {
    int x;
    cin >> x;
    if (x<max) max = x;
  }cout << max;
}
