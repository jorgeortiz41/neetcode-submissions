func hasDuplicate(nums []int) bool {
    duplicates := make(map[int]int)
    for i:=0; i< len(nums); i++ {
        if duplicates[nums[i]] > 0 {
            return true
        } else {
            duplicates[nums[i]] = 1
        }
    }
    return false
}
