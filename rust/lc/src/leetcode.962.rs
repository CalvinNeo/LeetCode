impl Solution {
    pub fn max_width_ramp_wa(nums: Vec<i32>) -> i32 {
        // Fails with [6,0,8,2,1,5]
        use std::cmp::Ordering;
        let mut s = vec![];
        let mut mx = 0;
        for (i, x) in nums.iter().enumerate() {
            if s.is_empty() {
                s.push((i as i32, 0));
                continue;
            }
            // If x can update mx with all previous elements j with a smaller A[j]
            // The stack is like 10 5 3 ...
            // We find the first j with A[j] < A[i], starting from left.

            // Returns arbitrary, so we can not use binary_search.
            // println!("{:?}", vec![1,1,2,2,3,3].binary_search_by(|y| y.cmp(&2))); // 3
            // println!("{:?}", vec![1,1,3,3].binary_search_by(|y| y.cmp(&2))); // 2
            let mut l = 0 as i32;
            let mut r = s.len() as i32 - 1;
            while l < r {
                let m = (l + r) / 2;
                let (mv, _) = s[m as usize];
                match mv.cmp(x) {
                    Ordering::Less => {
                        // test left
                        r = m;
                    },
                    Ordering::Equal => {
                        // test left
                        r = m;
                    },
                    Ordering::Greater => {
                        // test right
                        l = m + 1;
                    },
                }
            }

            let mut max_gap = 0;
            if s[l as usize].0 < *x {
                for (y, g) in s.drain(l as usize..).into_iter() {
                    println!("drain from {} with {}={} gap {} at {}={}", l, y, nums[y as usize], g, i, x);
                    let c = i as i32 - y + g;
                    max_gap = std::cmp::max(max_gap, c);
                }
            }

            mx = std::cmp::max(mx, max_gap);
            s.push((i as i32, max_gap));
        }
        mx
    }
    
    pub fn max_width_ramp(nums: Vec<i32>) -> i32 {
        use std::cmp::Ordering;
        let mut s = vec![];
        let mut mx = 0;
        for (i, x) in nums.iter().enumerate() {
            if s.is_empty() {
                s.push(i as i32);
                continue;
            }
            // If x can update mx with all previous elements j with a smaller A[j]
            // The stack is like 10 5 3 ...
            // We find the first j with A[j] < A[i], starting from left.

            let mut l = 0 as i32;
            let mut r = s.len() as i32 - 1;
            while l < r {
                let m = (l + r) / 2;
                let mv = nums[s[m as usize] as usize];
                match mv.cmp(x) {
                    Ordering::Less => {
                        // try left
                        r = m;
                    },
                    Ordering::Equal => {
                        // try left
                        r = m;
                    },
                    Ordering::Greater => {
                        // go right
                        l = m + 1;
                    },
                }
            }

            if nums[s[l as usize] as usize] <= *x {
                for y in s[l as usize..].iter() {
                    let c = i as i32 - y;
                    // println!("drain start from {} find {}={} is less than {}={} update {} s {:?}", l, y, nums[*y as usize], i, x, c, s);
                    mx = std::cmp::max(mx, c);
                }
            } else {
                // x is the smallest
                s.push(i as i32);
                // println!("no smaller than {}, s{:?}", x, s);
            }
        }
        mx
    }
}

// i < j and A[i] <= A[j]