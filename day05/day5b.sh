# This sounds like a job for more regular expressions.

cat day5.txt |
grep -E '((.){2}).*\1' |
grep -E '((.)).\1' |
wc -l
