from .models import (
    mprod_exp180, mprod_proflevel
)


def fetch_product_list(product):
    if product == 'exp180':
        p = mprod_exp180.objects.order_by('id')[:3]
        return p
    else:
        return None



from .models import mprod_exp180


def fetchExp180Randomly():
    rand_prod_4 = mprod_exp180.objects.order_by('id')[:4]
    prd_titles = [x.title for x in rand_prod_4]

    return rand_prod_4              # prd_titles


import json
from django.conf import settings
from .const_resumeweb import PRODUCT_LIST_COMPLETE
# prod_list_complete = []
def generate_product_list(PRODUCT_LINE):
    prod_list_others = []
    for j in PRODUCT_LIST_COMPLETE:
        if j[0]!=PRODUCT_LINE:
            prod_list_others.append(j)

    prod_list_others = [s[0] for s in prod_list_others]
    return prod_list_others
