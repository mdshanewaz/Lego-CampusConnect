from django.urls import path
from django.conf.urls import url, include


# dialect >>> mprod_proglang
from ..views.products import (
    ProgLangHome,
    ProgLangServiceAll,
    ProgLangServiceByCat,
    ProgLangServiceProdDetails_ajax,
    ProgLangServiceProdDetails,

    ProgLangHowItWorks,
    ProgLangCompareThis,
    ProgLangUseCases,
    ProgLangFAQ,
    ProgLangProductDeliveryMethods

)


# dialect >>> mprod_proglang
dialect_url = [
    path("home",
        ProgLangHome.as_view(),
        name="proglang_home"
    ),
    path("all-services",
        ProgLangServiceAll.as_view(),
        name="proglang_all_services"
    ),
    path('category/<str:langname>',
        ProgLangServiceByCat.as_view(),
        name='proglang_bycat'
    ),
    path("service-details/<int:id>",
        ProgLangServiceProdDetails,
        name="proglang_prod_details"
    ),



    path("how-it-works",
        ProgLangHowItWorks.as_view(),
        name="proglang_how_it_works"
    ),
    path("service-comparison",
        ProgLangCompareThis.as_view(),
        name="proglang_compare_this"
    ),
    path("use-cases",
        ProgLangUseCases.as_view(),
        name="proglang_use_cases"
    ),
    path("faq",
        ProgLangFAQ.as_view(),
        name="proglang_faq"
    ),
    path("product-delivery-methods",
        ProgLangProductDeliveryMethods.as_view(),
        name="proglang_del_meth"
    ),
]
