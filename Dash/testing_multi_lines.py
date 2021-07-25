dates <- seq(from = as.Date("2004-01-01"), to = as.Date("2020-12-31"), by = 12)
dt.allDataFvsS <- data.frame(date = dates, meanDifference = seq_along(dates))

v.years <- as.Date(c("2004-01-01", "2005-01-01", "2006-01-01", "2007-01-01", "2008-01-01", "2009-01-01",
                     "2010-01-01", "2011-01-01", "2012-01-01", "2013-01-01", "2014-01-01", "2015-01-01",
                     "2016-01-01", "2017-01-01", "2018-01-01", "2019-01-01", "2020-01-01", "2021-01-01"))
df.dateYears <- as.data.frame(v.years)


p <- plot_ly(dt.allDataFvsS, x = dt.allDataFvsS$date, y = dt.allDataFvsS$meanDifference, mode = 'lines',
             type = 'scatter', line = list(color = "#007d3c"), text = ~"forwardProduct", 
             hovertemplate = paste("<b>%{text} vs. Spot</b><br>", "%{xaxis.title.text}:  %{x}<br>",
                                   "%{yaxis.title.text}:  %{y}<br><extra></extra>")) %>%
  add_trace(x = as.Date("2018-10-01"), type = 'scatter', mode = 'lines',
            line = list(color = "red", dash = "dash"), text = "Price Zone Separation",
            hovertemplate = paste("<b>%{text}</b><br>", "%{xaxis.title.text}:  %{x}<br><extra></extra>")) %>%
  layout(title = "Average Price Difference Forward vs. Spot", xaxis = list(title = "Date"), 
         yaxis = list(title = "EUR/MWh"), showlegend = FALSE)


for(v.year in df.dateYears$v.years){
  p <- add_trace(p, x = as.Date(v.year, origin = "1970-01-01"), type = 'scatter', mode = 'lines',
            line = list(color = "red", dash = "dash"), text = "Price Zone Separation",
            hovertemplate = paste("<b>%{text}</b><br>", "%{xaxis.title.text}:  %{x}<br><extra></extra>"))
}

p