def index():
    with open('temples/index.html') as template:
        return template.read()


def blog():
    with open('temples/blog.html') as template:
        return template.read()
