func getConcatenation(nums []int) []int {
    result := make([]int, len(nums)*2)

    for i:=0; i<len(nums)*2;i++{
        if i >= len(nums) {
            result[i]= nums[i-(len(nums))]
        } else {
            result[i] = nums[i]
        }
    }
    return result
} 
