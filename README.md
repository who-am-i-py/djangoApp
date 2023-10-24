# Django application

- The django framework is not add to github
- I have to learn more about Model manager

# The request / response cycle:

1. A web browser requests a page by its URL.

   - for example : [`code` https://domain.com/blog/33 `code` ]
   - The web server recieves the HTTP request and passess it over to Django

2. Django runs through each URL pattern defined in the URL patterns configuration.

   - The frame-work work checks each pattern against the given URL path.
   - In order of appearence, and stops at the first one that matches the requested URL
   - In this case the pattern /blog/<id> [for example id=33] the patterns matches the path /blog/33/

3. Django imports the view of the matching URL pattern and executes it, passing an instance of the HttpRequest class and the keyword or positional arguments. The view uses the models to retieve information from the database. Using the Django ORM QuerySets are translted into SQL and executed in the database.

4. The view uses the render() function to render and HTML template passing the Post object as a context variable.

5. The rendered content is returned as a HttpResponse object by the view the text/html content type by default.

# Summary for Chapter:1

In this chapter, you learned the basics of the Django web framework by creating a simple blog application.
You designed the data models and applied migrations to the database. You also created the
views, templates, and URLs for your blog.
In the next chapter, you will learn how to create canonical URLs for models and how to build SEO-friendly
URLs for blog posts. You will also learn how to implement object pagination and how to build classbased
views. You will also implement
