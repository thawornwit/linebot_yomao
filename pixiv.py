import random
import time
from pixivpy3 import *

pixiv_username = ''
pixiv_password = ''

class pixiv_crewler():
	def __init__(self):
		self.api = PixivAPI()
		self.api.login(pixiv_username, pixiv_password)
		
	def get_image(self, keyword_list, sample = 500, advance_sample = 10):
		query = ' '.join(keyword_list)
		total_count = self.__get_total_count(query)
		start_index = random.randint(1, total_count // sample + 1)
		tStart = time.time()
		print('start query')
		result = self.api.search_works(query, page = start_index, per_page = sample).response
		print('end query: ' + str(time.time() - tStart))
		sorted_result = sorted(result, reverse = True,\
			key = lambda _: _.stats.favorited_count.public + _.stats.favorited_count.private)
		result = sorted_result[random.randint(0, advance_sample)]
		return result.image_urls.px_480mw, result.image_urls.large

	def __get_total_count(self, query):
		return self.api.search_works(query, page = 1, per_page = 1).pagination.total
