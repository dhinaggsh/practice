import asyncio
from django.http import HttpResponse


async def fun(request):
    print("Hello")
    await asyncio.sleep(2)
    print("world")
    return HttpResponse("Done")