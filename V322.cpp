#include <bits/stdc++.h>
using namespace std;
int main() {
  int x,y;
  cin >> x >> y;
  int z,ans = 0;
  if (x>y) z=x;
  else z=y;
  for (int i=1; i<=z;i++){
    if (x%i==0&&y%i==0) ans = i;
  }
  cout << ans;
}
 