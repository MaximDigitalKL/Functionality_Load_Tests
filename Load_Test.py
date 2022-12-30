import time
import unittest
from locust import HttpUser, task, between


class Load_DEV(HttpUser):
    wait_time = between(1, 2)


    @task
    def Load_Test_Home_Page(self):
        self.client.get(url="")

    @task
    def Load_Test_JOB_OPORTUNITIES(self):
        self.client.get(url="/careers-at-kerv/job-opportunities/")

    @task
    def Load_Test_DEV_Form(self):
        self.client.get(url="/job-details/mp0syiy/")
