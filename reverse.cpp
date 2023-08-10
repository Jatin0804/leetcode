class Solution
{
public:
    int reverse(int x)
    {
        int y = 0;
        int z = -1;
        bool xt = false;

        if (x < INT_MIN || x > INT_MAX)
            return 0;
        /*if (x<0)
        {
            xt=true;
            x = x*z;
        }*/
        while (x)
        {
            if (y < INT_MIN / 10 || y > INT_MAX / 10)
                return 0;
            y = y * 10 + x % 10;
            x = x / 10;
        }
        /*
        if (xt == true)
            y *= z;
        */
        return y;
    }
};


//best time

class Solution
{
public:
    int reverse(int x)
    {
        int r = 0; // decleare r
        while (x)
        {
            if (r > INT_MAX / 10 || r < INT_MIN / 10)
                return 0;        // check 32 bit range if r is outside the range then return 0
            r = r * 10 + x % 10; // find remainder and add its to r
            x = x / 10;          // Update the value of x
        }
        return r; // if r in the 32 bit range then return r
    }
};