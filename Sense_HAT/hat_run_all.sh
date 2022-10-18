for fn in `ls hat*.py`; do
	echo "the next file is $fn"
	python $fn
done