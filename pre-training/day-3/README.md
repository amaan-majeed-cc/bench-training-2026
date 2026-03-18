## Day-3: OOP task tracker with JSON persistence

## Why I used a class here instead of just functions
Classes were used instead of functions to make it easier to manage the task and data storage in json format. It also makes it easier to add new features to the task tracker in the future.

## Usage Examples
```bash
python tasks.py add 'Fix login bug'
python tasks.py done 3
python tasks.py list
python tasks.py list --filter done
```


```bash
> python3 tasks.py add 'Fix login bug'
3
> python3 tasks.py done 3
3
> python3 tasks.py list
3	Fix login bug	done	2026-03-18 22:30:08
> python3 tasks.py list --filter done
3	Fix login bug	done	2026-03-18 22:30:08
> python3 tasks.py delete 3
> python3 tasks.py list --filter done
> python3 tasks.py list
> python3 tasks.py add 'ABC'
4
> python3 tasks.py list
4	ABC	todo	2026-03-18 22:30:45
> python3 tasks.py add 'KFC'

```