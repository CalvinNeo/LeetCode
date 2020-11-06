package main

import (
    "fmt"
    "sort"
    "strings"
    "strconv"
)

var ans map[string] int = make(map[string] int)

func iter(n int, cur int, lst string, nums []int) {
    if n == cur{
        ans[lst] = 1
    }else{
        v := strconv.Itoa(nums[cur])
        if lst == ""{
            iter(n, cur + 1, v, nums)
        }else{
            iter(n, cur + 1, lst + "," + v, nums)
        }
        iter(n, cur + 1, lst, nums)
    }
}

func subsetsWithDupAC1(nums []int) (ret [][]int) {
    sort.Ints(nums)
    ans = make(map[string] int)
    iter(len(nums), 0, "", nums)
    for s, _ := range ans {
        lst := make([]int, 0)
        // fmt.Printf("%v\n", s)
        for _, ch := range strings.Split(s, ","){
            v, _ := strconv.Atoi(ch)
            // fmt.Printf("=== %v\n", v)
            if ch != ""{
                lst = append(lst, v)
            }
        }
        ret = append(ret, lst)
    }
    return
}


func subsetsWithDup(nums []int) (ret [][]int) {
    sort.Ints(nums)
    n := len(nums)
    i := 0
    ret = append(ret, []int{})
    for i < n{
        // 如果是新的
        j := i
        for j < n{
            if nums[j] != nums[i]{
                break
            }
            j ++
        }
        // [i, j)的值是相同的，都为nums[i]
        nr := len(ret)
        // fmt.Printf("=== %v %v %v\n", i, j, ret)
        // for a := 0; a < nr; a++{
        //     fmt.Printf("++ %v\n", ret[a])
        // }
        new_ret := make([][]int, nr)
        copy(new_ret, ret)
        for a := 0; a < nr; a++{
            // 对于每一个已有的lst，分别添加0-l个当前的数
            prefix := make([]int, len(ret[a]))
            copy(prefix, ret[a])
            for k := i + 1; k <= j; k++{
                // fmt.Printf("%v/%v %v %v", a, nr, prefix, nums[i:k])
                new_slice := append(prefix, nums[i:k]...)
                // fmt.Printf("%v\n", new_slice)
                new_ret = append(new_ret, new_slice)
            }
        }
        ret = new_ret
        i = j
    }
    return
}

func subsetsWithDupWA(nums []int) (ret [][]int) {
    sort.Ints(nums)
    n := len(nums)
    i := 0
    ret = append(ret, []int{})
    for i < n{
        // 如果是新的
        j := i
        for j < n{
            if nums[j] != nums[i]{
                break
            }
            j ++
        }
        // [i, j)的值是相同的，都为nums[i]
        nr := len(ret)
        fmt.Printf("=== %v %v %v\n", i, j, ret)
        new_ret := make([][]int, nr)
        copy(new_ret, ret)
        for a := 0; a < nr; a++{
            // 对于每一个已有的lst，分别添加0-l个当前的数
            fmt.Printf("++ %v %v\n", a, ret)
            for k := i + 1; k <= j; k++{
                r := make([]int, len(nums[i:k]))
                copy(r, nums[i:k])
                l := make([]int, len(ret[a]))
                copy(l, ret[a])
                new_slice := append(l, r...)
                fmt.Printf("%v/%v %v %v %v\n", a, nr, ret[a], nums[i:k], new_slice)
                new_ret = append(new_ret, new_slice)
            }
        }

        ret = new_ret
        i = j
    }
    return
}

func main(){
    // fmt.Printf("%v\n", subsetsWithDup([]int{1,2,2}))
    // fmt.Printf("%v\n", subsetsWithDup([]int{0,3,5,7,9}))
    fmt.Printf("%v\n", subsetsWithDupWA([]int{0,3,5,7,9}))
    // fmt.Printf("%v\n", subsetsWithDup([]int{0,3,5,7}))
}