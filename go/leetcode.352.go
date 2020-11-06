// package main

import (
    // "fmt"
    "sort"
)

type Range struct{
    l int
    r int
    father *Range
    rank int
}


func Min(a, b int) int{
    if a < b{
        return a
    }
    return b
}
func Max(a, b int) int{
    if a > b{
        return a
    }
    return b
}


func (this *SummaryRanges) NewRange(v int) *Range{
    n := &Range{l: v, r:v, rank: 1}
    n.father = n
    return n
}
func (this *SummaryRanges) Find(n *Range) *Range{
    if n.father == n{
        return n
    }
    p := this.Find(n.father)
    // 懒更新
    n.father = p
    return p
}
func (this *SummaryRanges) Merge(a *Range, b *Range){
    pa := this.Find(a)
    pb := this.Find(b)
    if pa.rank < pb.rank{
        pa.father = pb
        pb.l = Min(pa.l, pb.l)
        pb.r = Max(pa.r, pb.r)
        this.root_map[pa] = nil
    }else{
        pb.father = pa
        if pa.rank == pb.rank{
            pa.rank ++
        }
        pa.l = Min(pa.l, pb.l)
        pa.r = Max(pa.r, pb.r)
        this.root_map[pb] = nil
    }
}

// func Init(n int){
//     father = make([]int, n)
//     for i := range father{
//         father[i] = i
//     }
// }

// func Find(v int) int{
//     if father[v] == v{
//         return v
//     }else{
//         return Find(father[v])
//     }
// }

// func Merge(a int, b int) int {
//     father[a] = b
// }

type SummaryRanges struct {
    range_map map[int]*Range
    root_map map[*Range]*Range
}


/** Initialize your data structure here. */
func Constructor() SummaryRanges {
    sum := SummaryRanges{range_map: make(map[int]*Range), root_map: make(map[*Range]*Range)}
    return sum
}


func (this *SummaryRanges) AddNum(val int)  {
    if _, ok := this.range_map[val]; ok {
        return
    }
    // 如果不存在，就在map和并查集中进行添加
    n := this.NewRange(val)
    this.range_map[val] = n
    this.root_map[n] = n

    if v, ok := this.range_map[val + 1]; ok{
        this.Merge(n, v)
    }
    if v, ok := this.range_map[val - 1]; ok{
        this.Merge(n, v)
    }
    return
}

type Ranges []*Range

func (rs Ranges) Len() int {
    return len(rs)
}

func (rs Ranges) Swap(i, j int) {
    rs[i], rs[j] = rs[j], rs[i]
}

func (rs Ranges) Less(i, j int) bool {
    return rs[i].l < rs[j].l
}

func (this *SummaryRanges) GetIntervals() (ans2 [][]int) {
    var ans Ranges
    for _, v := range this.root_map{
        if v != nil{
            ans = append(ans, v)
        }
    }
    if len(ans) >= 2 {
        sort.Sort(ans)
    }
    for _, ret := range ans {
        ans2 = append(ans2, []int{ret.l, ret.r})
    }
    return ans2
}


/**
 * Your SummaryRanges object will be instantiated and called as such:
 * obj := Constructor();
 * obj.AddNum(val);
 * param_2 := obj.GetIntervals();
 */

 // func main(){
 //    fmt.Printf("%v\n", 1)
 // }