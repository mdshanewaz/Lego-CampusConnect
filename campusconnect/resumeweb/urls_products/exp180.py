from django.urls import path
from django.conf.urls import url, include


# exp180 >>> mprod_exp180
from ..views.products import (
    Exp180Home,
    Exp180DetailView_ajax,
    Exp180DetailView,
    Exp180ServiceAll,
    Exp180ServiceBycat,

    Exp180HowItWorks,
    Exp180CompareThis,
    Exp180UseCases,
    Exp180ProductDeliveryMethods,
    Exp180FAQ,
)


exp180_urls = [
    path("home",
        Exp180Home.as_view(),
        name="exp180_homepg_url"
    ),
    path("all-services",
        Exp180ServiceAll.as_view(),
        name="exp180_services_all"
    ),
    path("category/<str:category>",
        Exp180ServiceBycat.as_view(),
        name="exp180_services_bycat"
    ),    
    path("service-details/<int:id>",
        Exp180DetailView,
        name="exp180_detail_view_link"
    ),




    path("how-it-works",
        Exp180HowItWorks.as_view(),
        name="exp180_how_it_works"
    ),
    path("service-comparison",
        Exp180CompareThis.as_view(),
        name="exp180_compare_this"
    ),
    path("use-cases",
        Exp180UseCases.as_view(),
        name="exp180_use_cases"
    ),
    path("faq",
        Exp180FAQ.as_view(),
        name="exp180_faq"
    ),
    path("product-delivery-methods",
        Exp180ProductDeliveryMethods.as_view(),
        name="exp180_del_meth"
    ),

]
