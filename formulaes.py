rf_mys = 0.0340 #updated 25/7/2025 https://www.bnm.gov.my/government-securities-yield
mrp_mys = 0.0593 #updated 25/7/2025 https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/ctryprem.html
updatetime = "25/7/2025"


def cost_of_equity(beta, exp_return=""):
    if exp_return != "":
        coe = rf_mys + beta*(float(exp_return) - rf_mys)
    else:
        coe = rf_mys + beta*mrp_mys
    
    return coe
