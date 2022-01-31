import scrapy

class PostsSpider(scrapy.Spider):
    name="posts"

    start_urls=[
        'https://www.house.gov/representatives'
    ]

    def parse(self, response):

        for post in response.css('.table'):
            for traverse in post.css('tbody tr'):
                district_name=post.css('caption::text').get()
                district_number=traverse.css('.views-field.views-field-value-2::text').get()
                district=district_name.strip()+" "+district_number
                name=traverse.css('.views-field.views-field-value-4.views-field-value-5 a::text').get()
                url=traverse.css('.views-field.views-field-value-4.views-field-value-5 a').attrib['href']
                party=traverse.css('.views-field.views-field-value-7::text').get()
                lastname,firstname=name.split(',')
                officeRoom=traverse.css('.views-field.views-field-value-8.views-field-value-9::text').get()
                phone=traverse.css('.views-field.views-field-value-10::text').get()
                committeeAssignment=traverse.css('.views-field.views-field-markup ul li::text').getall()

                yield {

                    'firstname':firstname,
                    'lastname':lastname,
                    'district':district,
                    'party':party,
                    'officeRoom':officeRoom,
                    'phone':phone,
                    'committeeAssignment': committeeAssignment,
                    'url':url,
                    'type':"Federal",
                    'country':"United States of America"

                }




        