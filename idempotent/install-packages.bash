#!/bin/bash -e

cd "$(cd -P -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd -P)"
PACKAGEFILE="$1"

if [ -z "$1" ] ; then
  echo "Argument missing. Please provide the filename containing the list of packages." >&1
  exit 1
fi

if [ ! -f $PACKAGEFILE ] ; then
  echo "Can not read \"$PACKAGEFILE\". Check it is present and accessible." >&1
  exit 1
fi


TMPFILE=$(mktemp)
trap "rm -rf $TMPFILE" EXIT

cut -d\# -f1 $PACKAGEFILE |grep -v '^$' >$TMPFILE
sudo xargs -a $TMPFILE dnf install -y

