import csv
import sys
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError


def get_status_code(url: str, timeout: int = 10) -> str:
    """Return the HTTP status code for a URL, or ERROR if no response is received."""
    try:
        request = Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urlopen(request, timeout=timeout) as response:
            return str(response.getcode())
    except HTTPError as error:
        return str(error.code)
    except URLError:
        return "ERROR"
    except Exception:
        return "ERROR"


def read_urls_from_csv(csv_path: str) -> list[str]:
    """Read the list of URLs from the CSV file."""
    urls = []

    with open(csv_path, "r", encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            url = (row.get("urls") or "").strip()
            if url:
                urls.append(url)

    return urls


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python3 task2_status_codes.py <csv_file>")
        sys.exit(1)

    csv_path = sys.argv[1]
    urls = read_urls_from_csv(csv_path)

    for url in urls:
        status_code = get_status_code(url)
        print(f"({status_code}) {url}")


if __name__ == "__main__":
    main()
