################################################################################
# prep
################################################################################
rm(list=ls()) 
# load packages
library(plot0) 
library(geiger)
# set output path
res_dir <- paste0(getwd(), '/results/')

################################################################################
# figure 1a 
################################################################################
# load -------------------------------------------------------------------------
filepath <- paste0(getwd(), '/data/data_new.csv')
filename <- 'data_new.csv'
dt <- read.csv(filepath)

data_black <- subset(dt, race == 'black', select=c('risk_score_t', 'gagne_sum_t'))

plot(data_black, x='risk_score_t', y='gagne_sum_t')

# compute ----------------------------------------------------------------------
df <- MyComputePlotDF(dt, 
                      col.to.y = 'gagne_sum_t',
                      col.to.cut = 'risk_score_t',
                      col.to.groupby = 'race',
                      nquantiles = 10,
                      ci.level = 0.95)

plot(col.to.y, col.to.cut)