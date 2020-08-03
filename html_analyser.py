from bs4 import BeautifulSoup


class HtmlAnalyser:
    def get_actress_list_from_response(self, response):
        """
        analyze response(HTML) and return actress's name, actress's img of path
        """
        ret_list = []
        soup = BeautifulSoup(response.text, "html.parser")
        elms =  soup.find_all('div', class_='thumbnailBox')

        for elm in elms:
            if elm.text:
                a_tag = elm.find('a', recursive=False)
                actress_name = a_tag['title']
                img_tag = a_tag.find('img')
                actress_img_path = ''
                if img_tag.has_attr('src'):
                    actress_img_path = img_tag.get('src')
                elif img_tag.has_attr('data-original'):
                    actress_img_path = a_tag.find('img').get('data-original')
                else:
                    continue
                ret_list.append({'name': actress_name,
                                'img_url': actress_img_path})

        return ret_list
