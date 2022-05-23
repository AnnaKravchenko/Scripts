rec=$1
lig=$2

tdir="$(mktemp -d /tmp/XXXXXXXXX)" || exit 1 # make a random dir in /tmp/ and save path to it 

nlig=`cat $lig|wc -l`
nrec=`cat $rec|wc -l`

for i in `seq $nlig`; do
	awk -v i=$i 'NR==i' $lig > $tdir/ligbead$i.pdb
done

for i in `seq $nrec`; do
	awk -v i=$i 'NR==i' $rec > $tdir/recbead$i.pdb
done

	
for i in `seq $nrec`; do
	for j in `seq $nlig`; do
		$ATTRACTDIR/attract $ATTRACTDIR/../structure-single.dat $ATTRACTDIR/../attract.par $tdir/recbead$i.pdb $tdir/ligbead$j.pdb |awk -v i=$i -v j=$j '$2=="Energy:"{ if($3!=0.000) print i, j, $3}'
	done
done

rm -r $tdir
