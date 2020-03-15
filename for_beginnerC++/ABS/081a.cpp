#define _GLIBCXX_DEBUG
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
#define rep(i, n) for(int i = 0; i < (int)(n); i++)
#define all(v) (v).begin(), (v).end()

int main() {
  string s;
  cin >> s;
  int count = 0;
  rep(i, 3) {
    if(s[i] == '1') count++;
  }
  cout << count << endl;
}
