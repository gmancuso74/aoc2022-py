from day9 import Dir
from day9 import Day9
from day9 import distance
from day9 import magnitude
from day9 import get_moves

day = Day9()

def test_vector():
    p1 = (0,0)
    p2 = (1,1)
    v1=distance(p1,p2)
    print(f'vec:{v1[0]},{v1[1]}')
    assert magnitude(v1)==1

def test_magnitude2():
    p1 = (0,0)
    p2 = (1,2)
    v1=distance(p1,p2)
    assert magnitude(v1)==2
    v1=distance(p2,p1)
    assert magnitude(v1)==2
    assert v1[1]==2

def test_tupleInSet():
    t1=(0,0)
    t2=(0,0)
    visited=set()
    visited.add(t1)
    visited.add(t2)
    assert len(visited)==1, f'Expected 1 entry in  ''visited'''
    assert visited.issuperset(set([t1])), f'{set([t1])} is not a subset of {visited}'

def test_enumByKeys():
    line='U 9'
    (dir_str,cnt_str)=line.split(' ')
    dir=Dir[dir_str]
    cnt=int(cnt_str)
    assert dir.value==(0,1), f'Direction didn''t parse'
    assert cnt==9, f'Count didn''t parse'


def test_move_left():
    line='L 4'
    for knot in day.p1Rope:
        knot=(0,0)
    moves=get_moves(line)
    day.part1_move(moves)
    assert day.p1Rope[0][0]==-4
    assert day.p1Rope[-1][0]==-3

def test_moves():
    line='R 4'
    day.head=(0,0)
    day.tail=(0,0)
    moves=get_moves(line)
    assert 4==len(moves)
    assert all([x==Dir.R.value for x in moves])
    assert day.head==(0,0)
    assert day.tail==(0,0)
    day.part1_move(moves)
    day.printGrid()
    assert day.head==(4,0), f'head should be (4,0)'
    assert day.tail==(3,0), f'tail should be (3,0)'
    line='L 4'
    moves=get_moves(line)
    assert 4==len(moves)
    assert all([x==Dir.L.value for x in moves])
    day.part1_move(moves)
    assert day.head==(0,0), f'head should be (0,0)'
    assert day.tail==(1,0), f'tail should be (1,0)'

