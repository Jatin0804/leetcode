class Solution
{
public:
    vector<int> twoSum(vector<int> &nums, int target)
    {
        int n = nums.size();
        for (int i = 0; i < n - 1; i++)
        {
            for (int j = i + 1; j < n; j++)
            {
                if (nums[i] + nums[j] == target)
                    return {i, j};
            }
        }
        return {};
    }
};

//time

class Solution
{
public:
    vector<int> twoSum(vector<int> &nums, int target)
    {
        vector<pair<int, int>> v1;
        for (int i = 0; i < nums.size(); i++)
        {
            pair<int, int> p;
            p.first = nums[i];
            p.second = i;
            v1.push_back(p);
        }
        sort(v1.begin(), v1.end());
        int i = 0, j = v1.size() - 1;
        vector<int> ans;
        while (1)
        {
            if (v1[i].first + v1[j].first == target)
            {
                ans.push_back(v1[i].second);
                ans.push_back(v1[j].second);
                break;
            }
            else if ((v1[i].first + v1[j].first) > target)
            {
                j--;
            }
            else
            {
                i++;
            }
        }
        return ans;
    }
};