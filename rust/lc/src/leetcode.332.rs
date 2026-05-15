
use std::collections::HashMap;
use std::collections::hash_map::Entry;
fn dfs(tickets: & Vec<Vec<String>>, g: &HashMap<String, Vec<usize>>, res: &mut Vec<usize>, vis: &mut Vec<bool>, cur: String) -> Option<Vec<usize>> {
    if res.len() == tickets.len() {
        return Some(res.clone());
    }
    let choices = match g.get(&cur) {
        Some(v) => v.iter().map(|e| *e).collect::<Vec<_>>(),
        None => return None,
    };
    for nxt in choices {
        if !vis[nxt] {
            vis[nxt] = true;
            res.push(nxt);
            let r = dfs(tickets, g, res, vis, tickets[nxt][1].clone());
            if r.is_some() {
                return r;
            }
            res.pop();
            vis[nxt] = false;
        }
    }
    None
}
impl Solution{
    pub fn find_itinerary(tickets: Vec<Vec<String>>) -> Vec<String> {
    let mut g = HashMap::<String, Vec<usize>>::default();
    for i in 0..tickets.len() {
        match g.entry(tickets[i][0].clone()) {
            Entry::Occupied(mut e) => {
                e.get_mut().push(i);
            },
            Entry::Vacant(v) => {
                v.insert(vec![i]);
            }
        }
    };
    for i in 0..tickets.len() {
        g.get_mut(&tickets[i][0]).unwrap().sort_by(| k1, k2 | tickets[*k1][1].as_bytes().cmp(tickets[*k2][1].as_bytes()));
    }

    let mut res = vec![];
    let mut vis = vec![false; tickets.len()];
    let mut ans = vec![String::from("JFK")];
    let ans1: Vec<usize> = dfs(&tickets, &g, &mut res, &mut vis, String::from("JFK")).unwrap();
    ans.append(&mut ans1.into_iter().map(|e| tickets[e][1].clone()).collect::<Vec<_>>());
    return ans;
}
}

