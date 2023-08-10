class Solution
{
public:
    vector<vector<int>> threeSum(vector<int> &nums)
    {
        sort(nums.begin(), nums.end());
        set<vector<int>> s;
        vector<vector<int>> output;
        int i, j, k, sum;

        for (i = 0; i < nums.size(); i++)
        {
            j = i + 1;
            k = nums.size() - 1;

            while (j < k)
            {
                sum = nums[i] + nums[j] + nums[k];
                if (sum == 0)
                {
                    s.insert({nums[i], nums[j], nums[k]});
                    j++;
                    k--;
                }
                else if (sum < 0)
                    j++;
                else
                    k--;
            }
        }
        for (auto in : s)
            output.push_back(in);

        return output;
    }
};

//best time
class Solution
{
public:
    vector<vector<int>> threeSum(vector<int> &nums)
    {
        vector<vector<int>> ret;
        sort(nums.begin(), nums.end());
        auto zero = nums.cend();
        vector<int>::const_iterator l, r, il, ir;
        for (auto i = nums.cbegin(); i < zero; i++)
        {
            if (*i >= 0)
            {
                zero = i;
                break;
            }
        }

        for (auto i = nums.cbegin(); i < zero + 1; i++)
        {
            l = i + 1;
            r = nums.cend() - 1;

            while (l < r)
            {
                if (*i + *l + *r > 0)
                {
                    r--;
                }
                else if (*i + *l + *r < 0)
                {
                    l++;
                }
                else
                {
                    ret.push_back({*i, *l, *r});
                    il = l;
                    ir = r;
                    while ((l < r) && (*ir == *r))
                        r--;
                    while ((l < r) && (*il == *l))
                        l++;
                }
            }

            while ((i < zero) && (*i == *(i + 1)))
                i++;
        }
        return ret;
    }
};

//best space
class Solution
{
public:
    vector<vector<int>> threeSum(vector<int> &nums)
    {
        sort(nums.begin(), nums.end());

        vector<vector<int>> v;
        int n = nums.size();

        for (int i = 0; i < n; ++i)
        {
            int j = i + 1;
            int k = n - 1;

            // Same target as before, skip.
            if (i != 0 && nums[i] == nums[i - 1])
            {
                continue;
            }

            while (k > j)
            {
                if (k == j)
                {
                    --k;
                    continue;
                }
                int curr = nums[i] + nums[j] + nums[k];
                if (curr == 0)
                {
                    v.push_back({nums[i], nums[j], nums[k]});
                    // Skip over dupes.
                    do
                    {
                        ++j;
                    } while (j < n && nums[j] == nums[j - 1]);
                    do
                    {
                        --k;
                    } while (k > 0 && nums[k] == nums[k + 1]);
                }
                else if (curr < 0)
                {
                    ++j;
                }
                else if (curr > 0)
                {
                    --k;
                }
            }
        }
        return v;
    }
    // -1 -1 -1 0 0 0 1 1 2
};