import requests

from bs4 import BeautifulSoup


class ServiceLink:
    @staticmethod
    def parse_link(url: str) -> dict:
        from links.models import LinkTypeEnum

        data = {
            'title': '',
            'description': '',
            'preview_image': '',
            'link_type': LinkTypeEnum.WEBSITE.value
        }

        try:
            response = requests.get(url)
            response.raise_for_status()
            soup = BeautifulSoup(response.content, 'html.parser')

            og_title = soup.find('meta', property='og:title')
            og_description = soup.find('meta', property='og:description')
            og_image = soup.find('meta', property='og:image')
            og_type = soup.find('meta', property='og:type')

            data['title'] = og_title['content'] if og_title else soup.title.string if soup.title else ''
            data['description'] = og_description['content'] if og_description else soup.find('meta', attrs={'name': 'description'}).get('content', '') if soup.find('meta', attrs={'name': 'description'}) else ''
            data['preview_image'] = og_image['content'] if og_image else ''
            data['link_type'] = og_type['content'] if og_type else data['link_type']

        except requests.RequestException as error:
            raise ValueError(f"Error fetching URL: {error}") from error

        return data
