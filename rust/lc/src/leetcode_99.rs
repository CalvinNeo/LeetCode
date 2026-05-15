use std::borrow::BorrowMut;
// Definition for a binary tree node.
// #[derive(Debug, PartialEq, Eq)]
// pub struct TreeNode {
//   pub val: i32,
//   pub left: Option<Rc<RefCell<TreeNode>>>,
//   pub right: Option<Rc<RefCell<TreeNode>>>,
// }
//
// impl TreeNode {
//   #[inline]
//   pub fn new(val: i32) -> Self {
//     TreeNode {
//       val,
//       left: None,
//       right: None
//     }
//   }
// }
use crate::util::*;
type TreeNode = RawTreeNode<i32>;

use std::rc::Rc;
use std::cell::RefCell;
use std::vec::Vec;
use std::ops::DerefMut;

pub fn dfs(deep: &mut usize, v: &mut Vec<i32>, root: Option<Rc<RefCell<TreeNode>>>) {
    if let Some(r) = root {
        dfs(deep, v, (*r).borrow().left.clone());
        v.push((*r).borrow().val);
        (*(*r).borrow_mut()).val = *deep as i32;
        *deep += 1;
        dfs(deep, v, (*r).borrow().right.clone());
    }
}

pub fn dfs2(v: &mut Vec<i32>, root: Option<Rc<RefCell<TreeNode>>>) {
    if let Some(r) = root {
        dfs2(v, (*r).borrow().left.clone());
        let index = (*(*r).borrow()).val as usize;
        (*(*r).borrow_mut()).val = *v.get(index).unwrap();
        dfs2(v, (*r).borrow().right.clone());
    }
}

static mut prev: Option<Rc<RefCell<TreeNode>>> = None;
static mut res: Vec<Rc<RefCell<TreeNode>>> = vec![];

impl Solution {
    pub fn recover_tree_1(root: &mut Option<Rc<RefCell<TreeNode>>>) {
        let mut v = vec![];
        let mut deep = 0 as usize;
        dfs(&mut deep, &mut v, root.clone());
        v.sort();
        println!("{:?}", v);
        let mut vd = v.into();
        dfs2(&mut vd, root.clone());
    }

    pub fn recover_tree(root: &mut Option<Rc<RefCell<TreeNode>>>) {
        unsafe {
        }
    }
}

pub fn run() {
    let null = -1;
    println!("{:?}", Solution::recover_tree(&mut make_treelist(&vec![1,3,null,null,2], null, 0)));
}