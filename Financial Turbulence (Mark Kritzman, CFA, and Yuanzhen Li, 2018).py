import pandas as pd
import numpy as np
import yfinance as yf
import math
import matplotlib.pyplot as plt
import seaborn as sns

# 1st Chapter: getting data 
# Source Yahoo Finance
# In order to obtain a wide image of the global financial turbulence the following assets classes and their respective indexes were used:
# The main data focus is on American financial assets due to the major influence that the American economy has on the other economies
# US stock assets = S&P 500
# Non-US stock assets = SPDR EURO STOXX ETF (FEZ)
# US bonds = Invesco BulletShares 2023 Corporate Bond ETF (BSCN)
# Techonological assets = NASDAQ Composite (^IXIC)
# Commodity assets = Invesco DB Commodity Index Tracking Fund (DBC)
# US Real Estate = Vanguard Real Estate Index Fund (VNQ)

US_stock_assets = yf.Ticker("^GSPC")
Non_US_stock_assets = yf.Ticker("FEZ")
Technological_assets = yf.Ticker("^IXIC")
US_bonds = yf.Ticker("BSCN")
US__realestate_assets = yf.Ticker("VNQ")
Commodity_assets = yf.Ticker("DBC")

US_stock_assets = US_stock_assets.history(period = "5y", interval = "1wk")
Non_US_stock_assets = Non_US_stock_assets.history(period = "5y", interval = "1wk")
Technological_assets = Technological_assets.history(period = "5y", interval = "1wk")
US_bonds = US_bonds.history(period = "5y", interval = "1wk")
US__realestate_assets = US__realestate_assets.history(period = "5y", interval = "1wk")
Commodity_assets = Commodity_assets.history(period = "5y", interval = "1wk")

# 2nd Chapter: Data modification 
# In order to calculate the Financial Turbulence using the formula devised by Mark Kritzman, CFA, and Yuanzhen Li in 2018

Monthly_returns_US_stock_assets = US_stock_assets["Close"].pct_change()[1:]
Monthly_returns_Non_US_stock_assets = Non_US_stock_assets["Close"].pct_change()[1:]
Monthly_returns_Technological_assets = Technological_assets["Close"].pct_change()[1:]
Monthly_returns_US_bonds = US_bonds["Close"].pct_change()[1:]
Monthly_returns_US__realestate_assets = US__realestate_assets["Close"].pct_change()[1:]
Monthly_returns_Commodity_assets = Commodity_assets["Close"].pct_change()[1:]

Historical_average_Monthly_returns_US_stock_assets = np.matrix(np.average(Monthly_returns_US_stock_assets)).repeat(262)
Historical_average_Monthly_returns_Non_US_stock_assets = np.matrix(np.average(Monthly_returns_Non_US_stock_assets)).repeat(262)
Historical_average_Monthly_returns_Technological_assets = np.matrix(np.average(Monthly_returns_Technological_assets)).repeat(262)
Historical_average_Monthly_returns_US_bonds = np.matrix(np.average(Monthly_returns_US_bonds)).repeat(262)
Historical_average_Monthly_returns_US__realestate_assets = np.matrix(np.average(Monthly_returns_US__realestate_assets)).repeat(262)
Historical_average_Monthly_returns_Commodity_assets = np.matrix(np.average(Monthly_returns_Commodity_assets)).repeat(262)


Assets_monthly_returns = {"US stock assets": Monthly_returns_US_stock_assets, 
                          "Non US stock assets": Monthly_returns_Non_US_stock_assets,
                          "Technological assets": Monthly_returns_Technological_assets,
                          "US corporate bonds": Monthly_returns_US_bonds,
                          "US Real Estate assets": Monthly_returns_US__realestate_assets,
                          "Commodity assets": Monthly_returns_Commodity_assets
    
}

Assets_monthly_returns  = pd.DataFrame(Assets_monthly_returns, columns = ["US stock assets","Non US stock assets", "Technological assets","US corporate bonds","US Real Estate assets","Commodity assets"])

Assets_monthly_returns = Assets_monthly_returns.dropna()
Assets_monthly_returns = np.matrix(Assets_monthly_returns).transpose()


cov_matrix = np.cov(Assets_monthly_returns, bias=True)

# Types of Portfolio and their respective asset weights (according to Mark Kritzman, CFA, and Yuanzhen Li, 2018)
# With the addition of Techonological assets category
# Conservative (in this portfolio the Technological assets represent 25% of the orginal US stocks weight
# and the US stock assets have now a weight of 75% of their original weight)
Conservative_weight_US_stock_assets = 0.17145
Conservative_weight_Non_US_stock_assets = 0.1659
Conservative_weight_Technological_assets = 0.05715
Conservative_weight_US_bonds = 0.4995
Conservative_weight_US__realestate_assets = 0.0385
Conservative_weight_Commodity_assets = 0.0675

