#! /bin/sh
for num in {2..100..1}
  do
  p=0
  i=2
    while [ $i -lt $num ]
      do
        if [ `expr $num % $i` -eq 0 ]
        then
          p=1
          break
        fi
      i=`expr $i + 1` 
    done
    if [ `expr $p` = 0 ]
      then
        echo $num
      fi
  done