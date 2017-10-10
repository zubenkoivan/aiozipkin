import asyncio
import aiozipkin

from aiohttp import web


async def handler(request):
    await asyncio.sleep(0.01)
    body = "servcie_c"
    return web.Response(text=body)


def make_app():
    app = web.Application()
    app.router.add_get('/api/v1/data', handler)

    zipkin_address = "http://localhost:9411/api/v2/spans"
    endpoint = aiozipkin.create_endpoint("service_c")
    tracer = aiozipkin.create(zipkin_address, endpoint)
    aiozipkin.setup(app, tracer)
    return app


if __name__ == "__main__":
    host = "127.0.0.1"
    port = 9003
    app = make_app()
    web.run_app(app, host=host, port=port)