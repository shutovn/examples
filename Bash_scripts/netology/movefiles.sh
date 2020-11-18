#!/bin/bash

DIR_sourse="/opt/app/bigfiles"
DIR_target="/opt/app/bigfiles/move"
mask="test*"
mv_days="+30"
dell_days="+1825"

array_mv=($(find $DIR_sourse -type f -mtime $mv_days -name "$mask" | sed "s/.*\///"))

for file_name_mv in ${array_mv[@]}
do
mv -b $DIR_sourse/$file_name $DIR_target
ln $DIR_target/$file_name $DIR_sourse/$file_name
done

array_dell=($(find $DIR_target -type f -mtime $dell_days -name "$mask" | sed "s/.*\///"))

for file_name_dell in ${array_dell[@]}
do
rm -f $DIR_target/$file_name
rm -f $DIR_sourse/$file_name
done
