for file in *.txt ; do
	sort -u $file -o $file
done
