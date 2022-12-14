from abc import ABC, abstractmethod
import requests
from bs4 import BeautifulSoup
import re


class Engine(ABC):
    HEADERS = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) '
                      'AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Safari/605.1.15'
    }

    @abstractmethod
    def __init__(self, profession_name: str, name: str, keys_prof: str):
        self.profession_name = profession_name
        self.name = name
        self.keys_prof = keys_prof

    @abstractmethod
    def get_content(self, html):
        pass

    @abstractmethod
    def get_html(self, url: str, headers: dict, params=None):
        pass

    @abstractmethod
    def parser(self, url: str):
        pass


class HH(Engine):
    HOST = 'https://hh.ru'
    URL = 'https://hh.ru/search/vacancy?only_with_salary=true'

    def __init__(self, profession_name, name='HH', keys_prof='text'):
        super().__init__(profession_name, name, keys_prof)

    def get_html(self, url: str, headers: dict, params=None):
        r = requests.get(url, headers=headers, params=params)
        return r

    def get_content(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        items = soup.find_all('div', class_='serp-item')
        vacans = []
        for item in items:
            vacans.append(
                {
                    'title': item.findNext('a', class_='serp-item__title').get_text(),
                    'salary': item.findNext('span', class_='bloko-header-section-3').get_text().replace('\u202f', ''),
                    'job_posting_link': item.findNext('a', class_='serp-item__title').get('href'),
                    'description': item.findNext('div', class_='g-user-content').get_text()

                }
            )

        for i in vacans:
            num = re.findall(r'\d+', i["salary"])
            if len(num) == 0:
                i["salary"] = '0'
            else:
                i["salary"] = max(num)

        return vacans

    def parser(self, url: str):
        html = self.get_html(url=url, headers=self.HEADERS)
        if html.status_code == 200:
            count = []
            print(f'?????????????? ?????????? {self.name}')
            for i in range(1, 40):
                print('?????????????? ??????????????', i)
                html = self.get_html(url=url, headers=self.HEADERS, params={'page': i,
                                                                            self.keys_prof: self.profession_name})
                if len(self.get_content(html.text)) == 0:
                    print(f'???????????? ???????????????? ???? {self.name} ??????')
                    break
                count.extend(self.get_content(html.text))
            return count
        else:
            print('???????????????? ???? ????????????????')


class Superjob(HH):
    URL = 'https://russia.superjob.ru/vacancy/search/?'

    def __init__(self, profession_name, name='Superjob', keys_prof='keywords'):
        super().__init__(profession_name, name, keys_prof)

    def get_content(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        items = soup.find_all('div', class_='_2lp1U _2J-3z _3B5DQ')
        vacans = []
        for item in items:
            vacans.append(
                {
                    'title': item.findNext('span', class_='_9fIP1 _249GZ _1jb_5 QLdOc').get_text(),
                    'salary': item.findNext('span', class_='_2eYAG _1nqY_ _249GZ _1jb_5 _1dIgi').get_text().replace(
                        '\xa0', ''),
                    'job_posting_link': item.findNext('span', class_='_9fIP1 _249GZ _1jb_5 QLdOc').get('href'),
                    'description': item.findNext('span', class_='_1Nj4W _249GZ _1jb_5 _1dIgi _3qTky').get_text()

                }
            )
        for i in vacans:
            num = re.findall(r'\d+', i["salary"])
            if len(num) == 0:
                i["salary"] = '0'
            else:
                i["salary"] = max(num)
        return vacans


class Vacancy:
    def __init__(self, job_title: str, job_link: str, vacancy_description: str, salary_vacancies: int):
        self.salary_vacancies = salary_vacancies
        self.vacancy_description = vacancy_description
        self.job_link = job_link
        self.job_title = job_title

    def __repr__(self):
        return f'???????????????? ????????????????:  {self.job_title} -- ????????????????: {self.salary_vacancies} ??????.\n' \
               f'???????????? ???? ????????????????: {self.job_link}\n' \
               f'???????????????? ????????????????: \n{self.vacancy_description}\n'
