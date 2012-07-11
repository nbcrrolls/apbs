#!/bin/bash

apbs=/opt/apbs/bin/apbs
mpirun=/opt/openmpi/bin/mpirun

if test -z "$apbs" ; then
  echo "ERROR: apbs is missingd"
  exit 1
fi

if test -z "$mpirun" ; then
  echo "ERROR: mpirun is missingd"
  exit 1
fi

while [ "$1" != "" ]; do
    case $1 in
        -molecule)               
             shift
             molecule=$1
             ;;
        -input)               
             shift
             input=$1
             ;;
        -outfile)
             shift
             outfile=$1
             ;;
        -procs)
             shift
             procs=$1
             ;;
        *)   echo "Invalid argument in $@"
             exit 1
    esac
    shift
done

if test -z "$procs"; then
  echo "WARNING: Number of processors was not specified with the -procs option, defaults to 1"
  procs=1
fi

if test -z "$molecule"; then
  echo "ERROR: missing molecule input file"
  exit 1
fi
if test -z "$input"; then
  echo "ERROR: missing configuration input file"
  exit 1
fi

if test ! -z "$outfile"; then
  outputfile="--output-file=$outfile"
fi


sub="apbs.sub"

if test "$procs" = 1; then
  cmd="$apbs $outputfile $input >& $input.out"
  type="serial"
  echo Executing command: $cmd
  $cmd
else
  cmd="$mpirun -v -np \$NSLOTS $apbs $outputfile $input >& input.out"
  type="parallel"
fi

echo "#$ -S /bin/bash" >> $sub
echo "#$ -cwd" >> $sub
echo "#$ -e apbs.err" >> $sub
echo "#$ -o apbs.out" >> $sub
echo "#$ -V" >> $sub
echo "#$ -pe orte $procs" >> $sub
echo "#$ -N apbs-$type" >> $sub
echo "" >> $sub
echo "$cmd" >> $sub

qsub -sync y $sub

