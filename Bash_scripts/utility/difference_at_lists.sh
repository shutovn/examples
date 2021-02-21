#!/usr/bin/env bash

list_one=('zero' 'one' 'two' 'three' 'four' 'five' 'six' 'seven' 'eight' 'nine')
list_two=('zero' 'two' 'four' 'six' 'eight')
list_diff=()

for i in "${list_one[@]}"; do
    skip=
    for j in "${list_two[@]}"; do
        [[ $i == $j ]] && { skip=1; break; }
    done
    [[ -n ${skip} ]] || list_diff+=("${i}")
done

for diff in "${list_diff[@]}"; do
  echo "${diff}"
done
