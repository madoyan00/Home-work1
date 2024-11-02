import requests

def getProducts():
    try:
      apiUrl = "https://fakestoreapi.com/products"
      response = requests.get(apiUrl)

      if response.status_code == 200:
         return response.json()
      else:
         return f"Error {response.status_code}: Page not found"
    except requests.exceptions.HTTPError as http_err:
      print(f"HTTP ERROR: {http_err}")
    except  requests.exceptions.ConnectionError as con_err:
       print(f"CONNECTIO ERROR: {con_err}")
    except Exception as ex:
       print(f"SOmething wronf: {ex}")


def parseDAta():
  products =  getProducts()
#   ნაწილი ა
  yashig = []
  sum = 0
  for product in products:
      yashig.append(product["price"])
      sum += product["price"]
  sumKes = sum / len(yashig)
  print("A")
  print(188 * "=")
  print(f"min = {min(yashig)}")
  print(188 * "-")
  print(f"max = {max(yashig)}")
  print(188 * "-")
  print(f"average = {sumKes}")
  print(188 * "=")

# ნაწილი ბ
  productCategory = set()
  for product in products:
     productCategory.add(product["category"])
  sort = sorted(productCategory)
  print("B")
  print(188 * "=")
  print(productCategory)
  print(188 * "-")
  print(sort)
  print(188 * "=")

#   ნაწილი გ
  list1 = []
  
  for product in products:
   list1.append({"title": product["title"], "id" : product["id"]})
   sortedList1 = sorted(list1, key=lambda x: x["title"])
  print("C")
  print(188 * "=")
  print(list1)
  print(188 * "-")
  print(sortedList1)
  print(188 * "=")

#   ნაწილი დ

  rateList = []
  for product in products:
    rateList.append(product["rating"]["rate"])
    sortedRateList = sorted(rateList)
  print("D")
  print(188 * "=")
  print(rateList)
  print(188 * "-")
  print(sortedRateList)
  print(188 * "=")
parseDAta()