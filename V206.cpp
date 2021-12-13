#include <bits/stdc++.h>
using namespace std;
int main() {
  int x;
  cin >> x;
  if (x%400==0) cout << "Yes";
  else if (x%4==0 and x%100 != 0) cout << "Yes";
  else cout << "No";
}
