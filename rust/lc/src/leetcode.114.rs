
use std::borrow::BorrowMut;
use std::rc::Rc;
use std::cell::RefCell;
use std::ops::{Deref, DerefMut};


pub fn pre_order_wa(cur: Rc<RefCell<TreeNode>>) -> (Rc<RefCell<TreeNode>>, Rc<RefCell<TreeNode>>) {
    /// For every sub-tree `cur`:
    /// fn solve():
    ///     biggest(cur.left).right = cur;
    ///     cur.right = smallest(cur.right);
    ///
    /// We also noticed that we can
    /// fn solve():
    ///     biggest(solve(cur.left)).right = cur;
    ///     cur.right = smallest(solve(cur.right));
    ///
    /// Then
    /// biggest(solve(cur.left)) is the last node pre ordered by solve.
    /// smallest(solve(cur.right)) is the first node without left by solve.
    ///
    /// But how to be faster?
    /// Reconsider solve(cur.left) will sort out all left children, and return biggest(solve(cur.left)).
    /// Then we chain solve(cur.left) -> cur -> cur.right, and iterate over cur.right.
    ///
    /// What to return
    /// (smallest, biggest)
    /// What if we have no left for smallest and no right for biggest?
    /// We can't use cur. See "USE CUR ERROR WHEN HANDLE 2"

    let has_left = {
        cur.borrow().left.is_some()
    };
    let has_right = {
        cur.borrow().right.is_some()
    };

    if has_left {
        let left = cur.borrow().left.as_ref().unwrap().clone();
        let (smallest_left, biggest_left) = pre_order(left.clone());
        if has_right {
            let (smallest_right, biggest_right) = pre_order(cur.borrow().right.as_ref().unwrap().clone());
            println!("LR {} has smallest_left {} and biggest_left {} and smallest_right {} biggest_right {}", cur.borrow().val, smallest_left.borrow().val, biggest_left.borrow().val, smallest_right.borrow().val, biggest_right.borrow().val);
            {
                let mut x = cur.deref().borrow_mut();
                x.right.insert(left);
                x.left = None;
            }
            {
                let mut x = biggest_left.deref().borrow_mut();
                x.right.insert(smallest_right.clone());
                x.left = None;
            }
            println!("cur {:?}", cur);
            return (smallest_left, biggest_right);
        } else {
            println!("L {} has smallest_left {} and biggest_left {}", cur.borrow().val, smallest_left.borrow().val, biggest_left.borrow().val);
            {
                let mut x = cur.deref().borrow_mut();
                x.right.insert(left.clone());
                x.left = None;
            }
            println!("cur {:?}", cur);
            return (smallest_left, cur);
        }
    } else {
        // `cur` is the smallest in the tree rooted by `cur`,
        // we still need to pre_order right to find the biggest.
        if has_right {
            let right = cur.borrow().right.as_ref().unwrap().clone();
            let (smallest_right, biggest_right) = pre_order(cur.borrow().right.as_ref().unwrap().clone());
            println!("R {} has smallest_right {} and biggest_right {}", cur.borrow().val, smallest_right.borrow().val, biggest_right.borrow().val);
            {
                let mut x = cur.deref().borrow_mut();
                x.right.insert(right.clone());
                x.left = None;
            }
            return (cur, biggest_right);
        }
        {
            let mut x = cur.deref().borrow_mut();
            x.left = None;
        }
        println!("NO {}", cur.borrow().val);
        return (cur.clone(), cur.clone());
    };
}


