import requests
from bs4 import BeautifulSoup as bs

def main():
	url = "https://www.canadacomputers.com/on-sale.html"
	page = requests.get(url)

	soup = bs(page.text, "html.parser")
	product_name_list = soup.find_all(class_='text-dark text-truncate_3')
	original_price_list = soup.find_all(class_='d-sm-block line-height')
	discount_price_list = soup.find_all(class_='text-danger d-block mb-0 pq-hdr-product_price line-height')
	
	worthit_dict = {}
	for i in range(len(product_name_list)):
		if (float(original_price_list[i].text.strip('$')) - float(discount_price_list[i].text.strip('$')) > 50):
			worthit_dict[product_name_list[i].text] = [
				float(original_price_list[i].text.strip('$')), 
				float(discount_price_list[i].text.strip('$')), 
				round(float(original_price_list[i].text.strip('$')) - float(discount_price_list[i].text.strip('$')),2)
			]

	for key, value in sorted(worthit_dict.items()):
		print(key, value)

main()