cd juliana/

for dir in */
do
    dir=${dir%*/}
    # echo ${dir##*/}
    for file in $dir/*
    do
	    if [[ ${file:0:4} -eq "2017" ]]
	    then
	    # echo sub is 2018 directory ${file}
	        # echo $file
	        tar -zxvf $file
	    fi
    done
done