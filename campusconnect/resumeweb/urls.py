from django.conf.urls import url, include
from django.urls import path

# product
from .urls_products import (
    usvisa_urls,
    dialect_url,
    intprep_urls,
    exp180_urls,
    # mmr_eval_urls,
    identity_url,
    staircase_urls,
    strat_sol_urls
)

# product details
from .views.products import (
    USVisaProdDetails_ajax,
    RoleBasedServiceDetails_ajax,
    ProgLangServiceProdDetails_ajax,
    IntPrepProdDetails_ajax,
    Exp180DetailView_ajax,
    # EvalDetailView_ajax,
    ProfLevelServiceDetails_ajax,
    StratSolProdDetails_ajax,
)

# cart
from .views import (
    mmh_CartHome,
    mmh_CartFileUpload,
    # mmh_CartUserLogin,
    mmh_CartGuestLogin,
    mmh_CartLoginPage,
    mmh_CartLoginOrGuestSuccess,
    mmh_CartPurchaseSuccess,
    rwCartAjaxView_contents,
    rwCartAjaxView_carticon,
    rwCartAjaxView_emptycart,
    rwCartAjaxView_removebymodelnameandid,
    rwCartAjaxView_addproductver2,
    rwCartAjaxView_removeproductver2,
    # rwCartAjaxView_applycoupontocart,
    # rwCartAjaxView_unapplycoupontocart,
    # rwCartAjaxView_applycoupon,

)

# paypal
from .views import (
    vcreate,
    vcapture,
)

# user permissions
from .views import (
    vug_failed_test,
)

# general
from .views import(
    HomePageView,
    Page404View,
    AboutUsView,
    # top news
    Covid19ResponseView,
    BLMResponseView,
    PromotionalOffersView,
    ThisIsBeta,
    UsOnlySupport,
    # help center
    HelpCenterHome,
    MemberBenefitsView,
)



site_general_urls = [
    path("", 
        HomePageView.as_view(), 
        name="site_homepage_url"
    ),
    path("home/", 
        HomePageView.as_view(), 
        name="site_homepage_url"
    ),
    path("product-docs/all",
        AboutUsView.as_view(),
        name="about_us"
    ),
    path("page-404-view", 
        Page404View.as_view(), 
        name="page_404_view"
    ),

]



############################## news section
topnews_urls = [
    path("covid19-response", 
        Covid19ResponseView.as_view(), 
        name="covid19_res_url"
    ),
    path("how-we-tackle-racial-injudtice", 
        BLMResponseView.as_view(), 
        name="blm_page"
    ),
    path("promotional-offers", 
        PromotionalOffersView.as_view(), 
        name="promo_offers_page"
    ),
    path("us-only", 
        UsOnlySupport.as_view(), 
        name="us_only_support"
    ),    
    path("beta", 
        ThisIsBeta.as_view(), 
        name="this_is_beta"
    ),        
]



footer_urls = [
    # help center section
    ############################## 
    path("help-center/home",
        HelpCenterHome.as_view(),
        name="cust_service_home"
    ),
    path("help-center/membership-benefits",
        MemberBenefitsView.as_view(),
        name="mem_ben_url"
    ),    
]

all_product_urls = [
    # products that use cart
    path("exp180/",                     include(exp180_urls)),          # mprod_exp180
    # path("eval/",                     include(mmr_eval_urls)),        # mprod_eval
    path("dialogue/",                   include(intprep_urls)),         # mprod_intprep
    path("staircase/",                  include(staircase_urls)),       # mprod_proflevel
    path("dialect/",                    include(dialect_url)),          # mprod_proglang
    path("identity/",                   include(identity_url)),         # mprod_rolebased
    path("strategy/",                   include(strat_sol_urls)),       # mprod_strategy
    path("bandwidth/",                  include(usvisa_urls)),          # mprod_visabased
]

# cart urls
mmh_cart_urls = [
    path("cart/home/mmh",                                       mmh_CartHome,                               name="mmh_carthome"),
    path("cart/upload",                                         mmh_CartFileUpload,                         name="mmh_cartfileupload"),
    # path("checkout/sign-in/mmh/userlogin",                      mmh_CartUserLogin,                          name="mmh_cartuserlogin"),
    path("checkout/sign-in/mmh",                                mmh_CartLoginPage,                          name="mmh_cartcheckout"),
    path("checkout/sign-in/mmh/loginorguestsuccess",            mmh_CartLoginOrGuestSuccess,                name="mmh_cartloginorguestsuccess"),
    path("checkout/sign-in/mmh/guestlogin",                     mmh_CartGuestLogin,                         name="mmh_cartguestlogin"),
    path("checkout/success/<str:paypaltransaction_id>",         mmh_CartPurchaseSuccess,                    name="mmh_cartpurchasesuccess"),
]

