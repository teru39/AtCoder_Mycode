#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef pair<int, int> P;
#define rep(i, n) for(int i = 0; i < (n); i++)
#define all(v) (v).begin(), (v).end()

int main() {
  int N;
  cin >> N;
  vector<string> ans;
  rep(i, N) {
    string s;
    cin >> s;
    string output = "";

    for(auto x : s) {
      switch(tolower(x)) {
      case 'b':
      case 'c':
        output += "1";
        /* code */
        break;
      case 'd':
      case 'w':
        output += "2";
        break;
      case 't':
      case 'j':
        output += "3";
        break;
      case 'f':
      case 'q':
        output += "4";
        break;
      case 'l':
      case 'v':
        output += "5";
        break;
      case 's':
      case 'x':
        output += "6";
        break;
      case 'p':
      case 'm':
        output += "7";
        break;
      case 'h':
      case 'k':
        output += "8";
        break;
      case 'n':
      case 'g':
        output += "9";
        break;
      case 'z':
      case 'r':
        output += "0";
        break;
      default:
        break;
      }
    }
    if(output != "") ans.push_back(output);
  }
  for(int i = 0; i < ans.size(); i++) {
    if(i != ans.size() - 1)
      cout << ans[i] << " ";
    else
      cout << ans[i] << endl;
  }
  if(ans.size() == 0) cout << endl;
  return 0;
}
