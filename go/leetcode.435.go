package main

import (
    // "container/heap"
    "fmt"
    "sort"
)

// type IntHeap [][]int
 
// func (h IntHeap) Len() int           { return len(h) }
// func (h IntHeap) Less(i, j int) bool { return h[i][0] < h[j][0] }
// func (h IntHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }
// func (h *IntHeap) Push(x interface{}) {
//     // Push and Pop use pointer receivers because they modify the slice's length,
//     // not just its contents.
//     *h = append(*h, x)
// }
// func (h *IntHeap) Pop() interface{} {
//     old := *h
//     n := len(old)
//     x := old[n-1]
//     *h = old[0 : n-1]
//     return x
// }

type IntSlice [][]int  
 
func (c IntSlice) Len() int {  
    return len(c)  
}  
func (c IntSlice) Swap(i, j int) {  
    c[i], c[j] = c[j], c[i]  
}  
func (c IntSlice) Less(i, j int) bool {
    if c[i][0] == c[j][0]{
        return c[i][1] < c[j][1]
    }else{
        return c[i][0] < c[j][0]
    }
}  

func Min(x, y int) int {
    if x < y {
        return x
    }
    return y
}

func Max(x, y int) int {
    if x > y {
        return x
    }
    return y
}

func MaxIndex(arr []int) int{
    ansI := -1
    ansV := -100000
    for i, _ := range arr{
        if arr[i] > ansV{
            ansI = i
            ansV = arr[i]
        }
    }
    return ansI
}

func overlap(a []int, b []int) bool{
    x1 := Min(a[0], a[1])
    y1 := Max(a[0], a[1])
    x2 := Min(b[0], b[1])
    y2 := Max(b[0], b[1])

    if x2 >= y1 || x1 >= y2{
        return false
    }
    return true
}

func eraseOverlapIntervalsWA(intervals [][]int) int {
    ans := 0
    sort.Sort(IntSlice(intervals))
    var I = make([][]int, 0)
    for _, p := range intervals{
        // fmt.Printf("%v\n", p)
        if len(I) == 0{
            I = append(I, []int{p[0], p[1]})
        }else{
            px := I[len(I) - 1][0]
            py := I[len(I) - 1][1]
            if px != p[0] || py != p[1]{
                I = append(I, []int{p[0], p[1]})
            }else{
                ans ++
            }
        }
    }
    n := len(I)
    if n == 0{
        return 0
    }
    G := make([][]int, n)
    for i := range G {
        G[i] = make([]int, 0)
    }
    D := make([]int, n)
    for i := 0; i < n; i++{
        for j := i + 1; j < n; j++{
            is_over := overlap(I[i], I[j])
            if is_over{
                G[i] = append(G[i], j)
                G[j] = append(G[j], i)
                D[i] += 1
                D[j] += 1
            }
        }
    }

    for{
        mi := MaxIndex(D)
        if D[mi] == 0{
            break
        }
        for _, nxt := range G[mi]{
            D[nxt] -= 1
            D[mi] -= 1
        }
        // fmt.Printf("Remove %v %v\n", mi, D)
        ans += 1
    }
    return ans
}

type PairSlice [][]int  
 
func (c PairSlice) Len() int {  
    return len(c)  
}  
func (c PairSlice) Swap(i, j int) {  
    c[i], c[j] = c[j], c[i]  
}  
func (c PairSlice) Less(i, j int) bool {
    if c[i][1] == c[j][1]{
        return c[i][0] < c[j][0]
    }else{
        return c[i][1] < c[j][1]
    }
}

func eraseOverlapIntervals(intervals [][]int) int {
    n := len(intervals)
    if n == 0{
        return 0
    }
    var prev []int = nil
    ans := 0
    sort.Sort(PairSlice(intervals))
    // fmt.Printf("%v\n", intervals)
    for _, p := range intervals{
        if prev == nil{
            prev = p
        }else{
            if prev[1] == p[1] || p[0] < prev[1]{
                ans ++
            }else{
                prev = p
            }
        }
    }
    return ans
}

func main() {
    fmt.Printf("%v\n", eraseOverlapIntervals([][]int{{1,2},{2,3},{3,4},{1,3}})) // 1
    fmt.Printf("%v\n", eraseOverlapIntervals([][]int{{1,2},{1,2},{1,2}})) // 2
    fmt.Printf("%v\n", eraseOverlapIntervals([][]int{{1,2},{2,3}})) // 0
    fmt.Printf("%v\n", eraseOverlapIntervals([][]int{{0,2},{1,3},{1,3},{2,4},{3,5},{3,5},{4,6}})) // 4
}