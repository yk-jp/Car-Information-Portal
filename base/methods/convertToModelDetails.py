
def convertToModelDetails(modelDetailsData):
    modelDetails = []
    for modelDetailData in modelDetailsData:
            modelDetail = {
                'model_year':modelDetailData.get('model_year'),
                'model_name':modelDetailData.get('model_name'),
                'model_engine_power_ps':modelDetailData.get('model_engine_power_ps')
            } 
            if modelDetail not in modelDetails:
                 modelDetails.append(modelDetail)
            
    return modelDetails