## Day-4: GitHub account parser

<!-- day-4: github fetcher + weather CLI
README.md: Paste an example output from each script. What was the hardest part of
reading the API response? -->

## GitHub Account Parser
### Usage Examples
```bash
> python github_account_parser.py 'amaanmajeed'

Username: amaanmajeed
Bio: Vue.js Dev & Rails Enthusiast 💻 | Exploring the world of Solution Architecture 📐
Public repos: 21
Followers: 44
---------------------------
GDSC-Event-Add-Participants - 5 - Python
Post_on_socials_Automation - 4 - Python
QuickStock - 2 - JavaScript
Chrome-Extension-for-University-Portal-Login - 1 - JavaScript
Smart-Home-Automation - 1 - C++
---------------------------
```

### Weather CLI
### Usage Examples
```bash
> python3 weather-cli.py lahore
City: Lahore
Temperature: 16.8°C (62.24°F)
Wind Speed: 3.7 km/h
Weather Description: Rain showers: Slight
> python3 weather-cli.py karach
City: Karachi
Temperature: 22.8°C (73.03999999999999°F)
Wind Speed: 14.2 km/h
Weather Description: Overcast
> python3 weather-cli.py dsadaddds
Error: Please provide a valid city name

```


## Hardest part of reading the API response
There wasn't anything very hard, just needed to check the kind of data we were getting back from the API, and map that accordingly.
