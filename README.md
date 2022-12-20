*fomular_recognition*

classify by size differences
ex) very small: upper, lower/ middle size: denumerator, numerator/ big size: normal word

is typical CNN can classify size difference easily?
- maybe not

is one CNN same as combined small CNN?
- figure it out

# 1. Dividing 4X4 fitures

# 2. Apply same CNN for each
-> 4x4 same depth fiture maps

# 3. Combine the fiture maps
## by
### 1. CNN (idk)
### 2. RNN (Long short term memory)
use RNN for vertical and horizontal (two RNNs)
-> get several output vectors and 4x2 hidden vectors
hidden vectors may contain information of broken parts



# 4. Fully conected layer to classify
are output veectors usefull?

it can be expanded to same row but different columns
by slicing 4xn
