use crate::util::*;

impl Solution {
    pub fn search_matrix(matrix: Vec<Vec<i32>>, target: i32) -> bool {
        let n = matrix.len();
        let row_end = {
            let mut l = 0;
            let mut r = n - 1;
            while l < r {
                let m = (l + r + 1) / 2;
                if matrix[m][0] > target {
                    // Not suitable.
                    r = m - 1;
                } else {
                    l = m;
                }
            }
            l
        };
        for i in 0..=row_end {
            match matrix[i].binary_search(&target) {
                Ok(_) => return true,
                _ => (),
            }
        }
        return false;
    }
}

