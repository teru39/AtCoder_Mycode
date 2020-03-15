#define _GLIBCXX_DEBUG
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
#define rep(i, n) for(int i = 0; i < (int)(n); i++)
#define all(v) (v).begin(), (v).end()

// 移動先の座標をタプルで返す関数
tuple<int, int> move(char dir, int x, int y, vector<vector<char>> f, int h,
                     int w) {
  int nowx = x, nowy = y;

  if(dir == 'U') {
    nowy = y - 1;
  } else if(dir == 'R') {
    nowx = x + 1;
  } else if(dir == 'D') {
    nowy = y + 1;
  } else {
    nowx = x - 1;
  }
  // 動いた先が枠外ならその場の座標返す
  if(nowx < 0 || nowx >= w || nowy < 0 || nowy >= h) {
    return forward_as_tuple(x, y);
  } else if(f[nowy][nowx] == '#') { //動いた先が氷ならさらに再帰呼び出し
    return move(dir, nowx, nowy, f, h, w);
  } else { // 普通の床にうごいたら一手先の座標
    return forward_as_tuple(nowx, nowy);
  }
}

int main() {
  int h, w;
  cin >> h >> w;
  vector<vector<char>> field(h, vector<char>(w));
  rep(i, h) {
    rep(j, w) {
      cin >> field[i][j];
    }
  }
  int x, y, n;
  cin >> x >> y >> n;
  // 添え字と1ズレることに注意
  x--;
  y--;
  rep(i, n) {
    char dir;
    cin >> dir;
    tie(x, y) = move(dir, x, y, field, h, w);
  }
  // ずらした分を戻して出力
  x++;
  y++;
  cout << x << " " << y << endl;
}
