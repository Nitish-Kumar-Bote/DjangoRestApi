from django.http import HttpResponse,JsonResponse
def home_page(request):
    print("home page requested")
    product =['product_id',
        'product_name',
        'price'
    ]
    return JsonResponse(product, safe=False)