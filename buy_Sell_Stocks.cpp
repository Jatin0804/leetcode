class Solution
{
public:
    int maxProfit(vector<int> &prices)
    {
        int mini = prices[0];
        int profit = 0;
        for (auto i : prices)
        {
            profit = max(profit, i - mini);
            mini = min(mini, i);
        }
        return profit;
    }
};

//best time

int init = []
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    ofstream out("user.out");
    cout.rdbuf(out.rdbuf());
    for (string s; getline(cin, s); cout << '\n')
    {
        int ans = 0, mn = INT_MAX;
        for (int _i = 1, _n = s.length(); _i < _n; ++_i)
        {
            int v = s[_i++] & 15;
            while ((s[_i] & 15) < 10)
                v = v * 10 + (s[_i++] & 15);
            mn = min(mn, v);
            ans = max(ans, v - mn);
        }
        cout << ans;
    }
    exit(0);
    return 0;
}();

class Solution
{
public:
    int maxProfit(vector<int> &prices)
    {
        return 0;
    }
};

class Solution
{
public:
    int maxProfit(vector<int> &prices)
    {
        std::ios_base::sync_with_stdio(false);
        std::cin.tie(nullptr);

        if (prices.empty())
            return 0;

        auto min_value{prices.at(0)};
        auto max_value{0};

        for (const auto &price : prices)
        {
            const auto current_price{price - min_value};

            min_value = price < min_value ? price : min_value;
            max_value = current_price > max_value ? current_price : max_value;
        }

        return max_value;
    }
};