# Moderate (in this portfolio the Technological assets represent 50% of the orginal US stocks weight
# and the US stock assets have now a weight of 50% of their original weight)
Moderate_weight_US_stock_assets = 0.17615
Moderate_weight_Non_US_stock_assets = 0.2422
Moderate_weight_Technological_assets = 0.17615
Moderate_weight_US_bonds = 0.3281
Moderate_weight_US__realestate_assets = 0.0259
Moderate_weight_Commodity_assets = 0.0516

# Aggressive (in this portfolio the Technological assets represent 75% of the orginal US stocks weight
# and the US stock assets have now a weight of 25% of their original weight)
Aggressive_weight_US_stock_assets = 0.120375
Aggressive_weight_Non_US_stock_assets = 0.3219
Aggressive_weight_Technological_assets = 0.361125
Aggressive_weight_US_bonds = 0.1489
Aggressive_weight_US__realestate_assets = 0.0128
Aggressive_weight_Commodity_assets = 0.0349

Conservative_Monthly_returns_US_stock_assets = Monthly_returns_US_stock_assets*Conservative_weight_US_stock_assets
Conservative_Monthly_returns_Non_US_stock_assets = Monthly_returns_Non_US_stock_assets*Conservative_weight_Non_US_stock_assets
Conservative_Monthly_returns_Technological_assets = Monthly_returns_Technological_assets*Conservative_weight_Technological_assets
Conservative_Monthly_returns_US_bonds = Monthly_returns_US_bonds*Conservative_weight_US_bonds
Conservative_Monthly_returns_US__realestate_assets = Monthly_returns_US__realestate_assets*Conservative_weight_US__realestate_assets
Conservative_Monthly_returns_Commodity_assets = Monthly_returns_Commodity_assets*Conservative_weight_Commodity_assets

Conservative_portfolio_monthly_returns = Conservative_Monthly_returns_US_stock_assets+Conservative_Monthly_returns_Non_US_stock_assets+Conservative_Monthly_returns_Technological_assets+Conservative_Monthly_returns_US_bonds+Conservative_Monthly_returns_US__realestate_assets+Conservative_Monthly_returns_Commodity_assets
Conservative_portfolio_monthly_returns = Conservative_portfolio_monthly_returns.dropna()
plt.subplot(2,2,1)
plt.plot(Conservative_portfolio_monthly_returns)
Conservative_portfolio_monthly_returns = np.matrix(Conservative_portfolio_monthly_returns)

Moderate_Monthly_returns_US_stock_assets = Monthly_returns_US_stock_assets*Moderate_weight_US_stock_assets
Moderate_Monthly_returns_Non_US_stock_assets = Monthly_returns_Non_US_stock_assets*Moderate_weight_Non_US_stock_assets
Moderate_Monthly_returns_Technological_assets = Monthly_returns_Technological_assets*Moderate_weight_Technological_assets
Moderate_Monthly_returns_US_bonds = Monthly_returns_US_bonds*Moderate_weight_US_bonds
Moderate_Monthly_returns_US__realestate_assets = Monthly_returns_US__realestate_assets*Moderate_weight_US__realestate_assets
Moderate_Monthly_returns_Commodity_assets = Monthly_returns_Commodity_assets*Moderate_weight_Commodity_assets

Moderate_portfolio_monthly_returns = Moderate_Monthly_returns_US_stock_assets+Moderate_Monthly_returns_Non_US_stock_assets+Moderate_Monthly_returns_Technological_assets+Moderate_Monthly_returns_US_bonds+Moderate_Monthly_returns_US__realestate_assets+Moderate_Monthly_returns_Commodity_assets
Moderate_portfolio_monthly_returns = Moderate_portfolio_monthly_returns.dropna()
plt.subplot(2,2,2)
plt.plot(Moderate_portfolio_monthly_returns)
Moderate_portfolio_monthly_returns = np.matrix(Moderate_portfolio_monthly_returns)

