#!/usr/bin/env ruby

# Get the argument passed to the script
argument = ARGV[0]

# Define a regular expression
regex = /School/

# Use the scan method to find all occurrences of "School" in the argument
matches = argument.scan(regex)

# Join the matches into a single string
result = matches.join

# Print the result
puts result
