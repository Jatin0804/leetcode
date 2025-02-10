class Solution
{
public:
    bool containsDuplicate(vector<int> &nums)
    {
        unordered_map<int, int> mp;
        for (int i = 0; i < nums.size(); i++)
            if (++mp[nums[i]] == 2)
                return true;

        return false;
    }
};

//best time

static bool _foo = ios::sync_with_stdio(false);
static ostream *_bar = cin.tie(NULL);
class Solution
{
public:
    bool containsDuplicate(vector<int> &nums)
    {
        sort(nums.begin(), nums.end());
        for (int i = 0; i < nums.size() - 1; i++)
        {
            if (nums[i] == nums[i + 1])
                return true;
        }
        return false;
    }
};