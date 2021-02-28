#!/usr/bin/env bash

log_dir="/tmp/test_log"
log_file="${log_dir}/logfile.log"

mkdir -p $log_dir
touch $log_file

for ((i=1; i < $1; i++))
do
ts=$(date  +%d.%m.%Y\ %H:%M:%S\ %N)
h=$(hostname)
sha=$(echo -n "${i}" | md5sum -)
msg=$(head -c 50 /dev/urandom | base64 | sed 's/[+=/A-Z]//g' | tail -c50)

echo "${i} ${ts} ${h} ${sha} ${msg}" >> $log_file
done
