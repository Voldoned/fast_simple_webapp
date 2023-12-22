def request_locust(obj_locust,
                   url: str,
                   method: str,
                   *args, **kwargs):
    if method is "GET":
        with obj_locust.client.get(
            url,
            *args,
            **kwargs
        ) as response_get:
            try:
                return response_get
            except Exception as ex:
                response_get.failure(ex)

    elif method is "POST":
        with obj_locust.client.post(
            url,
            *args,
            **kwargs
        ) as response_post:
            try:
                return response_post
            except Exception as ex:
                response_post.failure(ex)

    elif method is "PUT":
        with obj_locust.client.put(
            url,
            *args,
            **kwargs
        ) as response_put:
            try:
                return response_put
            except Exception as ex:
                response_put.failure(ex)
