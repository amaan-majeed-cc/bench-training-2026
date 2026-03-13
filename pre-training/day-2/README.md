
# Day 1 — Control flow & loops exercises

## What would you do differently?
Have to look at what lambda functions do, because they simplify a lot of manual code.

## What's the difference between a list and a dict? When do you use each?
List is like an array, where we can store data of any kind. They can be used for singlar type of data, for example the price of items in which I have recently purchased. The problem with that is that if I have to keep track of what item costs what.. I would have to declare a second list having the names of those grocery items.

```python
grocery_items = ['milk', 'fruits', 'pan']
price_list = [20, 10, 15]
```

whereas if this was a dict, we could simply do this

```python
grocery = [{'item': 'milk'}, {'item': 'fruits'}, {'item': 'pan'}]
```

Now we if for some reason, we want to add another attribute like `weight`, in the case of list, we would have to add another list to keep track of it. whereas in dict we can just add another column in it.


### In short,
Dicts are easier to work with when dealing with complex data structures whereas lists are more suitable for simple collections of data where order matters and we don't need to have values with keys.
