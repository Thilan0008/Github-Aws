from flask import Flask
import os
import csv
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def run_scraper():
    import_csv_data()
    return 'CSV file has been generated and saved.'

def import_csv_data():
    # Read previously excluded courses from the CSV file
    excluded_courses = {}
    csv_file_path = os.path.join(app.root_path,'top_courses.csv')
    if os.path.exists(csv_file_path):
        with open(csv_file_path, 'r', encoding='utf-8-sig') as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader)  # Skip header row
            for row in csv_reader:
                title = row[0]
                excluded_courses[title] = tuple(row)

    # Combine previously excluded courses with top courses
    courses = scrape_coursera()
    updated_courses = {**courses, **excluded_courses}.values()

    # Sort the updated courses by enrollment count and rating count in descending order
    updated_courses = sorted(updated_courses, key=lambda x: (int(x[2]), float(x[1])) if x[1] else (int(x[2]), 0), reverse=True)

    # Truncate the list to include only the top 50 courses
    updated_courses = updated_courses[:50]

    # Write the updated courses to the CSV file
    os.makedirs(os.path.dirname(csv_file_path), exist_ok=True)
    with open(csv_file_path, 'w', newline='', encoding='utf-8-sig') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(['Title', 'Rating Value', 'Enrollment Count', 'Main Category', 'Link'])
        for course in updated_courses:
            csv_writer.writerow(course)

def scrape_coursera():
    def get_soup(site):
        source = requests.get(site).text
        return BeautifulSoup(source, 'lxml')

    def get_title(soup):
        try:
            return soup.find('h1').text.strip()
        except:
            return None

    def get_rating_val(soup):
        try:
            rating_val = soup.find('div', class_='cds-119 css-h1jogs cds-121').text.strip()
            return float(rating_val)
        except:
            return None

    def get_enroll_count(soup):
        try:
            enroll_count = soup.find('p', class_='cds-119 css-80vnnb cds-121').find('span').find('span').text.strip()
            return int(enroll_count.replace(',', ''))
        except:
            return None

    #def get_main_category(soup):
        #try:
            #return soup.find_all('div', class_='_1ruggxy')[1].a.text.strip()
        #except:
            #return None

    source = requests.get('https://www.coursera.org/sitemap~www~courses.xml').text
    soup = BeautifulSoup(source, 'xml')  # Use XML parser

    courses = {}

    for site in soup.find_all('loc'):
        site_soup = get_soup(site.text)
        title = get_title(site_soup)
        rating_val = get_rating_val(site_soup)
        enroll_count = get_enroll_count(site_soup)
        #main_category = get_main_category(site_soup)
        course_link = site.text  # Extract the course link from the XML file

        # Exclude courses with empty titles and null or zero values
        if title and rating_val and enroll_count: #main_category
            # Store the course in the dictionary using the title as the key,
            # including the course link in the tuple
            courses[title] = (title, rating_val, enroll_count, course_link)

        # Break the loop if 50 courses are scraped
        if len(courses) >= 50:
            break

    return courses

if __name__ == '__main__':
    app.run()
