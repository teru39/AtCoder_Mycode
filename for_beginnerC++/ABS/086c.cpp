#define _GLIBCXX_DEBUG
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
#define rep(i, n) for(int i = 0; i < (int)(n); i++)
#define all(v) (v).begin(), (v).end()

int main() {
  int n;
  cin >> n;
  int x = 0, y = 0, t = 0;
  rep(i, n) {
    int tt, xx, yy;
    cin >> tt >> xx >> yy;
    if(((xx + yy) % 2) != (tt % 2)) {
      cout << "No" << endl;
      return 0;
    }
    if(tt - t < (abs(xx - x) + abs(yy - y))) {
      cout << "No" << endl;
      return 0;
    }
    t = tt;
    x = xx;
    y = yy;
  }
  cout << "Yes" << endl;
}
