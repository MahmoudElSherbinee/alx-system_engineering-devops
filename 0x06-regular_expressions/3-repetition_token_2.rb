#!/usr/bin/env ruby

# Retrieve the argument passed to the script
input_string = ARGV[0]

# Define the regular expression pattern
pattern = /hbt+n/

# Scan the input string for matches using the defined pattern
matches = input_string.scan(pattern)

# Join the matched substrings into a single string
result = matches.join

# Output the resulting string
puts result
