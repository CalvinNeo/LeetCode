
use crate::util::*;

pub fn run() {
    println!("{}", Solution::nth_ugly_number(1));
    println!("{}", Solution::nth_ugly_number_wa(10));
}

impl Solution {
    pub fn nth_ugly_number_wa(n: i32) -> i32 {
        // What is wrong here is we need to record every res;
        let mut m2 = 2;
        let mut m3 = 3;
        let mut m5 = 5;
        let mut res = 1;
        for i in 0..n {
            res = *(vec![m2, m3, m5].iter().min().unwrap());
            if m2 <= res && res == m2 {
                m2 = res * 2;
            }
            if m3 <= res && res == m3 {
                m3 = res * 3;
            }
            if m5 <= res && res == m5 {
                m5 = res * 5;
            }
            println!("{}\t{}\t{}\t{}\t{}", i + 1, res, m2, m3, m5);
        }
        return res;
    }

    pub fn nth_ugly_number(n: i32) -> i32 {
        let mut m2 = 0;
        let mut m3 = 0;
        let mut m5 = 0;
        let mut res = vec![1];

        for i in 1..n {
            let n2 = res[m2] * 2;
            let n3 = res[m3] * 3;
            let n5 = res[m5] * 5;
            let nxt = *(vec![n2, n3, n5].iter().min().unwrap());
            if nxt == n2 {
                m2 += 1;
            }
            if nxt == n3 {
                m3 += 1;
            }
            if nxt == n5 {
                m5 += 1;
            }
            res.push(nxt);
        }
        return *res.last().unwrap();
    }
}