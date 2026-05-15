impl Solution {
    pub fn max_area(height: Vec<i32>) -> i32 {
        let n = height.len();
        let mut i = 0;
        let mut j = n - 1;
        let mut mx = 0;
        while i < j {
            let h = std::cmp::min(height[i], height[j]);
            let w = j - i;
            mx = std::cmp::max(mx, h * w);
            while i < j && height[i] <= h {
                i+=1;
            }
            while i < j && height[j] <= h {
                j-=1;
            }
        }
        mx
    }
}