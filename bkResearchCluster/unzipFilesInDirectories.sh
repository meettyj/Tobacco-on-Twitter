cd juliana/

for dir in */
do
    dir=${dir%*/}
    # echo ${dir##*/}
    for file in $dir/*
	do
		# echo $file
	    tar -zxvf $file
	done
done