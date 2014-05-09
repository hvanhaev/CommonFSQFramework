#! /bin/bash


if [ $# -ne 2 ]
then
  echo "Usage: `basename $0` filter command"
  exit 1
fi


command=$2
filter=$1



log=cblog_$filter.txt
rm -rf $log

for m in `ls  |grep $filter `; do
  crab -$command -c $m #| tee -a $log
done

# bell

echo Logfile: $log
echo $'\a'

