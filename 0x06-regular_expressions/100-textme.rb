#!/usr/bin/env ruby
# Script that extract and output: [SENDER],[RECEIVER],[FLAGS]
puts ARGV[0].scan(/\[(?:from:|to:|flags:)([^\]]+)\]/).join(",")
