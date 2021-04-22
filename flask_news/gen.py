import names 
import string
import random
import lorem
from datetime import date, timedelta


class StudentGen:
    def __init__(self, count = 3):
        self.students_gen(count)

   
    def students_gen(self, count=50):
        self.students = []
        for x in range(count):
            name = names.get_full_name().split()
            news_head = self.news_head()
            news_content = self.news_content()
            category = self.category()
            date = str(self.date())
            slug = self.slug()

            self.students.append({
                    "fname": name[0],
                    "sname":name[1],
                    "news_head": news_head,
                    "news_content": news_content,
                    "category": category,
                    "date": date,
                    "slug": slug
                })

    def news_head(self):
        return lorem.sentence()

 

    def slug(self):
        result = "".join(random.choices(string.ascii_letters, k = 5))
        return result


    def category(self):
        categories = ["Sports","Politics", "Science","Health","Entertainment"]
        return random.choice(categories)

    def date(self):
        start_date = date(2020, 1, 1)
        end_date = date(2021, 4, 20)

        time_between_dates = end_date - start_date
        days_between_dates = time_between_dates.days
        random_number_of_days = random.randrange(days_between_dates)
        random_date = start_date + timedelta(days=random_number_of_days)

        return random_date


    def news_content(self):
        return lorem.text()

   
