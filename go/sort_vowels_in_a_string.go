//no. 2785
import(
  "sort"
  "string"
)


func checkVowel(s byte) bool{
    vowels := "AEIOUaeiou"
    for i := 0; i < len(vowels); i++{
        if s == vowels[i]{
            return true
        }
    }
    return false
}
func sortVowels(s string) string {
    var vowel_pos []int
    var vs []byte
    var chars []byte
    for i := 0; i < len(s); i++{
        chars = append(chars, s[i])
        if checkVowel(s[i]){
            vs = append(vs, s[i])
            vowel_pos = append(vowel_pos, i)
        }
    }
    if (len(vowel_pos) > 0){
        sort.Slice(vs, func(i, j int) bool {
            return vs[i] < vs[j]
        })
        for i := 0; i < len(vowel_pos); i++{
            chars[vowel_pos[i]] = vs[i]
        }
        s = string(chars[:])
    }
    return s
}
