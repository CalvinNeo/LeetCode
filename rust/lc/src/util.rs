
#[derive(PartialEq, Eq, Clone, Debug)]
pub struct RawUniqueListNode<T> {
    pub val: T,
    pub next: Option<Box<RawUniqueListNode<T>>>
}

impl<T> RawUniqueListNode<T> {
    #[inline]
    fn new(val: T) -> Self {
        RawUniqueListNode {
            next: None,
            val
        }
    }
}

pub fn make_listnode<T>(lst: Vec<T>) -> Option<Box<RawUniqueListNode<T>>> {
    if lst.is_empty() {
        return None;
    }
    let mut next : Option<Box<RawUniqueListNode<T>>> = None;
    for v in lst.into_iter().rev() {
        next = Some(Box::new(RawUniqueListNode{ next, val: v }));
    }
    return next;
}

pub use std::rc::Rc;
pub use std::cell::RefCell;
pub use std::cmp::PartialEq;
use std::fmt::Display;
pub use std::ops::Deref;
// Note that in leetcode we can't import this.
pub use std::borrow::Borrow;

#[derive(Debug, PartialEq, Eq)]
pub struct RawTreeNode<T: PartialEq + Clone> {
  pub val: T,
  pub left: Option<Rc<RefCell<RawTreeNode<T>>>>,
  pub right: Option<Rc<RefCell<RawTreeNode<T>>>>,
}

impl<T: PartialEq + Clone> RawTreeNode<T> {
  #[inline]
  pub fn new(val: T) -> Self {
      RawTreeNode {
      val,
      left: None,
      right: None
    }
  }
}

pub fn make_treelist<T: PartialEq + Clone>(lst: &Vec<T>, null: T, index: usize) -> Option<Rc<RefCell<RawTreeNode<T>>>> {
    if let Some(x) = lst.get(index) {
        if *x != null {
            return Some(Rc::new(RefCell::new(RawTreeNode{
                val: x.clone(),
                left: make_treelist(lst, null.clone(), index * 2 + 1),
                right: make_treelist(lst, null.clone(), index * 2 + 2),
            })));
        }
    }
    return None;
}

pub fn make_treenode<T: PartialEq + Clone>(val: T) -> Option<Rc<RefCell<RawTreeNode<T>>>> {
    Some(Rc::new(RefCell::new(RawTreeNode{
        val,
        left: None,
        right: None,
    })))
}

pub fn print_treelist<T: PartialEq + Clone + Display>(root: Option<Rc<RefCell<RawTreeNode<T>>>>, pad: usize) {
    match root {
        Some(n) => {
            println!("{}{}", "    ".repeat(pad), n.deref().borrow().val);
            print_treelist(n.deref().borrow().left.clone(), pad + 1);
            print_treelist(n.deref().borrow().right.clone(), pad + 1);
        },
        None => {
            println!("{}-", "    ".repeat(pad));
        }
    }
}

pub struct Solution {}