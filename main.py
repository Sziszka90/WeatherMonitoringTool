# Weather API
import queryData
import processData


data, dataToPlot = queryData.queryFromAPI()
processData.createFile(data)
processData.createPlot(dataToPlot)
print(data)


