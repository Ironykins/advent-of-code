# This sounds like a job for regular expressions.

cat day5.txt |
  grep -E '(.)\1' |
  grep -E '[aeiou].*[aeiou].*[aeiou]' |
  grep -E -v '(ab|cd|pq|xy)' |
  wc -l
