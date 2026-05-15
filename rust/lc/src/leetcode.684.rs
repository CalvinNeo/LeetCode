impl Solution {
    pub fn find_redundant_connection(edges: Vec<Vec<i32>>) -> Vec<i32> {
        let mut fset: Vec<i32> = (0i32..edges.len() as i32 +1).collect::<Vec<_>>();
        let fa = |f: &[i32], x: i32| -> i32 {
            let mut i = x;
            while f[i as usize] != i {
                i = f[i as usize];
            }
            i
        };
        let mer = |f: &mut[i32], x: i32, y: i32| {
            let fx = fa(&f, x);
            let fy = fa(&f, y);
            f[fx as usize] = fy;
        };
        for v in edges.iter() {
            let x = v[0];
            let y = v[1];
            if fa(&fset, x) == fa(&fset, y) {
                let mut r = vec![x, y];
                r.sort();
                return r;
            } else {
                mer(&mut fset, x, y);
            };
        }
        vec![]
    }
}