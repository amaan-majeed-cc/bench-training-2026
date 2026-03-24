## Day-7

### Country Info API Wrapper

This mini project compares two countries using live APIs and prints side-by-side stats for population, region, area, GDP, languages, and currencies.

### How to run

1. Install dependency:
   `pip install requests`
2. From this folder, run:
   `python3 countries.py compare <Country1> <Country2>`

Example:
`python3 countries.py compare Pakistan India`

### Example output

```text
Comparing Pakistan and India...

Metric               | Pakistan                                           | India
------------------------------------------------------------------------------------------------------------------------------
Population           | 241499431                                          | 1417492000
Region               | Asia                                               | Asia
Area                 | 796095.0                                           | 3287263.0
GDP per Capita       | $371.57 Billion                                    | $3.91 Trillion
Languages            | English, Urdu                                      | English, Hindi, Tamil
Currencies           | {'symbol': '₨', 'name': 'Pakistani rupee'}         | {'symbol': '₹', 'name': 'Indian rupee'}
------------------------------------------------------------------------------------------------------------------------------
```

### Edge cases (multi-word country names)

If a country name has spaces, enter it with `-` between words.
The script converts `-` back to spaces internally.

Examples:

- `python3 countries.py compare north-korea south-korea`
- `python3 countries.py compare united-states-of-america costa-rica`
- `python3 countries.py compare papua-new-guinea czech-republic`

