#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for(int i = 0; i < (int)(n); i++)

int main() {
  int h, w;
  cin >> h >> w;
  vector<vector<char>> v(h, vector<char>(w));
  rep(i, h) {
    rep(j, w) {
      cin >> v[i][j];
    }
  }
  rep(i, h) {
    rep(j, w) {
      if(v[i][j] == '#') {
        cout << '#';
        continue;
      }
      int ans = 0;
      for(int y = -1; y <= 1; y++) {
        for(int x = -1; x <= 1; x++) {
          if(x + j < w && 0 <= x + j && y + i < h && 0 <= y + i &&
             v[y + i][x + j] == '#') {
            ans++;
          }
        }
      }
      cout << ans;
    }
    cout << endl;
  }
}
