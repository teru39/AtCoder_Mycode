#define _GLIBCXX_DEBUG
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
#define rep(i, n) for(int i = 0; i < (int)(n); i++)
#define all(v) (v).begin(), (v).end()

int main() {
  int n, Y;
  cin >> n >> Y;
  rep(z, n + 1) {
    rep(y, n + 1 - z) {
      if(z * 1000 + y * 5000 + (n - z - y) * 10000 == Y) {
        cout << (n - z - y) << " " << y << " " << z << endl;
        return 0;
      }
    }
  }
  cout << "-1 -1 -1" << endl;
}
