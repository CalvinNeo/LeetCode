use crate::util::*;

type ListNode = RawUniqueListNode<i32>;

impl Solution {
    pub fn reverse_list(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        let mut prev = None;
        let mut cur = head;
        while cur.is_some() {
            let mut c = cur.unwrap();
            let next = c.next.take();
            c.next = prev;
            prev = Some(c);
            cur = next;
        }
        return prev;
    }
}

pub fn run() {
    println!("{:?}", Solution::reverse_list(make_listnode(vec![1, 2, 3])));
    println!("{:?}", Solution::reverse_list(make_listnode(vec![1])));
    println!("{:?}", Solution::reverse_list(make_listnode(vec![])));
}
