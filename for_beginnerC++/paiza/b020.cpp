#define _GLIBCXX_DEBUG
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
#define rep(i, n) for(int i = 0; i < (int)(n); i++)
#define all(v) (v).begin(), (v).end()

int main() {
  int n;
  cin >> n;
  vector<string> queri(n);
  cin.ignore(); // 改行文字捨てる
  int now = 0;
  rep(i, n) {
    string a, b, page;
    cin >> a >> b;
    cin.ignore(); // スペース捨てる
    getline(cin, page); //スペース込みで一行取得
    if(a == "go") {
      queri[i] = page;
      now = i;
    } else {
      queri[i] = queri[now - 1];
      now--;
    }
  }
  for(string x : queri) {
    cout << x << endl;
  }
}
