# naive-bayes-python

> this code are not clean a.k.a smelly code
>
> do not expect too much from me
>
> I tried to add comments for more readable

### how to run

Windows OS

```
git clone https://github.com/andikasujanadi/naive-bayes-python.git
```

```
cd naive-bayes-python
```

```
python app.py
```

Unix-Like OS

```
git clone https://github.com/andikasujanadi/naive-bayes-python.git
```

```
cd naive-bayes-python
```

```
python3 app.py
```

### change CSV data

My default CSV is to determine type of fish based on length, width, and weight

length|width|weight|fish
----|-----|------|----
long|small|light|catfish
long|medium|heavy|catfish
long|wide|heavy|gourami
long|small|heavy|catfish
long|medium|light|catfish
long|wide|heavy|gourami
short|small|light|gourami
short|medium|light|gourami
short|wide|heavy|gourami

You can change all of the data inside CSV as long as:
* the top column are for label
* the last row are for prediction result

### Program Preview

```
Naïve Bayes Algoritm
Author: Andika Sujanadi

determine fish

PLEASE INPUT THE INDEX EACH CATEGORY

length [long(0), short(1)] = 0

width [small(0), medium(1), wide(2)] = 2

weight [light(0), heavy(1)] = 1


fact:

P(fish=catfish) = 4/9
P(fish=gourami) = 5/9

fact:

P(length = long | fish = catfish) = 4/4
P(width = wide | fish = catfish) = 0/4
P(weight = heavy | fish = catfish) = 2/4

P(length = long | fish = gourami) = 2/5
P(width = wide | fish = gourami) = 3/5
P(weight = heavy | fish = gourami) = 3/5

HMAP: 

P(length = long, width = wide, weight = heavy | fish = catfish) = 0.0
P(length = long, width = wide, weight = heavy | fish = gourami) = 0.08

fish = gourami
```
