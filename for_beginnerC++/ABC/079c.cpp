#define _GLIBCXX_DEBUG
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
#define rep(i, n) for(int i = 0; i < (int)(n); i++)
#define all(v) (v).begin(), (v).end()

int main() {
  string s;
  cin >> s;
  for(int tmp = 0; tmp < (1 << 4); tmp++) {
    bitset<3> ss(tmp);
    int ans = 0;
    ans += s[0] - '0';
    for(int i = 0; i < 3; i++) {
      int cal;
      if(ss.test(i))
        cal = -(s[i + 1] - '0');
      else
        cal = s[i + 1] - '0';
      ans += cal;
    }
    if(ans == 7) {
      cout << s[0];
      rep(i, 3) {
        if(ss.test(i))
          cout << '-';
        else
          cout << '+';
        cout << s[i + 1];
      }
      cout << "=7" << endl;
      return 0;
    }
  }
}
