import pickle
import os
import time
class Guest:
	userFileName = "UserList.pickle"
	productsListName = "ProductList.pickle"
	def __init__(self):
		pass

	def GetRegistered(self):
		print("\nRegister yourself to purchase products.")
		if os.path.exists(Guest.userFileName):
			filepointer = open(Guest.userFileName,"rb") 
			if(filepointer):
				UserDetail = pickle.load(filepointer)
				filepointer.close()
				HighestId = sum(len(users) for users in UserDetail.values())
				self.UserId = int(HighestId / 4) + 1
				self.UserName = input("Enter Your Name: ")
				self.UserPhone = input("Enter Your Contact No: ")
				self.UserAdd = input("Enter Your Address: ")
				self.Password = input("Enter Your Password: ")
				  
				UserData =	str(self.UserName) + ":" + str(self.UserPhone) + \
								":" + str(self.UserAdd) + ":" + str(self.Password)

				UserDetail[self.UserId] = UserData.split(':')
				with open(Guest.userFileName,'wb') as filepointer:
					pickle.dump(UserDetail, filepointer)
					filepointer.close()
				print("Registered Successfully!")
				print("Your user Id is: ",self.UserId)
		else:
			print("Something went wrong!")

	def ViewProducts(self):
		if os.path.exists(Guest.productsListName):
			with open(Guest.productsListName,"rb") as filepointer:
				if(filepointer):
					ShowProducts = pickle.load(filepointer)
					filepointer.close()
				print("Products:")
				for item in ShowProducts:
					print(str(item) + ". " + str(ShowProducts[item][0]) + "\t\tRs" +
						str(ShowProducts[item][1]) + "\t\t" + str(ShowProducts[item][2]))
		else:
			print("Products are not Available!")

		

class Admin(Guest):
	adminLogin = None
	ProductId = None
	FileName = "ProductList.pickle"
	def __init__():
		self.ProductName = None
		self.ProductPieces = None
		self.ProductPrice = None

	def MarkShipment(self):
		pass
	def ConfirmDelivery(self):
		pass
		
	def AddProducts(self):
		filepointer = open(Admin.FileName,"rb")
		if(filepointer):
			ProductsList = pickle.load(filepointer)
			filepointer.close()
			print(ProductsList)
			HighestId = sum(len(products) for products in ProductsList.values())
			self.ProductId = int(HighestId / 3) + 1
			self.ProductName = input("Enter Product Name:")
			self.ProductPrice = input("Enter Product Price:")
			self.ProductPieces = input("Enter Quantity Available:")

			ProductDetail =	str(self.ProductName) + ":" + str(self.ProductPrice) + ":" + str(self.ProductPieces) 
			ProductsList[self.ProductId] = ProductDetail.split(':')

			with open(Admin.FileName,'wb') as filepointer:
				pickle.dump(ProductsList, filepointer)
				filepointer.close()
			print("Product Added!!")

	def DeleteProducts(self,ProductId):
		self.ProductId = int(ProductId)
		if os.path.exists(Admin.FileName):
			filepointer = open(Admin.FileName, "rb") 
			if(filepointer):
				ProductsList = pickle.load(filepointer)
				filepointer.close()
				if(int(self.ProductId) in ProductsList):
					del ProductsList[self.ProductId]
					with open(Admin.FileName, "wb") as filepointer:
						pickle.dump(ProductsList, filepointer)
						filepointer.close()
					print("Delete Product Successfully!")
				else:
					print("Invalid Product Id!")	
		else:
			print("File not present")


	def ModifyProducts(self,ProductId):
		self.ProductId = int(ProductId)
		if os.path.exists(Admin.FileName):
			filepointer = open(Admin.FileName, "rb") 
			if(filepointer):
				ProductsList = pickle.load(filepointer)
				filepointer.close()
				if(self.ProductId in ProductsList):
					ProductsList[self.ProductId][0] = input("Enter Product Name:")
					ProductsList[self.ProductId][1] = input("Enter Product Price:")
					ProductsList[self.ProductId][2] = input("Enter Product Quantity Available:")
					with open(Admin.FileName,'wb') as filepointer:
						pickle.dump(ProductsList, filepointer)
						filepointer.close()
					print("Product Modified!!")
			else:
				print("Invalid Input!")
		else:
			print("File doesn't exists!")
		

class Payment:
	def __init__():
		CustId
		CustName
		CardType
		CardNo

