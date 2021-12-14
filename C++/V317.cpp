#include <bits/stdc++.h>
using namespace std;
int main() {
  bool flag = false;
  int n;
  cin >> n;
  while (n--) {
    int x;
    cin >> x;
    if (x<50) flag = true;
  }
  if (flag==true) cout << "Yes" << endl;
  else cout << "No" << endl;
}
