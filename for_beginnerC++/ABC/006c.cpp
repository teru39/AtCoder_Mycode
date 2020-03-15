#define _GLIBCXX_DEBUG
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
#define rep(i, n) for(int i = 0; i < (int)(n); i++)
#define all(v) (v).begin(), (v).end()

int main() {
  int n, m;
  cin >> n >> m;

  //老人0人
  rep(i, n + 1) {
    if((4 * i) + (2 * (n - i)) == m) {
      printf("%d %d %d\n", n - i, 0, i);
      return 0;
    }
  }
  m -= 3;
  n -= 1;
  // 老人一人
  rep(i, n + 1) {
    if((4 * i) + (2 * (n - i)) == m) {
      printf("%d %d %d\n", n - i, 1, i);
      return 0;
    }
  }
  cout << "-1 -1 -1" << endl;
}