# cart AJAX urls
mmh_cart_urls_ajax = [
    path("contents",                                            rwCartAjaxView_contents,                name="rwCartAjaxView_contents"),
    path("carticon",                                            rwCartAjaxView_carticon,                name="rwCartAjaxView_carticon"),
    path("emptycart",                                           rwCartAjaxView_emptycart,               name="rwCartAjaxView_emptycart"),
    path("removebymodelnameandid",                              rwCartAjaxView_removebymodelnameandid,  name="rwCartAjaxView_removebymodelnameandid"),
    path("addproductver2",                                      rwCartAjaxView_addproductver2,          name="rwCartAjaxView_addproductver2"),
    path("removeproductver2",                                   rwCartAjaxView_removeproductver2,       name="rwCartAjaxView_removeproductver2"),
    # path("applycoupontocart/<str:string32>",                    rwCartAjaxView_applycoupontocart,       name="rwCartAjaxView_applycoupontocart"),
    # path("unapplycoupontocart/<str:string32>",                  rwCartAjaxView_unapplycoupontocart,     name="rwCartAjaxView_unapplycoupontocart"),
    # path("applycoupon",                                         rwCartAjaxView_applycoupon,             name="rwCartAjaxView_applycoupon"),
]

# paypal_urls
mmh_vpaypal_urls = [
    path('vcreate', vcreate, name="vpaypal_vcreate"),
    path('vcapture/<order_id>', vcapture, name="vpaypal_vcapture"),
]

# cart ajax detail product views
mmh_cart_detail_ajax_product_views = [
    path("mprod_exp180/<int:id>",       Exp180DetailView_ajax,              name="exp180_detail_view_link_ajax"),
    path("mprod_intprep/<int:id>",      IntPrepProdDetails_ajax,            name="intprep_detail_view_link_ajax"),
    path("mprod_proflevel/<int:id>",    ProfLevelServiceDetails_ajax,       name="proflevel_detail_view_link_ajax"),
    path("mprod_proglang/<int:id>",     ProgLangServiceProdDetails_ajax,    name="proglang_detail_view_link_ajax"),
    path("mprod_rolebased/<int:id>",    RoleBasedServiceDetails_ajax,       name="rolebased_detail_view_link_ajax"),
    path("mprod_strategy/<int:id>",     StratSolProdDetails_ajax,           name="strategy_detail_view_link_ajax"),
    path("mprod_visabased/<int:id>",    USVisaProdDetails_ajax,             name="visabased_detail_view_link_ajax"),
]


# user permissions
vusergroup_views = [
    path("failedtest/<str:testname>/<str:viewname>/<str:optionalmessage>",  vug_failed_test,     name="vug_failed_test"),
    path("failedtest/<str:testname>/<str:viewname>",                        vug_failed_test,     name="vug_failed_test"),
]


## final url declaration
########################
## GENERAL STUFF
SITE_GENERAL       = [path("",                 include(site_general_urls)),]
FOOTER            = [path("",                 include(footer_urls)),]

TOPNEWS            = [path("news/",            include(topnews_urls)),]


## CART + PayPal
MMH_CART       = [path("cart/",            include(mmh_cart_urls)),]
MMH_CART_AJAX  = [path("cart_ajax/",       include(mmh_cart_urls_ajax)),]
MMH_AJAX_DETAIL     = [path("ajax_detail/",     include(mmh_cart_detail_ajax_product_views)),]
PAYPAL         = [path("vpaypal/",         include(mmh_vpaypal_urls)),]
## PRODUCT PAGES
PRODUCT        = [path("service/",         include(all_product_urls)),]
## USER PERMISSIONS
USERGROUP      = [path("vug/",             include(vusergroup_views)),]


urlpatterns =   SITE_GENERAL
urlpatterns +=  FOOTER
urlpatterns +=  TOPNEWS

urlpatterns +=  MMH_CART
urlpatterns +=  MMH_CART_AJAX
urlpatterns +=  MMH_AJAX_DETAIL
urlpatterns +=  PAYPAL
urlpatterns +=  PRODUCT
urlpatterns +=  USERGROUP
