# B. Ilya and Queries

Ilya the Lion wants to help all his friends with passing exams. They need to solve the following problem to pass the IT exam.

You've got string  _s_ = _s_1_s_2...  _s__n_  (_n_  is the length of the string), consisting only of characters "." and "#" and  _m_  queries. Each query is described by a pair of integers  _l__i_, _r__i_  (1 ≤ _l__i_ < _r__i_ ≤ _n_). The answer to the query  _l__i_, _r__i_  is the number of such integers  _i_  (_l__i_ ≤ _i_ < _r__i_), that  _s__i_ = _s__i_ + 1.

Ilya the Lion wants to help his friends but is there anyone to help him? Help Ilya, solve the problem.

## Input

The first line contains string  _s_  of length  _n_  (2 ≤ _n_ ≤ 105). It is guaranteed that the given string only consists of characters "." and "#".

The next line contains integer  _m_  (1 ≤ _m_ ≤ 105)  — the number of queries. Each of the next  _m_  lines contains the description of the corresponding query. The  _i_-th line contains integers  _l__i_, _r__i_  (1 ≤ _l__i_ < _r__i_ ≤ _n_).

## Output

Print  _m_  integers — the answers to the queries in the order in which they are given in the input.

## Examples

### Input

    ......  
    4  
    3 4  
    2 3  
    1 6  
    2 6
### Output

    1
    1
    5
    4
### Input

    #..###
    5
    1 3
    5 6
    1 5
    3 6
    3 4
### Output

    1
    1
    2
    2
    0
    