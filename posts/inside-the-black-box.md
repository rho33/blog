<!--
.. title:  
.. slug: inside-the-black-box-notes
.. date: 2020-01-22 15:56:51 UTC-08:00
.. tags: 
.. category: Book Notes
.. link: 
.. description: 
.. type: text
-->

# Inside the Black Box: The Simple Truth About Quantitative Trading
by Rishi K Narange


## Chapter 1. Why Does Quant Trading Matter
- A rapidly growing proportion of all trading is automated.
- Quants are forced to theink deeply about trading strategies.
- Quants measure and mismeasure risk.
- Computers are more disciplined in execution of strategies.

## Chapter 2. An Introduction to Quantitative Trading
- Quant strategies are often viewed as complex and secretive (a "black box").
- A quant systematically applies an alpha-seeking investment strategy that was specified based on exhaustive research, emphasis is on how strategies are conceived and implemented.
- Once a strategy goes live, human judgement is generally limited in day-to-day management.
- Strategies exist on a spectrum between fully systematic and fully discretionary.
- Typical structure of quantitative system:
    ![f](https://gdurl.com/GipZ)

## Chapter 3. Alpha Models: How Quants Make Money
- Alpha models are "designed to time the selection and/or sizing of portfolio holdings. They hold as a core premise that no instrument is inherently good or bad, and therefore no instrument is worth always owning or perpetually ignoring."
- Alpha models are "the software that a quant builds and uses to conduct this timeing"
    - Synonyms for alpha model: 
        - forecasts
        - factors
        - alphas
        - models
        - strategies
        - estimators
        - predictors
- Theory driven alpha models resemble traditional science where hypotheses are formulated then tested.
- Data driven alpha models rely on correctly performed empirical observations to predict future patterns in the absence of coherent explanation.
    - similar to The Human Genome Project
    - also called data miners
- Theory-Driven Alpha Models
    - Strategies utilizing price-related data:
        - trend following
        - Mean reversion
            - Includes statistical arbitrage
    - Strategies utilizing fundamental data:
        - **value/yield** - relies on measures of cheapness (P/E, E/P, book to price, EBITDA, carry trading...)
        - **growth** - relies on historical/expected economic growth (EPS Growth rate, P/E vs EPS growth, sentiment data...)
        - **quality** - seek to own "quality" instruments, values capital safety (debt to equity ratios, earnings quality signals)
- Data-Driven Alpha Models
    - more difficult to understand
    - more technically challenging
    - favored by many high frequency traders
    - may be more favorable at shorter time horizons
    - shortcomings:
        - more likely to find spurious correlations and false signals
        - often require substantial processing power
        - need constant adjustments for market change
        - often end up resembling trend following or mean reverting strategies anyway
- Implementing the Strategies
    - Strategies can forecast direction, magnitude, duration, and confidence level of a move.
        - Greater signal strength generally results in bigger positions.
    - Time Horizons
        - high frequency - less than a day
        - short term - 1 day to 2 weeks
        - medium term - weeks to months
        - long term - several months or more
    - Bet Structures
        - intrinsic - betting on direction of instrument
        - relative - betting on direction of instrument relative to other instruments
            - e.g. pairs trading, stock movement w/in sector
            - important to note that the phrase "relative value" is hedgefund jargon which refers to relative bet structures but does not necessarily refer to value investing
    - Investment Universe Choices
        - geography (e.g. USA vs Hong Kong)
        - asset class (e.g. forex vs equities)
        - instrument class (e.g. indicies vs individual stocks)
        - Quants prefer liquid assets with large quantities of high quality data.
    - Model Specification
        - Every aspect of strategy must be defined before it is usable such as how to define a trend and how often to refit.
        - Machine learning/data mining techniques are often more suited to defining model specification details than to finding alpha.
    - Run Frequency - how often to run model 
        - more often can be noisy
        - less often can miss opportunities and lead to larger trades that "move the market."
        - Most quants run model at least once per week
    - Blending Alpha Models Approaches
        - linear (multiple regression)
        - nonlinear
            - conditional - weight of one alpha factor based on weight of another
            - rotational - follows trends in performance of alpha models
            - machine learning - this is a good problem for ML

## Chapter 4. Risk Models
- "But the fact remains that one of the great strengths of quant trading is to be able to measure various exposures and to be intentional about the selection of such exposures"
- limiting the amount of risk
    - by constraint - hard line limit level (e.g. no position larger than x% of portfolio)
    - by penalty function - the further from the position limit level the position becomes the more difficult it is to add to position (more alpha/signal strength required)
        - can be thought of as making rules to govern exceptions
- risk measures:
    - volatility - standard deviation of returns
    - dispersion - correlation/covariance among instruments in a given universe
- where limits can be applied
    - size of positions/groups of positions
    - size of exposure to types of risk (e.g. +/- 5% net exposure to market direction)
    - controlling leverage
    - value at risk models (VaR)
        - current levels of volatility used to forecast portfolio gain/loss within given confidence interval
- limiting types of risk
    - "some apporaches to risk modeling focus on eliminating whole types of exposure entirely."
    - "As a general rule, it is always better to eliminate any unintentional exposures, siince there should be no expectation of being compensated sufficiently for accepting them."
    - alpha models can incorporate risk management concepts (e.g. forecasting stocks relative to their sectors means not ahving to bet on sector itself)
    - theory-driven risk models
        - "Theory-driven risk modeling uses a set of pre-defined systematic risks, which enables the quant to measure and calibrate a given portfolio's exposure"
            - systematic risk - risks that cannot be diversified away (e.g. sector risk, market cap risk, interest rate risk...)
        - risks derived from theory i.e. there are reasonable economic arguments for the existence of risk types
        - either make intentional bets on systematic risk or eliminate exposure
    - empirical risk models
        - "uses historical data to determine what risks are and how exposed a given portfolio is to them"
        - uses statistical techniques such as principal component analysis (PCA) to discern systematic risks that may or may not correspond to named risk factors
    - how quants choose a risk model
        - empirical risk models chosen for adaptiveness
            - however there is an adaptiveness vs. significance trade off
        - theory driven makes sense if it is likely to be true (i.e. strong theoretical underpinnings)
        - most quants tend toward theory driven
        
## Chapter 5. Transaction Cost Models
- "Note that transaction cost models are not designed to minimize the cost of trading, only to inform the portfolio construction engine of the costs of making any given trade"
    - execution algorithm responsible for minimizing costs
- components of transaction cost model
    - commissions and fees - brokerage fees for clearing and settlement services
    - slippage - change in price between time trader decides to transact and when the order is actually at exchange
    - market impact - price moving as a result of traders order
- types of transaction cost models
    - flat - same cost for each order
        - simplest
        - not widely used
    - linear - cost increases with size of order in linear fashion
    - piecewise linear
        - more accurate than linear
    - quadratic
        - most complex
        - most accurate
        - pain to build
        
## Chapter 6. Portfolio Construction Models
- The portfolio construction models acts like an arbitrator, hearing all the arguments of the alpha model, risk model, and transaction cost model and then makes a decision about how to proceed.
- 2 types: rule based and optimized
- rule-based portfolio construction models
    - equal position
        - eliminates disadvantages of unequal weighting (adverse selection bias, dificulty predicting magnitude of moves)
    - equal risk weighting
        - position sizes are inversely related to volatility (or other risk measure)
    - alpha-driven weighting
        - greater alpha prediction = greater position size
        - often used with limits on position groups (aset classes, sectors...)
        - can exascerbate drawdowns (e.g. by falling victim to adverse selection in a trend following strategy)
    - decision-tree models
        - decision trees with internal nodes representing model predictions and leaf nodes assigning a position size
        - decision trees can be used to combine alpha models
        - leaf node position sizes can be functions of the risk model and/or transaction cost model
- portfolio optimizers
    - "Portfolio optimization is one of the most important topics in quantitative finance."
    - mean variance optimization - seeks to determine the portfolios with highest return at each level of risk (called the efficient frontier)
        - also called modern portfolio theory
    - inputs to optimization
        - expected return (alpha)
        - expected volatility
            - stochastic volatility models
                - Generalized Autoregressive Conditional Heteroskedasticity (GARCH) models
        - expected correlation between assets (correlation matrix)
            - Correlations can be unstable over time but stability should improve with appropriately selected groups
    - optimization techniques
        - unconstrained
            - can end up suggesting that all money be invested in the instrument with the highest risk-adjusted return
        - constrained
            - can defeat purpose of optimizing with constraints driving portfolio selection more than the optimizer
        - Black-Litterman optimizer (below notes are from wikipedia)
            -  starts with the equilibrium assumption that the asset allocation of a representative agent should be proportional to the market values of the available assets , and then modifies that to take into account the 'views' (i.e., the specific opinions about asset returns) of the investor in question to arrive at a bespoke asset allocation (this is from wikipedia)
                - it assumes that the initial expected returns are whatever is required so that the equilibrium asset allocation is equal to what we observe in the markets
            - The user is only required to state how his assumptions about expected returns differ from the markets and to state his degree of confidence in the alternative assumptions. From this, the Black–Litterman method computes the desired (mean-variance efficient) asset allocation
        - Grinold and Kahn's approach: optimizing factor portfolios
            - builds factor portfolios, which are portfolios based on a signal alpha signal and usually rule based (e.g. one growth portfolio, one value portfolio, one momentum portfolio...)
            - each factor portfolio is then treated as an instrument and fed to the optimizer
        - resampled efficiency
            - uses monte carlo simulation to create alternate histories and alternative efficient frontiers, then frontiers can be averaged to create a resampled efficient frontier
            - adresses oversensitivity to estimation errors in expected alpha, volatility, and correlation
            - thought to produce more robust predictions
        - data mining approaches to optimization
            - machine learning techniques such as supervised learning or genetic algorithms
    - how quants choose a portfolio construction model
        - Most quants using rule based portfolio construction are also using intrinsic alpha models (as opposed to relative), and most of these are futures traders.
        - Most quants using optimizers are focused on relative alpha approaches (often equity market neutral strategies)

## Chapter 7. Execution
- 3 ways to get execution algorithm:
    - build
    - buy from broker
    - 3rd party software
- Quants sometimes utilize portfolio bidding services from brokers where they bid on a "blind" portfolio described only by its characteristics.
- types of orders:
    - market
        - quick execution
        - price varies
    - limit
        - execution time varies
        - price fixed
- limit order book - collection/queue of limit orders to buy and sell (better price = higher priority)
- Market orders are aggressive while limit orders vary in levels of aggression spectrum.
    - A limit order crossing the spread is more aggressive.
- Passive orders get better transaction price (if filled) and also usually get rebate from exchange for providing liquidity.
    - Market orders "take" liquidity.
- Momentum alpha strategies favor aggressive orders.
- Mean reversion alpha strategies favor passive orders.
- Stronger alpha signals favor aggressive orders.
- A middle ground beteween passive and agressive order would be putting a limit order in the middle of the spread.
- Large orders are often chunked into smaller orders and spread out over time.
- Hidden orders exist but will lose priority in queue to equivalent visible order
    - Not all exchanges allow hidden orders
- iceberging - execution strategy theat hides most of a large order but leaves part of it visible
- Some markets have several pools of liquidity for the same instrument.
- smart order routing - determines which pool of liquidity is best to send order at any given moment
- Rapid placement and cancelling of large orders is sometimes used to test the markets reaction to changing depth in the order book or to manipulate perceptions
- High frequency trading focuses on micro structure alphas which focus on liquidity patterns in the order book
    - HFT strategies require heavy investment in infrastructure and research while being limited in how much money they can manage (due to market impact).
    - HFT strategies often sound like a cutting edge computer game with names like guerilla, sniper, shark
    - HFT can use 
- Most quants use direct market access (DMA) to conduct trades.
- Colocation and sponsored access are also available but are mostly used for HFT
- financial information exchange protocol (FIX) engines can be bought or built, and are often custom built by quants for optimal speed
- Quants have choice to build or buy hardware and software such as orderer management systems, extant hardware, and third party execution software.
- "Most quants use either Linux or UNIX operating systems because they are more efficient and therefore provide better computing performance than a PC/Windows configuration."

## Chapter 8. Data
- Data reaches black box through data servers which are connected to data sources
    - Data servers use data feed handlers
- The best firms collect data from primary sources rather than from vendors
- Price data includes price, volume, indicies, and order book
- Price data strategies are usually faster than fundamental data strategies.
- primary sources of data:
    - exchanges
    - regulators
    - governments
    - corporations
    - news agencies
    - proprietary data vendors
- Primary sources usually cost more but provide more control over data cleaning and speed.
- data cleaning techniques/issues:
    - spike filters
    - handling splits and dividends
    - incorrect timestamps
    - look ahead bias from asynchronous data (e.g. using end of of quarter reports at end of quarter when they aren't acutally published until several weeks after end of quarter. Also failing to account for different closing times of different markets)
- data storage options:
    - flat files
    - relational database
        - data cube

## Chapter 9. Research
- Well behaved quants adhere to the scientific method which forces rogor and discipline.
- Process:
    1. observe
    2. hypothesize
    3. deduce consequences of hypothesss
    4. seek to disprove hypothesis (based on deductions from step 3)
- falsification - a theory that has not yet been disproved can be accepted as true for the moment, but we can never be certain that the next observation we make of the theory will not falsify it
- A key difference between markets and natural sciences is that nature is relatively stable while markets are not.
- sources of idea generation:
    - market observations
    - academic literature
    - discretionary traders
    - migration - ideas from other quant shops
- "First, build a model and train it on some subset of the data available (the *in-sample period*). Then test it on another subset of the data to see if it is profitable (the *out-of-sample period*)."
- when constructing an in-sample, a quant must consider
    - breadth - how many stocks to include and which ones
    - length - length of time used for fitting the model
- A wide variety of metrics are used to determine the "goodness" of a model
    - equity risk premium
    - average rate of return
    - variability of returns over time
        - standard deviation
        - lumpiness
    - worst peak tovalley drawdowns
    - r squared
    - quantile bracketing
    - percentage of winning trades or time periods
    - risk adjusted return
        - Sharpe ratio
        - Sterling ratio
        - Omega ratio
        - Calmar ratio
    - relationships with other strategies
        - correlation
        - Do portfolio results improve or deteriorate with new strategy, i.e. Is the new strategy synergistic with the existing strategies?
    - time decay
        - Testing what returns would be if trades lagged behind signals can give insight into how crowded the strategy is.
    - sensitivity to specific parameters (tests overfitting)
    - number of assumptions (fewer is better, occam's razor)
- out of sample testing considerations
    - rolling window vs growing window
    - burning data
    - researchers already knowing characteristics of out of sample data (e.g. being aware of internet bubble in out of sample data)
- Transaction costs and availability of short positions must also be considered when testing.

## Chapter 10. Risks Inherent to Quant Strategies
- model risk - "the risk that the strategy does not accurately describe, match, or predict the real-world phenomenon it is attempting to expliot"
    - inapplicability of modeling
        - choosing the wrong problem model
        - misapplication of valid techniques (e.g. using techniques that assume normality when data actually has fat tails)
    - model misspecification
    - implementation errors (programming errors)
- regime change risk - risk of structural shift in market that would cause its behavior and relationships to change dramatically
- exogenous shock risk - risk of change that is driven by information not internal to the market (can't be predicted)
- contagion risk - risk of strategy becoming crowded
- how quants monitor risk
    - exposure tools
    - profit and loss monitors
    - execution monitoring tools
    - hit rate
    
## Chapter 11. Criticisms of Quant Trading
- Trading is an art not a science and human behavior can't be modeled
    - Over time, human behavior can be predicted enough to be profitable
- Quants cause more market volatility by underestimating risk.
    - Decision makers in every field underestimate risk
- Quants cannot handle unusual events or rapid changes in market conditions.
    - generally a valid criticism however some quant strategies are designed to profit from short reversals of longer-term trends
- Quants are all the same.
    - correlation in quant return data is actually pretty low
- Only a few large quants can survive in the long run
    - managing large amounts of money can be a disadvantage in times of stress
    - managing large amounts of money makes many appealing strategies impossible
    - smaller funds can specialize while larger funds diversify
- Quants are guilty of data mining.
    - Most quants are theory driven.
    - Data mining can be successful.
    
## Chapter 12. Evaluating Quants and Quant Strategies
- You should seek to both understand the strategy and evaulate the practitioners.
- gathering information
    - build trust
        - don't ask for sensitive information
        - don't share what other quants do
    - display knowledge of possible strategies (menu of options)
    - keep information organized once gathered
- 6 investment process components to consider when evaluating quant strategy:
    1. research and strategy development
        - How do you come up with new ideas for trading strategies?
        - How do you test these ideas?
        - What kinds of things are you looking for to determine whether a strategy works or not?
    2. data sourcing, gathering, cleaning, and management
        - What data are you using?
        How do you store the data, and why that way?
        - How do you clean the data?
    3. investment selection and structuring
        - Are your alpha models theory driven or data driven?
        - Which alpha strategies are you using (e.e., trend, reversion, value/yield, growth, or quality)?
        - Are you making relative bets or a bunch of individual bets?
        - If relative, what does relative mean, exactly?
        - Over what time horizon, and in what investment universe?
        - How are you mixing your various alpha models?
    4. portfolio construction
        - How do you do portfolio construction?
        - What are your limits, and why did you set them there?
        - What are the inputs to your portfolio construction?
        - What areyou trying to achieve with portfolio construction (i.e., what is your "objective function")?
    5. execution
        - What kind of transaction cost model are you using, and why did you choose to model transaction costs the way you did?
        - How are you executing trades--manually or algorithmically?
        - Tell me about your order executioin algorithms: What kinds of things did you build into them (e.g., hidden vs. visible, or active v. passive)?
    6. risk management and monitoring
        - What does your risk model account for, and why those things?
        - What are your various risk limits, and why did you set them where you did?
        - Under what circumstances would you ever intervene with your model?
        - What are you monitoring on an ongoing basis?
- evaluating the accumen of quantitative traders
    - do at least some members have live experience
    - attitude should be cautious and humble
    - should be able to dig deep into details with you in a few areas
- Where does their edge come from and how sustainable is it?
    - edge must come from one of 6 components of investment process
    - data edge
        - proprietary access
        - superior gathering, cleaning, or storage techniques
        - lack-of-competition edge
    - structural edge - relates to something in the market strucutre that puts the wind in the sails of a market participant (usually caused and removed by regulation)