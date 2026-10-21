from locust import HttpUser, task, tag, events, constant, between


class TestClass(HttpUser):

    wait_time = constant(2)     # for between: wait_time = between (5,15)

    host = 'https://petstore.swagger.io/'

    @events.test_start.add_listener
    @task
    def on_starting(environment, **kwargs):
        print('environment setup done. This code runs before all test scripts')

    @events.test_stop.add_listener
    @task
    def on_ending(environment, **kwargs):
        print('this runs once the entire script has executed')


    @task
    @tag('first')
    def first_script(self):
        self.client.get('v2/store/inventory')


    @task
    @tag('post')
    def post_script(self):
        request_body = {
            {
        "id": 0,
        "category": {
            "id": 0,
            "name": "Updated value 1"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
            "id": 0,
            "name": "string"
            }
        ],
        "status": "available"
        }
        }

        with self.client.post('/v2/pet', json=request_body) as response:
            if response.status_code !=200:
                response.success('test passed')
                return

            else: 
                response.failure('test failed')
                return
            