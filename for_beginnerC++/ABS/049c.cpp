#define _GLIBCXX_DEBUG
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
#define rep(i, n) for(int i = 0; i < (int)(n); i++)
#define all(v) (v).begin(), (v).end()

int main() {
  string s;
  cin >> s;
  reverse(all(s));
  string divide[4] = {"dream", "dreamer", "erase", "eraser"};
  rep(i, 4) {
    reverse(all(divide[i]));
  }
  // bool ok = true;
  for(int i = 0; i < s.size();) {
    bool ok = false;
    for(int j = 0; j < 4; j++) {
      string tmp = divide[j];
      if(s.substr(i, tmp.size()) == tmp) {
        ok = true;
        i += tmp.size();
      }
    }
    if(ok == false) {
      cout << "NO" << endl;
      return 0;
    }
  }
  cout << "YES" << endl;
}
