use std::borrow::Borrow;
use std::ops::Deref;
use crate::util::*;

type TreeNode = RawTreeNode<i32>;

pub enum Res {
    Ok(i32),
    Elapsed(i32),
}

pub fn dfs(nd: Option<Rc<RefCell<TreeNode>>>, kk: i32) -> Res {
    if nd.is_none() {
        return Res::Elapsed(0);
    }
    let mut remained = kk;
    let mut total = 0;
    let nd = nd.unwrap();
    // Seem Leetcode do not suppoer nd.deref().
    match dfs((*nd).borrow().left.clone(), remained) {
        Res::Ok(x) => return Res::Ok(x),
        Res::Elapsed(e) => {
            remained -= e;
            total += e;
        }
    };
    if remained == 0 {
        return Res::Ok((*nd).borrow().val);
    }
    remained -= 1;
    total += 1;
    match dfs((*nd).borrow().right.clone(), remained) {
        Res::Ok(x) => return Res::Ok(x),
        Res::Elapsed(e) => {
            remained -= e;
            total += e;
        }
    };
    return Res::Elapsed(total);
}

impl Solution {
    pub fn kth_smallest(root: Option<Rc<RefCell<TreeNode>>>, k: i32) -> i32 {
        match dfs(root, k - 1) {
            Res::Ok(x) => return x,
            _ => panic!("unreachable!()"),
        }
    }
}