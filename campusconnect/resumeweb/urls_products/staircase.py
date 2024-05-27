from django.urls import path
from django.conf.urls import url, include


# staircase >>> mprod_proflevel
from ..views.products import (
    ProfLevelHome,
    ProfLevelServiceAll,
    ProfLevelServiceByCat,
    ProfLevelServiceDetails_ajax,
    ProfLevelServiceDetails,

    ProfLevelHowItWorks,
    ProfLevelCompareThis,
    ProfLevelUseCases,
    ProfLevelFaq,
    ProfLevelProductDeliveryMethods,

)

staircase_urls = [
    path("home",
        ProfLevelHome.as_view(),
        name="proflevel_home"
    ),
    path("all-services",
        ProfLevelServiceAll.as_view(),
        name="proflevel_all_services"
    ),
    path("category/<str:levelname>",
        ProfLevelServiceByCat.as_view(),
        name='proflevel_bycat'
    ),
    path("prod-details/<int:id>",
        ProfLevelServiceDetails,
        name="proflevel_prod_details"
    ),




    path("how-it-works",
        ProfLevelHowItWorks.as_view(),
        name="proflevel_how_it_works"
    ),
    path("service-comparison",
        ProfLevelCompareThis.as_view(),
        name="proflevel_compare_this"
    ),
    path("use-cases",
        ProfLevelUseCases.as_view(),
        name="proflevel_use_cases"
    ),
    path("faq",
        ProfLevelFaq.as_view(),
        name="proflevel_faq"
    ),
    path("product-delivery-methods",
        ProfLevelProductDeliveryMethods.as_view(),
        name="proflevel_del_meth"
    ),

]
