class Solution {
    public int mySqrt(int x) {
        int l = 1;
        int r = x;

        while(l <= r){
            int mid = (l + r) / 2;

            if(x / mid == mid){
                return mid;
            } else if(mid > x / mid){
                r = mid - 1;
            } else {
                l = mid + 1;
            }
        }

        return r;
    }


    public static void main(String[] args) {
        Solution solution = new Solution();
        int x = 16; // test value for square root
        int result = solution.mySqrt(x);
        System.out.println("The square root of " + x + " is: " + result);
    }
    
}