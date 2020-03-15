#define _GLIBCXX_DEBUG
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
#define rep(i, n) for(int i = 0; i < (int)(n); i++)
#define all(v) (v).begin(), (v).end()

int main() {
  int n, m;
  cin >> n >> m;
  int point = 0;
  rep(i, m) {
    int pay;
    cin >> pay;
    if(point >= pay) {
      point -= pay;
    } else {
      n -= pay;
      point += pay / 10;
    }
    cout << n << " " << point << endl;
  }
}
