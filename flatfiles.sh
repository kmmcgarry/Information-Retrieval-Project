for top in /Users/kristen/Desktop/clinicaltrials_xml/*
do
  for dir in $top/*
  do
    for file in $dir/*
    do
      mv $file $top
    done
  done
done