pub fn pre_order(cur: Rc<RefCell<TreeNode>>) -> (Rc<RefCell<TreeNode>>, Rc<RefCell<TreeNode>>) {
    /// For every sub-tree `cur`:
    /// fn solve():
    ///     biggest(cur.left).right = cur;
    ///     cur.right = smallest(cur.right);
    ///
    /// We also noticed that we can
    /// fn solve():
    ///     biggest(solve(cur.left)).right = cur;
    ///     cur.right = smallest(solve(cur.right));
    ///
    /// Then
    /// biggest(solve(cur.left)) is the last node pre ordered by solve.
    /// smallest(solve(cur.right)) is the first node without left by solve.
    ///
    /// But how to be faster?
    /// Reconsider solve(cur.left) will sort out all left children, and return biggest(solve(cur.left)).
    /// Then we chain solve(cur.left) -> cur -> cur.right, and iterate over cur.right.
    ///
    /// What to return
    /// (smallest, biggest)
    /// What if we have no left for smallest and no right for biggest?
    /// We can't use cur. See "USE CUR ERROR WHEN HANDLE 2"

    let P = false;
    let has_left = {
        cur.borrow().left.is_some()
    };
    let has_right = {
        cur.borrow().right.is_some()
    };

    if has_left {
        let left = cur.borrow().left.as_ref().unwrap().clone();
        let (smallest_left, biggest_left) = pre_order(left.clone());
        if has_right {
            let right = cur.borrow().right.as_ref().unwrap().clone();
            let (smallest_right, biggest_right) = pre_order(cur.borrow().right.as_ref().unwrap().clone());
            if P {
                println!("LR {} has smallest_left {} and biggest_left {} and smallest_right {} biggest_right {}", cur.borrow().val, smallest_left.borrow().val, biggest_left.borrow().val, smallest_right.borrow().val, biggest_right.borrow().val);
            }
            {
                let mut x = cur.deref().borrow_mut();
                x.right.insert(left);
                x.left = None;
            }
            {
                let mut x = biggest_left.deref().borrow_mut();
                x.right.insert(right.clone());
                x.left = None;
            }
            if P {
                println!("cur {:?}", cur);
            }
            return (smallest_left, biggest_right);
        } else {
            if P {
                println!("L {} has smallest_left {} and biggest_left {}", cur.borrow().val, smallest_left.borrow().val, biggest_left.borrow().val);
            }
            {
                let mut x = cur.deref().borrow_mut();
                x.right.insert(left.clone());
                x.left = None;
            }
            if P {
                println!("cur {:?}", cur);
            }
            return (smallest_left, biggest_left);
        }
    } else {
        // `cur` is the smallest in the tree rooted by `cur`,
        // we still need to pre_order right to find the biggest.
        if has_right {
            let right = cur.borrow().right.as_ref().unwrap().clone();
            let (smallest_right, biggest_right) = pre_order(cur.borrow().right.as_ref().unwrap().clone());
            if P {
                println!("R {} has smallest_right {} and biggest_right {}", cur.borrow().val, smallest_right.borrow().val, biggest_right.borrow().val);
            }
            {
                let mut x = cur.deref().borrow_mut();
                x.right.insert(right.clone());
                x.left = None;
            }
            if P {
                println!("cur {:?}", cur);
            }
            return (cur, biggest_right);
        }
        {
            let mut x = cur.deref().borrow_mut();
            x.left = None;
        }
        if P {
            println!("NO {}", cur.borrow().val);
        }
        if P {
            println!("cur {:?}", cur);
        }
        return (cur.clone(), cur.clone());
    };
}
impl Solution {
    pub fn flatten(root: &mut Option<Rc<RefCell<TreeNode>>>) {
        match root {
            Some(r) => {
                pre_order(r.clone());
            }
            None => {
                return
            }
        }
    }
}

struct Solution {}

fn M<T>(x: T) -> Option<Rc<RefCell<T>>> {
    Some(Rc::new(RefCell::new(x)))
}

fn test() {
    let mut root = M(TreeNode {
        left: M(TreeNode {
            val: 2,
            left: M(TreeNode::new(3)),
            right: M(TreeNode::new(4)),
        }),
        right: M(TreeNode {
            val: 5,
            left: None,
            right: M(TreeNode::new(6)),
        }),
        val: 1,
    });
    Solution::flatten(&mut root);
    println!("{:?}", root); // 1 2 3 4 5 6
    let mut root = M(TreeNode {
        left: M(TreeNode {
            val: 2,
            left: M(TreeNode::new(3)),
            right: None,
        }),
        right: None,
        val: 1,
    });
    Solution::flatten(&mut root);
    println!("{:?}", root); // 1 2 3
    let mut root = M(TreeNode {
        left: None,
        right: M(TreeNode {
            val: 2,
            left: M(TreeNode::new(3)),
            right: None,
        }),
        val: 1,
    });
    Solution::flatten(&mut root);
    println!("{:?}", root); // 1 2 3
    // // USE CUR ERROR WHEN HANDLE 2
    let mut root = M(TreeNode {
        left: M(TreeNode {
            val: 2,
            left: M(TreeNode {
                val: 3,
                left: M(TreeNode::new(5)),
                right: None,
            }),
            right: M(TreeNode::new(4)),
        }),
        right: None,
        val: 1,
    });
    Solution::flatten(&mut root);
    println!("{:?}", root); // 1 2 3 5 4
    // [2,1,4,null,null,3]
    let mut root = M(TreeNode {
        left: M(TreeNode {
            val: 1,
            left: None,
            right: None,
        }),
        right: M(TreeNode {
            val: 4,
            left: M(TreeNode::new(3)),
            right: None,
        }),
        val: 2,
    });
    Solution::flatten(&mut root);
    println!("{:?}", root); // 2 1 4 3
}
