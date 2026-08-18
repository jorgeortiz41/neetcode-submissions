
func isAnagram(s string, t string) bool {
    // First check: strings must be same length
    if len(s) != len(t) {
        return false
    }

    // Create a charmap
    char_count_s := make(map[byte]int)
    char_count_t := make(map[byte]int)

    // Sort and compare
    for i:=0; i<len(s); i++ {
        char_count_s[s[i]] += 1
        char_count_t[t[i]] += 1
    }

    // Manual comparison instead of maps.Equals
    if len(char_count_s) != len(char_count_t) {
        return false
    }

    for key, val := range char_count_s {
        if char_count_t[key] != val {
            return false
        }
    }

    return true
}
