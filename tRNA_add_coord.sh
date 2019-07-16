#Using this to append genomic co-ordinates to the tRNA tsv files
#Need to run in directory that contains .tsv files used for svg

mkdir tsv_appended

ls *.tsv | while read line
do
	gene=$(echo "$line" | sed -e 's/.tsv//g')
	start=$(cat tRNA_genes.txt | grep -i "$gene" | awk '{
		if ($4=="+") #-i so case insentive match
		{print $1}
		else
		{print $2}}') #if not + then must be -, and use end since gene in reverse
	echo $gene
	echo $start
	rm tsv_appended/${gene}_appended.tsv
	#using tr to get rid of the carriage return in the files....and grep to get rid of resulting empty lines
	cat $line | tr '\r' '\n' | grep -v '^$' | awk -v s=${start} '{
		if ($1 == "b")
		{print $0,s; s=s+1} #this increments +1 per line
		else
		{print $0}
	}' OFS='\t' > tsv_appended/${gene}_appended.tsv
done


