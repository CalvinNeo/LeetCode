use crate::util::*;

pub fn run() {
    assert_eq!(1, Solution::find_kth_largest(vec![2,1], 2));
    assert_eq!(1, Solution::find_kth_largest(vec![1], 1));
    assert_eq!(5, Solution::find_kth_largest(vec![3,2,1,5,6,4], 2));
    assert_eq!(4, Solution::find_kth_largest(vec![3,2,3,1,2,4,5,5,6], 4));
}

pub fn qs(nums: &mut Vec<i32>, l: usize, r: usize, k: usize) -> i32 {
    if l == r {
        return nums[l];
    }
    let p = nums[r];
    // println!("handle {:?} p {}", &nums[l..=r], p);
    // [r] is p
    // [l, i-1] <= p
    // [i, j-1] > p
    // [j, r-1] pending
    let mut i = l;
    let mut j = l;
    while j < r {
        if nums[j] > p {
            // 6  7  4
            // ij    p
            // 6  7  4
            // i  j
            j += 1
        } else {
            // move nums[j] into <= p
            nums.swap(i, j);
            i += 1;
            j += 1;
        }
    }
    // Now p located at i
    // println!("should place p={} at i={} k {} nums {:?}", p, i, k, nums);
    // 6  7  4
    // i  j  p
    nums.swap(i, r);
    // println!("after swap {} with {}, nums {:?}", i, r, nums);
    if k == i {
        return p;
    } else if k < i {
        return qs(nums, l, i - 1, k);
    } else {
        return qs(nums, i + 1, r, k);
    }
}

impl Solution {
    pub fn find_kth_largest(nums: Vec<i32>, k: i32) -> i32 {
        let mut nums = nums;
        let r = nums.len() - 1;
        if r == 0 {
            return nums[0];
        }
        let ksmall = r + 1 - k as usize;
        // println!("find {}st small in {:?}", ksmall, nums);
        return qs(&mut nums, 0, r, ksmall);
    }
}