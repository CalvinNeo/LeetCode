impl Solution {
    pub fn max_score_sightseeing_pair_wa(values: Vec<i32>) -> i32 {
        let n = values.len();
        let f = |i, j| -> i32 {
            if i == j {
                return 0;
            }
            values[i] + values[j] + i as i32 - j as i32
        };
        let mut i = 0;
        let mut j = n - 1;
        let mut mx = 0;
        while i < j {
            let h = std::cmp::min(values[i], values[j]);
            mx = std::cmp::max(mx, f(i, j));
            while i < j && values[i] <= h {
                i+=1;
            }
            while i < j && values[j] <= h {
                j-=1;
            }
        }
        mx
    }

        pub fn max_score_sightseeing_pair_wa2(values: Vec<i32>) -> i32 {
        let n = values.len();
        let f = |i, j| -> i32 {
            if i == j {
                return 0;
            }
            values[i] + values[j] + (i as i32) - (j as i32)
        };
        let mut i = 0;
        let mut j = 1;
        if n == 1 {
            return 0;
        } else if n == 2 {
            return f(0, 1);
        }
        let mut mx = f(0, 1);
        while true {
            // println!("== {} {}", i, j);
            while j + 1 < n && f(i, j + 1) > mx {
                j += 1;
                mx = std::cmp::max(mx, f(i, j));
            }
            println!("==1 {} {} {}", i, j, f(i, j));
            // now f(i, j) <= mx or j == n - 1
            while i < j && f(i, j) > mx {
                mx = std::cmp::max(mx, f(i, j));
                i += 1;
            }
            println!("==2 {} {} {}", i, j, f(i, j));
            // now f(i, j) <= mx or i == j
            if i == j && j == n - 1 {
                break;
            }
            // Error here:
            // Now we can advance neither i nor j, we will stuck here
            // if j + 1 < n {
            //     j += 1;
            // } else if i < j {
            //     i += 1
            // } else {
            //     break;
            // }
        }
        mx
    }
}

fn main() {
    println!("{}", Solution::max_score_sightseeing_pair(vec![8,1,5,2,6])); // 11
    println!("{}", Solution::max_score_sightseeing_pair(vec![7,8,8,10])); // 17
    println!("{}", Solution::max_score_sightseeing_pair(vec![5,3,1])); // 7
    println!("{}", Solution::max_score_sightseeing_pair(vec![1,7,10,4])); // 16
}