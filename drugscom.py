from bs4 import BeautifulSoup
from requests import get


class DrugsCom:
    
    def __init__(self, base_URL):
        # A visitor can only reach up to page 5 before an account is required
        self._max_page = 5
        self._base_url = base_URL
        self._base_page = get(base_URL).content
        self._base_soup = BeautifulSoup(self._base_page, 'html.parser')

    def __iter__(self):
        self._curr_page_num = 1
        self._curr_url = self._base_url
        self._curr_page = get(self._base_url).content
        self._curr_soup = BeautifulSoup(self._curr_page, 'html.parser')
        return self

    def __next__(self):
        if self._curr_page_num <= self._max_page:
            comment_boxes = self._curr_soup('div', class_='ddc-comment')
            comments_data = []
            for comment in comment_boxes:
                #print(comment)
                #comment_soup = BeautifulSoup(comment, 'html.parser')
                comment_soup = comment
                comment_text = comment_soup.find('p').get_text()
                comment_header = comment_soup.find('ul', class_='ddc-comment-header')
                #print(comment_header)
                try:
                    comment_dosage = comment_header.find_all('li')[1].get_text()
                except AttributeError:
                    comment_dosage = None
                comment_score = comment_soup.find('div', class_='ddc-rating-summary')
                try:
                    comment_rating = comment_score.find('b').get_text()
                except AttributeError:
                    comment_rating = None

                comment_footer = comment_soup.find('div', class_='ddc-comment-actions')
                comment_agree = comment_footer.find_all('div')[1]
                
                try:
                    comment_likes = comment_agree.find('a').get_text()
                except AttributeError:
                    comment_likes = None

                comments_data.append((comment_text, comment_dosage, comment_rating, comment_likes))
            
            self._curr_page_num += 1
            self._curr_url = self._base_url + f'/?page={self._curr_page_num}'
            self._curr_page = get(self._curr_url).content
            self._curr_soup = BeautifulSoup(self._curr_page, 'html.parser')

            return comments_data

        else:
            raise StopIteration

