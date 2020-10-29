
# Counts number of characters of the amino acid line
# --> each line that doesnt contain ">"
# Prints number of characters to stdout

for i in $(ls -1)
do 
    cat "$i" | grep -v ">" | wc -c
done
    