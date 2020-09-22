def compound_period(period):
    if period == "annually":
        annually = 1
        return annually
    elif period == "semi-annually":
        semi_annually = 2
        return semi_annually
    elif period == "quarterly":
        quarterly = 4
        return quarterly
    elif period == "bi-monthly":
        bi_monthly = 6
        return bi_monthly
    elif period == "monthly":
        monthly = 12
        return monthly
    elif period == "semi-monthly":
        semi_monthly = 24
        return semi_monthly
    elif period == "weekly":
        weekly = 52
        return weekly
    elif period == "daily":
        daily = 365
        return daily
    elif period == "continuously":
        continuously = 2.718281828
        return continuously