class Customer (Guest, Payment):
	ProductFileName = "ProductList.pickle"
	CustomerPass = None
	CustomerId = None
	CustomerLogin = None
	CustomerName = None
	NoOfProducts = 0
	Products = {}
	Total = 0
	def __init__(self):
		pass

	def BuyProducts(self):
		pass
	def MakePayment(self):
		pass
	def AddToCart(self, arg1):
		added = True
		ProductId = int(arg1)
		if(ProductId in self.Products):
			temp = int(self.Products[ProductId][2])
			if(temp < int(self.Products[ProductId][3])):
				oldprice = int(self.Products[ProductId][1])
				price = str(int(oldprice*(temp+1)/temp))
				self.Products[ProductId][1] = price
				quand = str(1 + int(self.Products[ProductId][2]))
				self.Products[ProductId][2] = quand
				self.Total += (int(price) - int(oldprice))
			else:
				print('Quantity exceeded')
				added = False
		else:
			if os.path.exists(Customer.ProductFileName):
				filepointer = open(Customer.ProductFileName, "rb") 
				ProductsList = pickle.load(filepointer)
				filepointer.close()
				if(ProductId in ProductsList):
					Productkeyvalue = ProductsList[ProductId][0] + ":" + \
										ProductsList[ProductId][1] + ":1:" + ProductsList[ProductId][2]
					self.Products[ProductId] = Productkeyvalue.split(':')
					self.Total += int(ProductsList[ProductId][1])
				else:
					print('Product not there')
					added = False
		if(added):
			self.NoOfProducts += 1
			print("Product", ProductId, "added into cart!")
		

	def ViewCart(self):
		for item in self.Products:	
			print(self.Products[item][0]+'\tRs.'+self.Products[item][1]+'\t'+self.Products[item][2])
		print("Total: Rs"+str(self.Total))
		# print(self.Products)

	def DeleteFromCart(self, arg1):
		ProductId = int(arg1)
		if(ProductId in self.Products):
			del self.Products[ProductId] 
			print("Product", ProductId, "removed!")
		else:
			print("Invalid Product Id!")



class Login (Admin, Customer):
	userFileName = "UserList.pickle"
	def __init__(self, LoginAs):
		Admin.adminLogin = False
		Customer.CustomerLogin = False
		self.UserId = input("Enter UserId: ")
		self.Password = input("Enter Password: ")

		if(LoginAs == 1):
			if(str(self.UserId) == "2357" and str(self.Password) == "tayal"):
				Admin.adminLogin = True
				print("Username: Admin")
			else:
				print("Wrong Credential. Try Again!")

		if(LoginAs == 2):	
			if os.path.exists(Login.userFileName):
				filepointer = open(Login.userFileName, "rb") 
				UserList = pickle.load(filepointer)
				filepointer.close()

			if(int(self.UserId) in UserList):
				if(self.Password == UserList[int(self.UserId)][-1]):
					Customer.CustomerLogin = True
					Customer.CustomerId = self.UserId
					Customer.CustomerName = UserList[int(self.UserId)][0]
					print("Username:",Customer.CustomerName)
				else:
					print("Invalid Password!")
			else:
				print("Invalid User Id!")

			

	def __del__(self):
		print("Logout Successfully!")

	        	

def main():
	while(1):
		print("\033c", end="")
		print("\t\t\t\tWelcome to AllMart\t\t\t", end = "")
		start = input("\nLogin as\n1.Admin\n2.Customer\n3.Guest\n")
		if(start == '1'):
			adminObject = Login(1)
			if(Admin.adminLogin == True):
				print("Login Successfully!")
				adminObject.ViewProducts()
				while(1):
					print("\n1. Add Products\n2. Modify Products\n3. Delete Products\n4. View Products\n5. Exit\nOperation: ")
					op_task = input()
					if(op_task == "1"):
						adminObject.AddProducts()
					elif(op_task == "2"):
						adminObject.ModifyProducts(input("Enter Product Id:"))
					elif(op_task == "3"):
						adminObject.DeleteProducts(input("Enter Product Id:"))
					elif(op_task == "4"):
						adminObject.ViewProducts()
					elif(op_task == "5"):
						exit(0)
					else:
						print("Invalid Input!")
			else:
				print("Try Again!")
				time.sleep(1)

		elif(start == '2' or start == '3'):
			if(start == '3'):
				GuestObject = Guest()
				print("\nYou are entered as Guest!")
				GuestObject.ViewProducts()
				is_user = input("\n1.Register\n2.Login\n")
				if(is_user == '1'):
					GuestObject.GetRegistered()
			
			userObject = Login(2)
			if(Customer.CustomerLogin == True):
				print("Login Successfully!")
				userObject.ViewProducts()
				while(1):
					print("\n1. Add Into Cart\n2. View Cart\n3. Delete From Card\n4. Buy Products\n5. View Products\n6. Exit\nOperation: ")
					op_task = input()
					if(op_task == "1"):
						userObject.AddToCart(input("Enter Product Id:"))
					elif(op_task == "2"):
						userObject.ViewCart()
					elif(op_task == "3"):
						userObject.DeleteFromCart(input("Enter Product Id:"))
					elif(op_task == "4"):
						userObject.BuyProducts()
					elif(op_task == "5"):
						userObject.ViewProducts()
					elif(op_task == "6"):
						exit(0)
					else:
						print("Invalid Input!")

			else:
				print("Try Again!")
				time.sleep(1)

		else:
			print("Invalid Input!")
			time.sleep(1)

if __name__ == '__main__':
    main() 