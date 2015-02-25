## I have no idea how to start solving this mission

If you see a function definition like `def function(*args):`,
then this function can work with an arbitrary number of arguments.
You can work with "args" as with a tuple.

```python
def func(*args):
    for x in args:
        print(x)

func(1, 2, 3)
func(2)
func()
```

## I need some help to proceed with the mission

You can easily find the minimum and maximum with the built-in functions "min" and "max".

```python
max([1, 2, 3, 100]) == 100
min([1, 2, 3, 100]) == 1
min((0.1, 1)) == 0.1
```

## I am gone half way through. Need help!

Don't forget about the empty arguments list. Check it before the min-max.

```python
if args:
    something
else:
    return 0
```
