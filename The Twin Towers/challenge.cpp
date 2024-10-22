#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int LCS(const vector<int>& tile_a, const vector<int>& tile_b) {
    int n = tile_a.size() + 1;
    int m = tile_b.size() + 1;

    vector<vector<int>> memo(n, vector<int>(m, 0));

    for (int i = 1; i < n; ++i) {
        for (int j = 1; j < m; ++j) {
            if (tile_a[i-1] == tile_b[j-1]) {
                memo[i][j] = memo[i-1][j-1] + 1;
            } else {
                memo[i][j] = max(memo[i-1][j], memo[i][j-1]);
            }
        }
    }

    return memo[n-1][m-1];
}

int main() {
    int sequence = 1;

    while (true) {
        int N1, N2;
        cin >> N1 >> N2;

        if (N1 == 0 && N2 == 0) {
            break;
        }

        vector<int> tile_a(N1);
        vector<int> tile_b(N2);

        for (int i = 0; i < N1; ++i) {
            cin >> tile_a[i];
        }
        for (int i = 0; i < N2; ++i) {
            cin >> tile_b[i];
        }

        int result = LCS(tile_a, tile_b);

        cout << "Twin Towers #" << sequence << endl;
        cout << "Number of Tiles : " << result << endl;
        cout << endl;

        sequence++;
    }

    return 0;
}