
use crate::util::*;

type TreeNode = RawTreeNode<i32>;

use std::cell::RefCell;
use std::rc::Rc;
use std::ops::Deref;
use std::collections::HashMap;
use std::collections::hash_map::Entry;
// son -> father
type US = HashMap<isize, Rc<RefCell<TreeNode>>>;

pub fn hash(a: &Rc<RefCell<TreeNode>>) -> isize {
    a.as_ptr() as *const _ as isize
}
pub fn merge(us : &mut US, as_father: Rc<RefCell<TreeNode>>, as_son: Rc<RefCell<TreeNode>>) {
    let as_father_father = find(us, as_father);
    let as_son_father = find(us, as_son);
    us.insert(hash(&as_son_father), as_father_father);
}
pub fn find(us : &mut US, a: Rc<RefCell<TreeNode>>) -> Rc<RefCell<TreeNode>> {
    let mut a = a;
    loop {
        let ha = hash(&a);
        match us.entry(ha) {
            Entry::Occupied(o) => {
                if *o.get() == a {
                    return a;
                }
                a = o.get().clone();
            }
            Entry::Vacant(v) => {
                // This is root
                v.insert(a.clone());
                return a;
            }
        }
    }
}
impl Solution {
    pub fn dfs(us : &mut US, hit1: &mut bool, nd: Rc<RefCell<TreeNode>>, p: &Rc<RefCell<TreeNode>>, q: &Rc<RefCell<TreeNode>>) -> Option<Rc<RefCell<TreeNode>>> {
        if let Some(left) = nd.deref().borrow().left.clone() {
            if let Some(r) = Self::dfs(us, hit1,left.clone(), p, q) {
                return Some(r);
            }
            // x is black

            merge(us, nd.clone(), left);
        }
        if let Some(right) = nd.deref().borrow().right.clone() {
            if let Some(r) = Self::dfs(us, hit1, right.clone(), p, q) {
                return Some(r);
            }
            // x is black
            merge(us, nd.clone(), right);
        }
        if nd == *p || nd == *q {
            if *hit1 {
                return Some(if nd == *p {
                    find(us, q.clone())
                } else {
                    find(us, p.clone())
                });
            } else {
                *hit1 = true;
            }
        }
        return None
    }
    pub fn lowest_common_ancestor(root: Option<Rc<RefCell<TreeNode>>>, p: Option<Rc<RefCell<TreeNode>>>, q: Option<Rc<RefCell<TreeNode>>>) -> Option<Rc<RefCell<TreeNode>>> {
        let mut us = HashMap::default();
        let mut hit1 = false;
        Self::dfs(&mut us, &mut hit1, root.unwrap(), p.as_ref().unwrap(), q.as_ref().unwrap())
    }
}

pub fn run() {
    let null = -1;
    let t = make_treelist(&vec![3,5,1,6,2,0,8,null,null,7,4], null, 0);
    // print_treelist(t, 0);
    println!("{:?}", Solution::lowest_common_ancestor(t, make_treenode(5), make_treenode(1)));
}
