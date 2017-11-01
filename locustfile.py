from locust import HttpLocust, TaskSet
import resource
resource.setrlimit(resource.RLIMIT_NOFILE, (999999, 999999))
# def login(l):
#     l.client.post("/login", {"username":"ellen_key", "password":"education"})

def all_articles(l):
    l.client.get("/articles/?format=json")


def get_user_articles(l):
    l.client.get("/user/1/articles?format=json")

class UserBehavior(TaskSet):
    tasks = {all_articles: 2, get_user_articles: 2}

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 9000
