# Option C — Country Info API Wrapper
# Wrap the REST Countries API (https://restcountries.com) into a clean Python module.
# Functions: get_country(name), get_region(region_name), compare_countries(c1, c2).
# Compare shows: population, area, GDP per capita (if available), languages, currencies sideby-side.
# CLI: python countries.py compare Pakistan India

import requests

def get_country(name):
  try:
    response = requests.get(f"https://restcountries.com/v3.1/name/{name}?fullText=true", timeout=5)
    response.raise_for_status()
    return response.json()
  except requests.RequestException:
    return

def get_region(region_name):
  try:
    response = requests.get(f"https://restcountries.com/v3.1/region/{region_name}", timeout=5)
    response.raise_for_status()
    return response.json()
  except requests.RequestException:
    return

def format_currency(value):
  if not value or not isinstance(value, (int, float)):
    return "N/A"
  if value >= 1e12:
    return f"${value / 1e12:.2f} Trillion"
  if value >= 1e9:
    return f"${value / 1e9:.2f} Billion"
  if value >= 1e6:
    return f"${value / 1e6:.2f} Million"
  return f"${value:,.0f}"

def get_gdp(country_code):
  try:
    url = f"https://api.worldbank.org/v2/country/{country_code}/indicator/NY.GDP.MKTP.CD?format=json&mrnev=1"
    response = requests.get(url, timeout=5)
    data = response.json()
    if isinstance(data, list) and len(data) > 1 and data[1]:
      val = data[1][0].get("value")
      return format_currency(val)
  except Exception:
      pass
  return "N/A"

def compare_countries(c1, c2):
  print(f"Comparing {c1} and {c2}...")
  country1 = get_country(c1.replace("-", " "))
  country2 = get_country(c2.replace("-", " "))

  if not country1 or not country2:
    print("One or both countries not found.")
    return

  data = {
    "Population": (country1[-1]["population"], country2[-1]["population"]),
    "Region": (country1[-1]["region"], country2[-1]["region"]),
    "Area": (country1[-1]["area"], country2[-1]["area"]),
    "GDP per Capita": (country1[-1].get("gdp", 0) or get_gdp(country1[-1]["cca3"]), country2[-1].get("gdp", 0) or get_gdp(country2[-1]["cca3"])),
    "Languages": (list(country1[-1]["languages"].values()), list(country2[-1]["languages"].values())),
    "Currencies": (list(country1[-1]["currencies"].values()), list(country2[-1]["currencies"].values())),
  }
  return data

if __name__ == "__main__":
  import sys
  if len(sys.argv) != 4 or sys.argv[1] != "compare":
    print("Usage: python countries.py compare <Country1> <Country2>")
    sys.exit(1)

  c1, c2 = sys.argv[2], sys.argv[3]
  comparison = compare_countries(c1, c2)

  if comparison:
    header = f"{'Metric':<20} | {c1.replace('-', ' ').title():<50} | {c2.replace('-', ' ').title():<50}"
    print("\n" + header)
    print("-" * len(header))

    for key, value in comparison.items():
      v1 = ", ".join(map(str, value[0])) if isinstance(value[0], list) else str(value[0])
      v2 = ", ".join(map(str, value[1])) if isinstance(value[1], list) else str(value[1])

      print(f"{key:<20} | {v1:<50} | {v2:<50}")
    print("-" * len(header) + "\n")