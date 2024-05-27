from django.urls import path
from django.conf.urls import url, include


from ..views.products import (
    # us visa >>> bandwidth
    USvisaHome,
    USvisaServiceAll,
    # USvisaSearchResults,
    USvisaServiceByCat,
    USVisaProdDetails_ajax,
    USVisaProdDetails,

    USvisaTypeDetails,
    USvisaOurspeciality,
    USvisaHowItWorks,
    USvisaCompareThis,
    USvisaUseCases,
    USvisaFAQs,
    USvisaProductDeliveryMethods,
    JobLostSupport,

)


# bandwidth >>> mprod_visabased
usvisa_urls = [
    path("home",
        USvisaHome.as_view(),
        name="usvisa_home"
    ),
    path("all-services",
        USvisaServiceAll.as_view(),
        name="usvisa_all_services"
    ),
    path("us-visa-type-details",
        USvisaTypeDetails.as_view(),
        name="usvisa_type_details"
    ),    
    # path("us-visa-search-resuults",
    #     USvisaSearchResults.as_view(),
    #     name="usvisa_search_res"
    # ),
    path("category/<str:visaname>",
        USvisaServiceByCat.as_view(),
        name='usvisa_bycat'
    ),
    path("service-details/<int:id>",
        USVisaProdDetails,
        name="usvisa_prod_details"
    ),




    path("job-lost-support",
        JobLostSupport.as_view(),
        name="h1b-lost-job"),




    path("how-it-works",
        USvisaHowItWorks.as_view(),
        name="usvisa_how_it_works"
    ),
    path("how-we-diff",
        USvisaOurspeciality.as_view(),
        name="usvisa_our_speciality"
    ),
    path("service-comparison",
        USvisaCompareThis.as_view(),
        name="usvisa_compare_this"
    ),
    path("use-cases",
        USvisaUseCases.as_view(),
        name="usvisa_use_cases"
    ),
    path("faq",
        USvisaFAQs.as_view(),
        name="usvisa_faq"
    ),
    path("product-delivery-methods",
        USvisaProductDeliveryMethods.as_view(),
        name="usvisa_del_meth"
    ),

]
