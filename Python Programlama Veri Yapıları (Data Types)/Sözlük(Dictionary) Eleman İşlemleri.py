#Sozluk Eleman İşlemleri

sozluk = {"REG" : "Regresyon Modeli",
          "LOJ" : "Lojistik Regresyon",
          "CART" : "Classification and Reg"}

sozluk[0]

sozluk["REG"]
sozluk["LOJ"]

sozluk = {"REG" : ["RMSE",10],
          "LOJ" : ["MSE",20],
          "CART" : ["SSE",30]}

sozluk["REG"]

sozluk = {"REG" : {"RMSE" : 10,
                   "MSE" : 20,
                   "SSE" : 30},
          
          "LOJ" : {"RMSE" : 10,
                   "MSE" : 20,
                   "SSE" : 30},
          
          "CART" : {"RMSE" : 10,
                    "MSE" : 20,
                    "SSE" : 30}}

sozluk
sozluk["REG"]["SSE"]
