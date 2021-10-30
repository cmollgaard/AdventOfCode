function AOC(){
for day in `seq 1 25`; 
    mkdir -p $1/$day && 
    {
    echo "data = open('input1.txt','r').read().split('\\n')"
    echo '' echo "data = data[0]" 
    echo "print(data)" } >$1/$day/part1.py && 
    { 
    echo "data = open('input2.txt', 'r').read().split('\\n')" 
    echo '' 
    echo "data = data[0]" 
    echo "print(data)" 
    } >$1/$day/part2.py && 
    touch $1/$day/input1.txt &&
    touch $1/$day/input2.txt 
}
