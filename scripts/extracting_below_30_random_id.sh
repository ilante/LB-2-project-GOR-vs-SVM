#printing relevant lines to new file
awk -F ' ' '$3 < 30 {print $0}' hits.blast.tab > lines_below_30_hits
#printing all lines < 30 to new .hits file
awk -F ' ' '{print $1}' lines_below_30_hits > ids_below_30
#sorting random and saving to new file
cat ids_below_30 | sort -R > all_random.blindset

