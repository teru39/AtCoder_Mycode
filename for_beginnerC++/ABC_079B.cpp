#include <bits/stdc++.h>
using namespace std;

int main()
{
    vector<long long> ans(90);
    int n;
    cin >> n;
    ans[0] = 2;
    ans[1] = 1;

    for (int i = 2; i <= n; i++)
    {
        ans[i] = ans[i - 1] + ans[i - 2];
    }

    cout << ans[n] << endl;
}
