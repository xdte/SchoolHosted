#include <bits/stdc++.h>
using namespace std;
int main() {
  int x,y;
  cin >> x >> y;
  int ans=0;
  for (int i = 1;i<=x*y;i++) {
    if (i%x==0&&i%y==0) {
      ans = i;
      break;
    
  }}cout << ans << endl;
}
