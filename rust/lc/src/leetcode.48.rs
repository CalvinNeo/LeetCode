
impl Solution {
    pub fn rotate(matrix: &mut Vec<Vec<i32>>) {
        // (i,j) => (j,n-1-i)
        // (0,0) -> (0,2) -> (2,2) -> (2,0) -> (0,0)
        let n = matrix.len() as i32;
        if n == 1 {
            return;
        }
        let next = |i: i32, j: i32| -> (i32, i32) {
            (j, n-1-i)
        };
        let max_layer = n / 2;
        for layer in 0..max_layer {
            for i in layer..n-layer-1 {
                let mut x = layer;
                let mut y = i;
                let mut take_out = None;
                for it in 0..4 {
                    match take_out {
                        None => {
                            take_out = Some(matrix[x as usize][y as usize]);
                        },
                        Some(mut v) => {
                            std::mem::swap(&mut v, &mut matrix[x as usize][y as usize]);
                            take_out = Some(v);
                        }
                    }
                    if let (a, b) = next(x, y) {
                        x = a;
                        y = b;
                    }
                }
                matrix[layer as usize][i as usize] = take_out.unwrap();
            }
        }
    }
}
