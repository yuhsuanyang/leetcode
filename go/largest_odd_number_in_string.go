//no. 1903
func largestOddNumber(num string) string {
  var largest_index int
  for i := len(num) - 1; i >= 0; i--{
    if(int(num[i]) % 2 == 1){
      largest_index = i
      break
    }
  }
  if(largest_index == 0) && (int(num[0]) % 2 == 0){
      return ""
  }
  return num[0:largest_index+1]
}
