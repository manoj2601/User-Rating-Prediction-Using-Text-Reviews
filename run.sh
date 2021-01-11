question=$1
trainpath=$2
testpath=$3
output=$4
if [[ $1 == "1" ]];
then
	python q1e2.py $2 $3 > $4
fi