from django.urls import path
from django.conf.urls import url, include

# identity >>> mprod_rolebased
from ..views.products import (
    IdentityServicesHome,
    JobTitleServiceAll,
    JobTitleServiceByCat,
    RoleBasedServiceDetails_ajax,
    RoleBasedServiceDetails,
    JobTitleServiceHowItWorks,
    JobTitleServiceCompareThis,
    JobTitleServiceUseCases,
    JobTitleServiceFaqs,
    JobTitleServiceProductDeliveryMethods,
)

identity_url = [
    path("home",
        IdentityServicesHome.as_view(),
        name="rolebased_home"
    ),
    path("all-services",
        JobTitleServiceAll.as_view(),
        name="rolebased_all_services"
    ),
    path("category/<str:rolename>",
        JobTitleServiceByCat.as_view(),
        name='rolebased_bycat'
    ),
    path("service-details/<int:id>",
        RoleBasedServiceDetails,
        name="rolebased_prod_details"
    ),




    path("how-it-works",
        JobTitleServiceHowItWorks.as_view(),
        name="identity_how_it_works"
    ),
    path("service-comparison",
        JobTitleServiceCompareThis.as_view(),
        name="identity_compare_this"
    ),
    path("use-cases",
        JobTitleServiceUseCases.as_view(),
        name="identity_use_cases"
    ),
    path("faq",
        JobTitleServiceFaqs.as_view(),
        name="identity_faq"
    ),
    path("product-delivery-methods",
        JobTitleServiceProductDeliveryMethods.as_view(),
        name="identity_del_meth"
    ),

]
