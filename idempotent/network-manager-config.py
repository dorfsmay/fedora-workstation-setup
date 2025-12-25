#!/usr/bin/env python3

# configparser does not deal with comments.
# This function changes only what is necessary

import os
import re

file_path = "/etc/NetworkManager/NetworkManager.conf"

privacy_line = "ipv6.ip6-privacy=2\n"
partial_match = re.compile(r' *ipv6.ip6-privacy *= *\d+')

section = "[connection]\n"
section_match = re.compile(r'\[connection\]')

def rewrite_file(new_content):
    with open(file_path, 'w') as f:
        f.writelines(new_content)

def parse(content):
    not_comment = [ line.split('#')[0] for line in content ]

    # We assume that if the pattern if found it is in the right section
    # we don't check.

    for idx, line in enumerate(not_comment):
        if partial_match.search(line):
            # options set
            value = line.split("=")[1].strip()
            if value == "2":
                # set to the right value
                return
            else:
                # Wrong value, we replace
                content[idx] = privacy_line
                rewrite_file(content)
                return

    for idx, line in enumerate(not_comment):
        if section_match.search(line):
            # Found section, insert line
            content.insert(idx + 1, privacy_line)
            rewrite_file(content)
            return

    # add section and line
    content.append(section)
    content.append(privacy_line)
    rewrite_file(content)

def main():
    content = open(file_path).readlines()
    parse(content)

if __name__ == "__main__":
    main()

