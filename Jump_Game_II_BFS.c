/*
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

For example:
Given array A = [2,3,1,1,4]

The minimum number of jumps to reach the last index is 2. (Jump 1 step from index 0 to 1, then 3 steps to the last index.)
E.g.2,3,4,1,1,2,8,3,4--> 2/3,4/1,1,2,8/3,4
*/
int Max(int a, int b)
{
    if(a >= b) return a;
    else return b;
}
int jump(int* nums, int numsSize) {
    int max = 0;
    int pre_max = 0;
    int step = 0;
    int i = 0;
    for(i=0; i < numsSize-1; i++)
    {
        max = Max(max, nums[i]+i);
        if(max >= numsSize-1)
        {
            step++;
            return step;
        }
        else
        {   
            if(pre_max == i) 
            {   step++;
               pre_max = max;
            }
        }
    }
    return step;
}
