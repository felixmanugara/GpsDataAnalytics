from distutils.log import error
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math
from scipy import stats

""""
def table():
    # create dataframe from .csv
    data = pd.read_csv('gpsdat.csv',engine='python', parse_dates=['Dates'])
    dataset = pd.DataFrame(data, index= range(1,len(data)))
    # cleaning data from duplicate values
    dataset = dataset.drop_duplicates(subset=['Latitude modul','Longitude modul','Sat count','Speed','Alt'],keep=False, inplace= False)
    dataset.index = range(1, len(dataset)+1)
    
    return dataset

dataset = table()

def koordinat_GPS(df):
    np_gps_arr = pd.DataFrame(df).loc[:,['Latitude modul','Longitude modul']].to_numpy(dtype=np.float32)
    #print(np_gps_arr)
    np_ref_arr = np.array([-5.3721512,105.2500960]) 
    #print(np_ref_arr)
    
    return np_gps_arr, np_ref_arr
    
np_gps_arr, np_ref_arr = koordinat_GPS(table())


# euclidean distance formula
def counting_process(gps_data,ref_data):
    data_count = np.linalg.norm(gps_data - ref_data, axis=1)    
    return data_count

# loop for storing calculation result
def store_data(data_counted):
    new_arr = []
    for i in data_counted:
        result = i * 111.322
        km = result * 1000
        m = round(km,2)
        new_arr.append(m)

    np_new_arr = np.array(new_arr)
    #print(np_new_arr)
    return np_new_arr

data_stored = store_data(counting_process(np_gps_arr, np_ref_arr))

average = stats.mode(data_stored)[0] # mencari nilai rata-rata
#average_value = (f"jarak error rata-rata adalah: {average} Meter")
#print(average_value)

def dataset():
    reference_coordinate = pd.DataFrame(np_ref_arr.reshape(1,2),columns=['Latitude ref','Longitude ref'])
    reference_coordinate.index = range(1,len(reference_coordinate)+1) # index using data length
    error_distance_data = pd.DataFrame(np.array(data_stored),columns=['Error Distance (m)'],index=range(1,len(data_stored)+1))
    merge_data = pd.concat([reference_coordinate,table(),error_distance_data],axis=1)
    df = merge_data.fillna(method='ffill')
    df.drop(columns='Dates')
   #df.head(10)

    return error_distance_data, df

error_distance_data, df = dataset()

def data_plot(source):
    min_val = error_distance_data.min()
    max_val = error_distance_data.max()
    bins = math.ceil((max_val - min_val) / 3)
    xlab = 'Nilai Error Dalam Meter'
    ylab = 'Jumlah Data'
    color = '#ff7f50'

    # plot customizations
    plt.title("Selisih Jarak Error GPS")
    plt.xlabel(xlab)
    plt.ylabel(ylab)

    plt.hist(source,bins=bins,edgecolor="black", alpha=0.8)
    plt.axvline(average,color=color,label='Nilai rata-rata',linewidth=2)
    plt.grid(color='grey',alpha=0.4)
    plt.legend(loc='best')
    plt.show()
                        
data_plot(data_stored) 
print(df)

"""

class GpsDataAnalytics:

    def __init__(self, GPSData):
        self.data = pd.read_csv(GPSData, engine='python', parse_dates=['Dates'])
        self.dataset = pd.DataFrame(self.data, index= range(1,len(self.data)))
        self.dataset.drop_duplicates(subset=['Latitude modul','Longitude modul','Sat count','Speed','Alt'], keep= False,inplace= True)
        self.dataset.index = range(1, len(self.dataset)+1)
        #print(dataset)

    def extractData(self):
        self.npGpsModuleArray = pd.DataFrame(self.dataset).loc[:,['Latitude modul','Longitude modul']].to_numpy(dtype=np.float32)
        self.npGpsReferenceArray = np.array([-5.3721512,105.2500960])
        #print(self.npGpsModuleArray)
        #print(self.npGpsReferenceArray)
    
    def countingProcess(self):
        self.dataProc = np.linalg.norm(self.npGpsModuleArray - self.npGpsReferenceArray, axis=1)
        #print(self.dataProc)

    def dataResult(self):
        resultArray = []
        for i in self.dataProc:
            multiplication = i * 111.322
            km = multiplication * 1000
            m = round(km, 2)
            resultArray.append(m)

        self.resultArrayData = np.array(resultArray)
        #print(self.resultArrayData)
    
    def finalDataTable(self):
        referenceCoordinate = pd.DataFrame(self.npGpsReferenceArray.reshape(1,2),columns=['Latitude Referensi','Longitude Referensi'])
        referenceCoordinate.index= range(1,len(referenceCoordinate)+1)
        # index using data length
        self.errorDistanceData = pd.DataFrame(self.resultArrayData, columns=['Jarak Error (Meter)'], index= range(1,len(self.resultArrayData)+1))
        mergeData = pd.concat([referenceCoordinate,self.dataset,self.errorDistanceData], axis=1)
        finalDataset = mergeData.fillna(method='ffill') # fill missing value 
        finalDataset.drop(columns=['Sat count','Speed','Dates','Alt'], inplace=True)
        #print(finalDataset.head(10))
    
    def dataPlot(self):
        minVal = self.errorDistanceData.min()
        maxVal = self.errorDistanceData.max()
        average = np.median(self.resultArrayData)
        binCount = math.ceil((maxVal - minVal) / 3)
        xLabel = "Nilai error dalam Meter"
        yLabel = "Jumlah Data"
        color = "#ff7f50"

        #plot customizations
        plt.title("Selisih Jarak Error GPS")
        plt.xlabel(xLabel)
        plt.ylabel(yLabel)

        plt.hist(self.resultArrayData,bins=binCount,edgecolor="black", alpha=0.8)
        plt.axvline(average,color=color,label='Nilai rata-rata',linewidth=2)
        plt.grid(color='grey',alpha=0.4)
        plt.legend(loc='best')
        plt.show()



Analytics = GpsDataAnalytics('gpsdat.csv')
Analytics.extractData()
Analytics.countingProcess()
Analytics.dataResult()
Analytics.finalDataTable()
Analytics.dataPlot()