from django.urls import path
from django.conf.urls import url, include


# dialogue >>> mprod_intprep
from ..views.products import (
    IntPrepHome,
    IntPrepServiceByCat,
    IntPrepServiceAll,
    IntPrepProdDetails_ajax,
    IntPrepProdDetails,

    IntPrepOurspeciality,
    IntPrepTerms,
    IntPrepHowItWorks,
    IntPrepUseCases,
    IntPrepCompareThis,
    IntPrepProductDeliveryMethods,
    IntPrepFAQ,
)


intprep_urls = [
    path("home",
        IntPrepHome.as_view(),
        name="intprep_home"
    ),
    path("all-services",
        IntPrepServiceAll.as_view(),
        name="intprep_all_services"
    ),
    path("category/<str:catname>",
        IntPrepServiceByCat.as_view(),
        name="intprep_bycat"
    ),
    path("service-details/<int:id>",
        IntPrepProdDetails,
        name="intprep_prod_details"
    ),




    path("terms-n-conditions",
        IntPrepTerms.as_view(),
        name="intprep_termscond"
    ),
    path("specialization",
        IntPrepOurspeciality.as_view(),
        name="intprep_specialization"
    ),


    path("how-it-works",
        IntPrepHowItWorks.as_view(),
        name="intprep_how_it_works"
    ),
    path("service-comparison",
        IntPrepCompareThis.as_view(),
        name="intprep_compare_this"
    ),
    path("use-cases",
        IntPrepUseCases.as_view(),
        name="intprep_use_cases"
    ),
    path("faq",
        IntPrepFAQ.as_view(),
        name="intprep_faq"
    ),    
    path("product-delivery-methods",
        IntPrepProductDeliveryMethods.as_view(),
        name="intprep_del_meth"
    ),

]
