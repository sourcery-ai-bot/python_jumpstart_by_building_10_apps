import requests
import bs4
import collections


def print_header():
    print("--------------------------------")
    print("           WEATHER APP")
    print("--------------------------------")
    print()


def get_html_from_web(zipcode):
    url = f"http://www.wunderground.com/weather-forecast/{zipcode}"
    print(url)
    response = requests.get(url)
    return response


def get_weather_from_html(html):
    soup = bs4.BeautifulSoup(html.text, "html.parser")
    # cityCss = '.region-content-header h1'
    # weatherScaleCss = '.wu-unit-temperature .wu-label'
    # weatherTempCss = '.wu-unit-temperature .wu-value'
    # weatherConditionCss = '.condition-icon'

    # loc = soup.find(class_="subheading").get_text()
    condition = soup.find(class_="condition-icon").get_text()
    temp = soup.find(class_="wu-unit-temperature").find(class_="wu-value").get_text()
    scale = soup.find(class_="wu-unit-temperature").find(class_="wu-label").get_text()

    # loc = cleanup_text(loc)
    # loc = find_city_and_state_from_location(loc)
    condition = cleanup_text(condition)
    temp = cleanup_text(temp)
    scale = cleanup_text(scale)

    # return condition, temp, scale

    report = WeatherReport(cond=condition, temp=temp, scale=scale)
    return report


def cleanup_text(text: str):  # type hinting
    if not text:  # error checking usint truthy values
        return text

    text = text.strip()
    return text


def find_city_and_state_from_location(loc):
    parts = loc.split("\n")
    return parts[0].strip()


WeatherReport = collections.namedtuple("WeatherReport", "cond, temp, scale")


def main():
    print_header()
    code = input("What zipcode do you want the weather for (97201)? ").strip()
    html = get_html_from_web(code)
    report = get_weather_from_html(html)
    print(f"The temp in this location is {report.temp} with {report.cond} conditions.")


if __name__ == "__main__":
    main()