Aggressive_Monthly_returns_US_stock_assets = Monthly_returns_US_stock_assets*Aggressive_weight_US_stock_assets
Aggressive_Monthly_returns_Non_US_stock_assets = Monthly_returns_Non_US_stock_assets*Aggressive_weight_Non_US_stock_assets
Aggressive_Monthly_returns_Technological_assets = Monthly_returns_Technological_assets*Aggressive_weight_Technological_assets
Aggressive_Monthly_returns_US_bonds = Monthly_returns_US_bonds*Aggressive_weight_US_bonds
Aggressive_Monthly_returns_US__realestate_assets = Monthly_returns_US__realestate_assets*Aggressive_weight_US__realestate_assets
Aggressive_Monthly_returns_Commodity_assets = Monthly_returns_Commodity_assets*Aggressive_weight_Commodity_assets

Aggressive_portfolio_monthly_returns = Aggressive_Monthly_returns_US_stock_assets+Aggressive_Monthly_returns_Non_US_stock_assets+Aggressive_Monthly_returns_Technological_assets+Aggressive_Monthly_returns_US_bonds+Aggressive_Monthly_returns_US__realestate_assets+Aggressive_Monthly_returns_Commodity_assets
Aggressive_portfolio_monthly_returns = Aggressive_portfolio_monthly_returns.dropna()
plt.subplot(2,2,3)
plt.plot(Aggressive_portfolio_monthly_returns)
Aggressive_portfolio_monthly_returns = np.matrix(Aggressive_portfolio_monthly_returns)

Historical_average_Aggressive_portfolio_monthly_returns = np.matrix(np.average(Aggressive_portfolio_monthly_returns)).repeat(261)
Historical_average_Moderate_portfolio_monthly_returns = np.matrix(np.average(Moderate_portfolio_monthly_returns)).repeat(261)
Historical_average_Conservative_portfolio_monthly_returns = np.matrix(np.average(Conservative_portfolio_monthly_returns)).repeat(261)



# 3rd Chapter: Financial Turbulence Estimation using Mahalanobis distance as a basis (the same formula used by Mark Kritzman, CFA, and Yuanzhen Li, 2018)

Table = {"US stock assets": Monthly_returns_US_stock_assets-np.average(Monthly_returns_US_stock_assets), 
                          "Non US stock assets": Monthly_returns_Non_US_stock_assets-np.average(Monthly_returns_Non_US_stock_assets),
                          "Technological assets": Monthly_returns_Technological_assets-np.average(Monthly_returns_Non_US_stock_assets),
                          "US corporate bonds": Monthly_returns_US_bonds-np.average(Monthly_returns_US_bonds),
                          "US Real Estate assets": Monthly_returns_US__realestate_assets-np.average(Monthly_returns_US__realestate_assets),
                          "Commodity assets": Monthly_returns_Commodity_assets-np.average(Monthly_returns_Commodity_assets)
    
}

Table  = pd.DataFrame(Table, columns = ["US stock assets","Non US stock assets", "Technological assets","US corporate bonds","US Real Estate assets","Commodity assets"])

Table = Table.dropna()

Table.reset_index(inplace=True)
Dates = Table["Date"]


Assets_monthly_returns_minus_average = {"US stock assets": Monthly_returns_US_stock_assets-np.average(Monthly_returns_US_stock_assets), 
                          "Non US stock assets": Monthly_returns_Non_US_stock_assets-np.average(Monthly_returns_Non_US_stock_assets),
                          "Technological assets": Monthly_returns_Technological_assets-np.average(Monthly_returns_Technological_assets),
                          "US corporate bonds": Monthly_returns_US_bonds-np.average(Monthly_returns_US_bonds),
                          "US Real Estate assets": Monthly_returns_US__realestate_assets-np.average(Monthly_returns_US__realestate_assets),
                          "Commodity assets": Monthly_returns_Commodity_assets-np.average(Monthly_returns_Commodity_assets)
    
}

Assets_monthly_returns_minus_average  = pd.DataFrame(Assets_monthly_returns_minus_average, columns = ["US stock assets","Non US stock assets", "Technological assets","US corporate bonds","US Real Estate assets","Commodity assets"])

Assets_monthly_returns_minus_average = Assets_monthly_returns_minus_average.dropna()
Assets_monthly_returns_minus_average = np.matrix(Assets_monthly_returns_minus_average)

Inverse_Covariance_matrix = np.linalg.inv(cov_matrix)

Financial_Turbulence = []

for i in range(261):
    Financial_Turbulence.append(np.matmul(np.matmul(Assets_monthly_returns_minus_average[i], Inverse_Covariance_matrix),Assets_monthly_returns_minus_average[i].transpose()))

Financial_Turbulence = np.array(Financial_Turbulence)
Financial_Turbulence = np.squeeze(Financial_Turbulence)

plt.subplot(2,2,4)
plt.plot(Dates, Financial_Turbulence)

plt.show()
