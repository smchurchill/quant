from quantopian.algorithm attach_pipeline, pipeline_input
from quantopian.pipeline import Pipeline
from quantopian.pipeline.factors import CustomFactor, AverageDollarAmount

def initialize(context):

    build_list()
    
    schedule_function(
        rebalance_heavy,
        date_rules.month_start(),
        time_rules.market_open(hours = 1, minutes = 0)        
    )

    schedule_function(
        rebalance_lite,
        date_rules.every_day(),
        time_rules.market_open(hours = 1, minutes = 30)
    )
        
    
def rebalance_lite(context, data):

    for security in context.securities:
        l = data.history(assets=security, fields='price', frequency='1m')
        ma = average(l)
        sd = standard_deviation(l)
        c = current_price
        if(c < (ma - 2*sd)):
            order_target_percent(security, 0)
        else if((ma - 2*sd < c) && (c < ma - sd)):
            order_target_percent(security, equal_share())
        else if(c > ma + sd):
            order_target_percent(security, 0)
        
def rebalance_heavy(context, data):
    


def build_list(context, data):
    # filter by dividends

