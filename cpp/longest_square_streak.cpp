class Solution
{
public:
    int longestSquareStreak(vector<int> &nn)
    {
        sort(begin(nn), end(nn));
        unordered_map<int, int> m;
        int out{};
        for (const auto &n : nn)
            if (int t = sqrt(n); t * t == n)
                out = max(out, m[n] = m[t] + 1);
            else
                m[n] = 1;
        return out > 1 ? out : -1;
    }
};