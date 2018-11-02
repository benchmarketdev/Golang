### Shadow copy

1. The slice `list[:]` is always an independent copy of the items copied.

2. `dict.copy()` and `set.copy()`, also `copy.copy()`

3. Using type as a function
```
copy_of_dict_d = dict(d)
copy_of_list_L = list(L)
copy_of_set_s = set(s)
```

### Deep copy

```
import copy
x = [1, 2, ['A', 'B', 'C']]
y = copy.deepcopy(x)
```
