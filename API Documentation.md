# Xmeme API Documentation


## `GET /memes`
This api endpoint is used to fetch top 100 memes, with the new ones posted first. It accepts HTTP GET request and returns the data from the database.


## `POST /memes`
This api endpoint is used to submit data to the database. It accepts HTTP POST request with required headers and the payload to be uploaded and then returns the id of the uploaded meme. It also have required error handling mechanism and proper status codes on error situations. 

## `GET /memes/<id>`
This api endpoint is used to fetch the meme with the given `id` and returns all the information of that meme i.e name, caption and url.

## `PATCH /memes/<id>`
This api endpoint is used to partially update the resource at database without creating a new entry. It accepts HTTP PATCH request with required headers and payload and is only abled to change the caption and url of the post. It cant change name of the post and also have the required error handling mechanisms.

## `GET /tags/<tagName>`
This api endpoint is used to get all the posts which are having same tags in their caption. It basically is working on model which stores the foreign key of posts with tags and those posts which have same tags can be fetched by this endpoint.

## `GET /count/`
This api endpoint is used to get the number of posts available at any moment in the database. It helps to assess the database for its size, i.e how much data is present in the database as well as helps in calculating the response time metrics of the database. 