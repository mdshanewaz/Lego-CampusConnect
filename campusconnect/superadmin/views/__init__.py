from .cart import *

from .coupon import (
	admin_mcoupon,
)

from .login import (
	MyLoginView,
)

from .others import (
	# admin_GuestResumeFiles,
	AdminSiteSurvey,
	Adminmsendmail,
)

from .users import (
	AdminVerifiedUsers
)

# product lines 
# ------------------------------------------------
from .prod_adhoc import (
	AdminAdhocRequests
)

from .prod_bandwidth import (
	Admin_USVISA_CAT_LIST,
	Admin_USVISA_SERV_LIST,
	AdminUSvisaServiceoption,
	admin_mprod_visabased_deliveryoption,
)

from .prod_dialect import (
	admin_mprod_proglang_catlist,
	AdminProglangServlist,
	AdminProglangServiceoption,
	admin_mprod_proglang_deliveryoption,

)

from .prod_dialogue import (
	admin_mprod_intprep_catlist,
	AdminIntprepServList,
	AdminIntprepServiceoption,
	admin_mprod_intprep_deliveryoption,
)

from .prod_exp180 import (
	AdminExp180ServList,
	AdminExp180Serviceoption,
	admin_mprod_exp180_deliveryoption,

)

from .prod_identity import (
	AdminTechRoleCatList,
	AdminTechRoleServList,
	AdminTechRoleServiceoption,
	AdminTechRoleDelivOption,

)

from .prod_staircase import (
	admin_mprod_proflevel_catlist,
	AdminProflevelServlist,
	AdminProflevelServiceoption,
	admin_mprod_proflevel_deliveryoption,

)

from .prod_strategy import (
	AdminStrategyCatList,
	AdminStrategyServList,
	AdminStrategyServiceoption,
	admin_mprod_strategy_deliveryoption,

)

from .prof_candidate import (
	AdminOrderCancellationRequest,
	MyResAdmin,
	MyResFormAdmin,
	DispCauseAdmin,
	DisputeAdmin,
	CandidateMessageAdmin,
	DeactivatedAccountAdmin,

)
