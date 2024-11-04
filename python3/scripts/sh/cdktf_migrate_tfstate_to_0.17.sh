#!/bin/bash

terraform plan -no-color | grep ' will be' -C 3 | grep ' resource' | sort > /tmp/diff.txt
cat /tmp/diff.txt | grep ' + ' > /tmp/plus
cat /tmp/diff.txt | grep ' - ' > /tmp/minus
paste /tmp/minus /tmp/plus | \
  sed 's/ + //g;s/ - //g;s/{//g;s/\"/ /g;s/[[:space:]]\+/ /g' | \
  awk '{print "terraform state mv -dry-run", $2,".",$3,$5,".",$6}' | \
  sed 's/ . /./g'

exit 0
