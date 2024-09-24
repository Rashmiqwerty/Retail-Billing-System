from tkinter import *
from tkinter import messagebox
import random,os,tempfile,smtplib
from excelconvert import save_to_excel

#functionalitypart
billnumber = random.randint(500, 1000)
def clear():
    bathsoapEntry.delete(0,END)
    facecreamEntry.delete(0,END)
    hairgelEntry.delete(0,END)
    hairsprayEntry.delete(0,END)
    bodylotionEntry.delete(0,END)
    facewashEntry.delete(0,END)

    riceEntry.delete(0,END)
    oilEntry.delete(0,END)
    daalEntry.delete(0,END)
    WheatEntry.delete(0,END)
    sugarEntry.delete(0,END)
    teaEntry.delete(0,END)

    MaazaEntry.delete(0,END)
    PepsiEntry.delete(0,END)
    SpriteEntry.delete(0,END)
    DewEntry.delete(0,END)
    FrootiEntry.delete(0,END)
    CococolaEntry.delete(0,END)

    bathsoapEntry.insert(0,0)
    facecreamEntry.insert(0,0)
    hairgelEntry.insert(0,0)
    hairsprayEntry.insert(0,0)
    bodylotionEntry.insert(0,0)
    facewashEntry.insert(0,0)

    riceEntry.insert(0,0)
    oilEntry.insert(0,0)
    daalEntry.insert(0,0)
    WheatEntry.insert(0,0)
    sugarEntry.insert(0,0)
    teaEntry.insert(0,0)

    MaazaEntry.insert(0,0)
    PepsiEntry.insert(0,0)
    SpriteEntry.insert(0,0)
    DewEntry.insert(0,0)
    FrootiEntry.insert(0,0)
    CococolaEntry.insert(0,0)

    cosmeticpriceEntry.delete(0,END)
    grocerypriceEntry.delete(0,END)
    colddrinkspriceEntry.delete(0,END)

    cosmetictaxEntry.delete(0,END)
    grocerytaxEntry.delete(0,END)
    colddrinkstaxEntry.delete(0,END)

    nameEntry.delete(0,END)
    phoneEntry.delete(0,END)
    billnumberEntry.delete(0,END)

    textarea.delete(1.0,END)

def send_email():
    def send_gmail():
        try:
            ob = smtplib.SMTP('smpt.gmail.com', 587)
            ob.starttls()  # help to establish a secure connection
            ob.login(senderEntry.get(), passwordEntry.get())
            message = email_textarea.get(1.0, END)
            ob.sendmail(senderEntry.get(), recieverEntry.get(), message)
            ob.quit()
            messagebox.showinfo('Success', 'Bill is Successfully sent.',parent=root1)
            root1.destroy()  # destroy means top level window will close
        except:
            messagebox.showerror('Error', 'Something went wrong please try again.',parent=root1)
    if textarea.get(1.0,END)=='\n':
        messagebox.showerror('Error','Bill is Empty')
    else:
        root1=Toplevel()
        #disable previous window means user will not able to do any operation in previous window until top window is not close.
        root1.grab_set()
        root1.title('Send Email')
        root1.config(bg='gray20')
        root1.resizable(0,0) # user not able to resize the window

        senderFrame=LabelFrame(root1,text='SENDER',font=('arial',16,'bold'),bd=6,bg='gray20',fg='white')
        senderFrame.grid(row=0,column=0,padx=40,pady=20)

        senderLabel=Label(senderFrame,text="Sender's Email",font=('arial',14,'bold'),bd=6,bg='gray20',fg='white')
        senderLabel.grid(row=0,column=0,padx=10,pady=8)

        senderEntry=Entry(senderFrame,font=('arial',14,'bold'),bd=2,width=23,relief=RIDGE)
        senderEntry.grid(row=0,column=1,padx=10,pady=8)

        passwordLabel= Label(senderFrame, text="Password", font=('arial', 14, 'bold'), bd=6, bg='gray20',
                                 fg='white')
        passwordLabel.grid(row=1, column=0, padx=10, pady=8)

        passwordEntry = Entry(senderFrame, font=('arial', 14, 'bold'), bd=2, width=23, relief=RIDGE)
        passwordEntry.grid(row=1, column=1, padx=10, pady=8)

        recipientFrame = LabelFrame(root1, text='RECIPIENT', font=('arial', 16, 'bold'), bd=6, bg='gray20', fg='white')
        recipientFrame.grid(row=1, column=0, padx=40, pady=20)

        recieverLabel = Label(recipientFrame, text="Email Address", font=('arial', 14, 'bold'), bd=6, bg='gray20',fg='white')
        recieverLabel.grid(row=0, column=0, padx=10, pady=8)
        recieverEntry = Entry(recipientFrame, font=('arial', 14, 'bold'), bd=2, width=23, relief=RIDGE)
        recieverEntry.grid(row=0, column=1, padx=10, pady=8)

        messageLabel = Label(recipientFrame, text="Email Address", font=('arial', 14, 'bold'), bd=6, bg='gray20',fg='white')
        messageLabel.grid(row=1, column=0, padx=10, pady=8)

        email_textarea=Text(recipientFrame,font=('arial', 14, 'bold'),bd=2,relief=SUNKEN,width=42,height=11)
        email_textarea.grid(row=2,column=0,columnspan=2)
        email_textarea.delete(1.0,END)
        email_textarea.insert(END,textarea.get(1.0,END).replace('=','').replace('-','').replace('\t\t\t','\t\t'))

        sendButton=Button(root1,text='SEND',font=('arial', 16, 'bold'),width=15,command=send_gmail)
        sendButton.grid(row=2,column=0,pady=20)

        root1.mainloop()

def print_bill():
    #check textarea is empty or not . if it is ==\n then it is empty.
    if textarea.get(1.0,END)=='\n':
        messagebox.showerror('Error','Bill is Empty')
    else:
        #tempfile is use to create temporary file . inbuilt given
        file=tempfile.mktemp('.txt')
        open(file,'w').write(textarea.get(1.0,END))
        os.startfile(file,'print') #print file in the window

def search_bill():
    for i in os.listdir('bills/'):
        if i.split('.')[0]==billnumberEntry.get():
            f=open(f'bills/{i}','r')
            textarea.delete('1.0',END)
            for data in f:
                textarea.insert(END,data)
            f.close()
            break
    else:
        messagebox.showerror('Error','Invalid Bill Number')


if not os.path.exists('bills'):
    os.mkdir('bills')

def save_bill():
    global billnumber
    result=messagebox.askyesno('Confirm','Do you want to save the bill?')
    if result:
        bill_content=textarea.get(1.0,END)
        file=open(f'bills/{billnumber}.txt','w')
        file.write(bill_content)
        file.close()
        messagebox.showinfo('Success',f'Bill Number {billnumber} is saved successfully')
        billnumber=random.randint(500,1000)

def bill():
    textarea.delete(1.0,END)
    if(nameEntry.get()=='' or phoneEntry.get()==''):
       messagebox.showerror('Error','Customer Details are Required')
    elif cosmeticpriceEntry.get()=='' and grocerypriceEntry.get()=='' and colddrinkspriceEntry.get()=='':
        messagebox.showerror('Error','No Products are selected')
    elif cosmeticpriceEntry.get()=='Rs 0' and grocerypriceEntry.get()=='Rs 0' and colddrinkspriceEntry.get()=='Rs 0':
        messagebox.showerror('Error','No product selected')
    else:
        textarea.insert(END,'\t\t**Welcome Customer**\n')
        textarea.insert(END,f'\nBill Number: {billnumber}')
        textarea.insert(END,f'\nCustomer Name:{nameEntry.get()}')
        textarea.insert(END,f'\nCustomer Phone Number:{phoneEntry.get()}')
        textarea.insert(END,f'\n======================================================')
        textarea.insert(END,'\nproduct\t\t\tQuantity\t\t\tPrice')
        textarea.insert(END,f'\n======================================================')
        if bathsoapEntry.get()!='0':
            textarea.insert(END,f'\nBath Soap:\t\t\t{bathsoapEntry.get()}\t\t\t{soapprice} Rs')
        if hairsprayEntry.get()!='0':
            textarea.insert(END,f'\nHair Spray:\t\t\t{hairsprayEntry.get()}\t\t\t{hairsprayprice} Rs')
        if hairgelEntry.get()!='0':
            textarea.insert(END,f'\nHair Gel:\t\t\t{hairgelEntry.get()}\t\t\t{hairgelprice} Rs')
        if bodylotionEntry.get()!='0':
            textarea.insert(END,f'\nBody Loction:\t\t\t{bodylotionEntry.get()}\t\t\t{bodylotionprice} Rs')
        if facecreamEntry.get()!='0':
            textarea.insert(END,f'\nFace Cream:\t\t\t{facecreamEntry.get()}\t\t\t{facecreamprice} Rs')
        if facewashEntry.get()!='0':
            textarea.insert(END,f'\nFace Wash:\t\t\t{facewashEntry.get()}\t\t\t{facewashprice} Rs')
        #textarea.insert(END,'\n------------------------------------------------------')
        # for grocery
        if riceEntry.get()!='0':
            textarea.insert(END,f'\nRice:\t\t\t{riceEntry.get()}\t\t\t{riceprice} Rs')
        if daalEntry.get()!='0':
            textarea.insert(END,f'\nDaal:\t\t\t{daalEntry.get()}\t\t\t{daalprice} Rs')
        if oilEntry.get()!='0':
            textarea.insert(END,f'\nOil:\t\t\t{oilEntry.get()}\t\t\t{oilprice} Rs')
        if sugarEntry.get()!='0':
            textarea.insert(END,f'\nSugar:\t\t\t{sugarEntry.get()}\t\t\t{sugarprice} Rs')
        if teaEntry.get()!='0':
            textarea.insert(END,f'\nTea:\t\t\t{teaEntry.get()}\t\t\t{teaprice} Rs')
        if WheatEntry.get()!='0':
            textarea.insert(END,f'\nWheat:\t\t\t{WheatEntry.get()}\t\t\t{wheatprice} Rs')
        #textarea.insert(END, '\n------------------------------------------------------')

# for Cold Drinks
        if MaazaEntry.get()!='0':
            textarea.insert(END,f'\nMaaza:\t\t\t{MaazaEntry.get()}\t\t\t{Maazaprice} Rs')
        if PepsiEntry.get()!='0':
            textarea.insert(END,f'\nPepsi:\t\t\t{PepsiEntry.get()}\t\t\t{Pepsiprice} Rs')
        if SpriteEntry.get()!='0':
            textarea.insert(END,f'\nSprite:\t\t\t{SpriteEntry.get()}\t\t\t{Spriteprice} Rs')
        if DewEntry.get()!='0':
            textarea.insert(END,f'\nDew:\t\t\t{DewEntry.get()}\t\t\t{Dewprice} Rs')
        if FrootiEntry.get()!='0':
            textarea.insert(END,f'\nFrooti:\t\t\t{FrootiEntry.get()}\t\t\t{Frootiprice} Rs')
        if CococolaEntry.get()!='0':
            textarea.insert(END,f'\nCoco Cola:\t\t\t{CococolaEntry.get()}\t\t\t{Cococolaprice} Rs')
        textarea.insert(END, '\n------------------------------------------------------')

        if cosmetictaxEntry.get()!='0.0 Rs':
            textarea.insert(END,f'\nCosmetic Tax :\t\t\t\t {cosmetictaxEntry.get()}')
        if grocerytaxEntry.get()!='0.0 Rs':
            textarea.insert(END,f'\nGrocery Tax :\t\t\t\t {grocerytaxEntry.get()}')
        if colddrinkstaxEntry.get()!='0.0 Rs':
            textarea.insert(END,f'\nCold Drinks Tax :\t\t\t\t {colddrinkstaxEntry.get()}')

        textarea.insert(END,f'\n\nTotal Bill:\t\t\t\tRs{totalbill}')
        textarea.insert(END, '\n------------------------------------------------------')

        save_bill()
def total():
    global soapprice,facecreamprice,facewashprice,hairsprayprice,hairgelprice,bodylotionprice
    global riceprice,daalprice,oilprice,sugarprice,teaprice,wheatprice
    global Maazaprice,Pepsiprice,Spriteprice,Dewprice,Frootiprice,Cococolaprice
    global totalbill

    #Cosmetic Price
    if bathsoapEntry.get().isdigit() and facecreamEntry.get().isdigit() and facewashEntry.get().isdigit()and hairsprayEntry.get().isdigit() and hairgelEntry.get().isdigit() and bodylotionEntry.get().isdigit():
        soapprice = int(bathsoapEntry.get()) * 20
        facecreamprice = int(facecreamEntry.get()) * 50
        facewashprice = int(facewashEntry.get()) * 100
        hairsprayprice = int(hairsprayEntry.get()) * 150
        hairgelprice = int(hairgelEntry.get()) * 80
        bodylotionprice = int(bodylotionEntry.get()) * 60
    else:
        messagebox.showerror('Error',"Quantity must contain integer only")


    totalcosmeticprice=soapprice+facecreamprice+facewashprice+hairsprayprice+hairgelprice+bodylotionprice
    cosmeticpriceEntry.delete(0,END)

    cosmeticpriceEntry.insert(0,f'Rs {totalcosmeticprice}')
     #12% tax
    cosmetictax=totalcosmeticprice*0.12
    cosmetictaxEntry.delete(0,END)
    cosmetictaxEntry.insert(0,'Rs '+str(round(cosmetictax,2)))

     #grocery Price

    if riceEntry.get().isdigit() and daalEntry.get().isdigit() and oilEntry.get().isdigit() and sugarEntry.get().isdigit() and teaEntry.get().isdigit() and WheatEntry.get().isdigit():
        riceprice = int(riceEntry.get()) * 30
        daalprice = int(daalEntry.get()) * 100
        oilprice = int(oilEntry.get()) * 120
        sugarprice = int(sugarEntry.get()) * 50
        teaprice = int(teaEntry.get()) * 148
        wheatprice = int(WheatEntry.get()) * 80
    else:
        messagebox.showerror('Error',"Quantity must contain integer only")

    totalgroceryprice=riceprice+daalprice+oilprice+sugarprice+teaprice+wheatprice
    grocerypriceEntry.delete(0,END)
    grocerypriceEntry.insert(0,f'Rs {totalgroceryprice}')

    grocerytax=totalgroceryprice*0.05
    grocerytaxEntry.delete(0,END)
    grocerytaxEntry.insert(0,'Rs '+str(round(grocerytax,2)))

    # colddrinks Price

    if MaazaEntry.get().isdigit() and PepsiEntry.get().isdigit() and SpriteEntry.get().isdigit() and DewEntry.get().isdigit() and FrootiEntry.get().isdigit() and CococolaEntry.get().isdigit():
        Maazaprice = int(MaazaEntry.get()) * 50
        Pepsiprice = int(PepsiEntry.get()) * 20
        Spriteprice = int(SpriteEntry.get()) * 30
        Dewprice = int(DewEntry.get()) * 20
        Frootiprice = int(FrootiEntry.get()) * 45
        Cococolaprice = int(CococolaEntry.get()) * 90
    else:
        messagebox.showerror('Error','Quantity must contain integer only')

    totalcolddrinksprice=Maazaprice+Pepsiprice+Spriteprice+Dewprice+Frootiprice+Cococolaprice
    colddrinkspriceEntry.delete(0,END)
    colddrinkspriceEntry.insert(0,f'Rs {totalcolddrinksprice}')

    colddrinkstax=totalcolddrinksprice*0.08
    colddrinkstaxEntry.delete(0,END)
    colddrinkstaxEntry.insert(0,'Rs '+str(round(colddrinkstax,2)))

    totalbill=totalcosmeticprice+totalgroceryprice+totalcolddrinksprice+cosmetictax+grocerytax+colddrinkstax

    save_to_excel(billnumber,nameEntry.get(), phoneEntry.get(), bathsoapEntry.get(),bodylotionEntry.get(),facewashEntry.get(),facecreamEntry.get(),hairsprayEntry.get(),hairgelEntry.get(),riceEntry.get(),oilEntry.get(),daalEntry.get(),WheatEntry.get(),sugarEntry.get(),teaEntry.get(),MaazaEntry.get(),PepsiEntry.get(),SpriteEntry.get(),DewEntry.get(),FrootiEntry.get(),CococolaEntry.get())
    messagebox.showinfo("Success","Data saved to Excel file")

#GUI part
# for creating window we have class inside tkinter module .That will help to creating Graphical user interface(GUI)  very easly we just need to create object of that class .

root=Tk() # creating object of class (TK) that present inside tkinter .help to creating a window

root.title('Retail Billing System') # giving title of the window
root.geometry('1270x685') # set size of window
root.iconbitmap('icon.ico') # set icon before title
headingLabel=Label(root,text='Retail Billing System',font=('times new roman',30,'bold'),bg='gray20',fg='gold',bd=12,relief=RIDGE) # creating a label
# bg: background color, fg: foreground/text color, bd:boader
headingLabel.pack(fill=X) # (show/place) the (label/ heading) at the top.

# ----------------Customer Details--------------

customer_details_frame=LabelFrame(root,text='customer Details',font=('times new roman',15,'bold'),fg='gold',bd=8,relief=GROOVE,bg='gray20') # creating customer Details frame
customer_details_frame.pack(fill=X)# use to display customer frame into the window but not able to see set position(usong grid) and build a label for this.

nameLabel=Label(customer_details_frame,text='Name',font=('times new roman',15,'bold'),bg='gray20',fg='white') # create label for customer details column
nameLabel.grid(row=0,column=0,padx=20) # set grid of that frame.

nameEntry=Entry(customer_details_frame,font=('arial',15),bd=7,width=18) # creating entry section of name
nameEntry.grid(row=0,column=1,padx=8) # set position.


phoneLabel=Label(customer_details_frame,text='Phone Number',font=('times new roman',15,'bold'),bg='gray20',fg='white') # create label for customer details column
phoneLabel.grid(row=0,column=2,padx=20,pady=2) # set grid of that frame.

phoneEntry=Entry(customer_details_frame,font=('arial',15),bd=7,width=18) # creating entry section of name
phoneEntry.grid(row=0,column=3,padx=8)

billnumberLabel=Label(customer_details_frame,text='Bill Number',font=('times new roman',15,'bold'),bg='gray20',fg='white') # create label for customer details column
billnumberLabel.grid(row=0,column=4,padx=20,pady=2) # set grid of that frame.
billnumberEntry=Entry(customer_details_frame,font=('arial',15),bd=7,width=18) # creating entry section of name
billnumberEntry.grid(row=0,column=5,padx=8)

searchButton=Button(customer_details_frame,text='SEARCH',font=('arial',12,'bold'),bd=7,width=10,command=search_bill)
searchButton.grid(row=0,column=6,padx=20,pady=8)

# ---main menu---(Cosmetics, Grocery, Cold Drinks and Bill Area)

productsFrame=Frame(root)
productsFrame.pack()

#-------1.Cosmetic Frame----------

cosmeticsFrame=LabelFrame(productsFrame,text='Cosmetics',font=('times new roman',15,'bold'),fg='gold',bd=8,relief=GROOVE,bg='gray20')
cosmeticsFrame.grid(row=0,column=0)

bathsoapLabel=Label(cosmeticsFrame,text='Bath Soap',font=('times new roman',15,'bold'),bg='gray20',fg='white')
bathsoapLabel.grid(row=0,column=0,pady=7,padx=10,sticky='w')
bathsoapEntry=Entry(cosmeticsFrame,font=('times new roman',15,'bold'),width=10,bd=5)
bathsoapEntry.grid(row=0,column=1,pady=7,padx=10)
bathsoapEntry.insert(0,0)

facecreamLabel=Label(cosmeticsFrame,text='Face cream',font=('times new roman',15,'bold'),bg='gray20',fg='white')
facecreamLabel.grid(row=1,column=0,pady=7,padx=10,sticky='w')
facecreamEntry=Entry(cosmeticsFrame,font=('times new roman',15,'bold'),width=10,bd=5)
facecreamEntry.grid(row=1,column=1,pady=7,padx=10)
facecreamEntry.insert(0,0)

facewashLabel=Label(cosmeticsFrame,text='Face Wash',font=('times new roman',15,'bold'),bg='gray20',fg='white')
facewashLabel.grid(row=2,column=0,pady=7,padx=10,sticky='w')
facewashEntry=Entry(cosmeticsFrame,font=('times new roman',15,'bold'),width=10,bd=5)
facewashEntry.grid(row=2,column=1,pady=7,padx=10)
facewashEntry.insert(0,0)

facecreamLabel=Label(cosmeticsFrame,text='Face cream',font=('times new roman',15,'bold'),bg='gray20',fg='white')
facecreamLabel.grid(row=3,column=0,pady=7,padx=10,sticky='w')
facecreamEntry=Entry(cosmeticsFrame,font=('times new roman',15,'bold'),width=10,bd=5)
facecreamEntry.grid(row=3,column=1,pady=7,padx=10)
facecreamEntry.insert(0,0)

hairsprayLabel=Label(cosmeticsFrame,text='Hair Spray',font=('times new roman',15,'bold'),bg='gray20',fg='white')
hairsprayLabel.grid(row=4,column=0,pady=7,padx=10,sticky='w')
hairsprayEntry=Entry(cosmeticsFrame,font=('times new roman',15,'bold'),width=10,bd=5)
hairsprayEntry.grid(row=4,column=1,pady=7,padx=10)
hairsprayEntry.insert(0,0)

hairgelLabel=Label(cosmeticsFrame,text='Hair Gel',font=('times new roman',15,'bold'),bg='gray20',fg='white')
hairgelLabel.grid(row=5,column=0,pady=7,padx=10,sticky='w')
hairgelEntry=Entry(cosmeticsFrame,font=('times new roman',15,'bold'),width=10,bd=5)
hairgelEntry.grid(row=5,column=1,pady=7,padx=10)
hairgelEntry.insert(0,0)

bodylotionLabel=Label(cosmeticsFrame,text='Body Lotion',font=('times new roman',15,'bold'),bg='gray20',fg='white')
bodylotionLabel.grid(row=1,column=0,pady=7,padx=10,sticky='w')
bodylotionEntry=Entry(cosmeticsFrame,font=('times new roman',15,'bold'),width=10,bd=5)
bodylotionEntry.grid(row=1,column=1,pady=7,padx=10)
bodylotionEntry.insert(0,0)

#-----------2.grocery---------------
groceryFrame=LabelFrame(productsFrame,text='Grocery',font=('times new roman',15,'bold') ,fg='gold',bd=8,relief=GROOVE,bg='gray20')
groceryFrame.grid(row=0,column=1)
riceLabel=Label(groceryFrame,text='Rice',font=('times new roman',15,'bold'),bg='gray20',fg='white')
riceLabel.grid(row=0,column=0,pady=7,padx=10,sticky='w')
riceEntry=Entry(groceryFrame,font=('times new roman',15,'bold'),width=10,bd=5)
riceEntry.grid(row=0,column=1,pady=7,padx=10)
riceEntry.insert(0,0)

oilLabel=Label(groceryFrame,text='oil',font=('times new roman',15,'bold'),bg='gray20',fg='white')
oilLabel.grid(row=1,column=0,pady=7,padx=10,sticky='w')
oilEntry=Entry(groceryFrame,font=('times new roman',15,'bold'),width=10,bd=5)
oilEntry.grid(row=1,column=1,pady=7,padx=10)
oilEntry.insert(0,0)

daalLabel=Label(groceryFrame,text='Daal',font=('times new roman',15,'bold'),bg='gray20',fg='white')
daalLabel.grid(row=2,column=0,pady=7,padx=10,sticky='w')
daalEntry=Entry(groceryFrame,font=('times new roman',15,'bold'),width=10,bd=5)
daalEntry.grid(row=2,column=1,pady=7,padx=10)
daalEntry.insert(0,0)

WheatLabel=Label(groceryFrame,text='Wheat',font=('times new roman',15,'bold') ,bg='gray20',fg='white')
WheatLabel.grid(row=3,column=0,pady=7,padx=10,sticky='w')
WheatEntry=Entry(groceryFrame,font=('times new roman',15,'bold'),width=10,bd=5)
WheatEntry.grid(row=3,column=1,pady=7,padx=10)
WheatEntry.insert(0,0)

sugarLabel=Label(groceryFrame,text='Sugar',font=('times new roman',15,'bold'),bg='gray20',fg='white')
sugarLabel.grid(row=4,column=0,pady=7,padx=10,sticky='w')
sugarEntry=Entry(groceryFrame,font=('times new roman',15,'bold'),width=10,bd=5)
sugarEntry.grid(row=4,column=1,pady=7,padx=10)
sugarEntry.insert(0,0)

teaLabel=Label(groceryFrame,text='Tea',font=('times new roman',15,'bold'),bg='gray20',fg='white')
teaLabel.grid(row=5,column=0,pady=7,padx=10,sticky='w')
teaEntry=Entry(groceryFrame,font=('times new roman',15,'bold'),width=10,bd=5)
teaEntry.grid(row=5,column=1,pady=7,padx=10)
teaEntry.insert(0,0)

#-----3.cold drinks---------
colddrinksFrame=LabelFrame(productsFrame,text='Cold Drinks',font=('times new roman',15,'bold'),fg='gold',bd=8,relief=GROOVE,bg='gray20')
colddrinksFrame.grid(row=0,column=2)

MaazaLabel=Label(colddrinksFrame,text='Maaza',font=('times new roman',15,'bold'),bg='gray20',fg='white')
MaazaLabel.grid(row=0,column=0,pady=7,padx=10,sticky='w')
MaazaEntry=Entry(colddrinksFrame,font=('times new roman',15,'bold'),width=10,bd=5)
MaazaEntry.grid(row=0,column=1,pady=7,padx=10)
MaazaEntry.insert(0,0)

PepsiLabel=Label(colddrinksFrame,text='Pepsi',font=('times new roman',15,'bold'),bg='gray20',fg='white')
PepsiLabel.grid(row=1,column=0,pady=7,padx=10,sticky='w')
PepsiEntry=Entry(colddrinksFrame,font=('times new roman',15,'bold'),width=10,bd=5)
PepsiEntry.grid(row=1,column=1,pady=7,padx=10)
PepsiEntry.insert(0,0)

SpriteLabel=Label(colddrinksFrame,text='Sprite',font=('times new roman',15,'bold') ,bg='gray20',fg='white')
SpriteLabel.grid(row=2,column=0,pady=7,padx=10,sticky='w')
SpriteEntry=Entry(colddrinksFrame,font=('times new roman',15,'bold'),width=10,bd=5)
SpriteEntry.grid(row=2,column=1,pady=7,padx=10)
SpriteEntry.insert(0,0)

DewLabel=Label(colddrinksFrame,text='Dew',font=('times new roman',15,'bold'),bg='gray20',fg='white')
DewLabel.grid(row=3,column=0,pady=7,padx=10,sticky='w')
DewEntry=Entry(colddrinksFrame,font=('times new roman',15,'bold'),width=10,bd=5)
DewEntry.grid(row=3,column=1,pady=7,padx=10)
DewEntry.insert(0,0)

FrootiLabel=Label(colddrinksFrame,text='Frooti',font=('times new roman',15,'bold'),bg='gray20',fg='white')
FrootiLabel.grid(row=4,column=0,pady=7,padx=10,sticky='w')
FrootiEntry=Entry(colddrinksFrame,font=('times new roman',15,'bold'),width=10,bd=5)
FrootiEntry.grid(row=4,column=1,pady=7,padx=10)
FrootiEntry.insert(0,0)

CococolaLabel=Label(colddrinksFrame,text='Coco cola',font=('times new roman',15,'bold') ,bg='gray20',fg='white')
CococolaLabel.grid(row=5,column=0,pady=7,padx=10,sticky='w')
CococolaEntry=Entry(colddrinksFrame,font=('times new roman',15,'bold'),width=10,bd=5)
CococolaEntry.grid(row=5,column=1,pady=7,padx=10)
CococolaEntry.insert(0,0)

billframe=Frame(productsFrame,bd=8,relief=GROOVE) # means billframe(new) is inside productframe
billframe.grid(row=0,column=3,padx=10)

billareaLabel=Label(billframe,text='Bill Area',font=('times new roman',12,'bold'),bd=7,relief=GROOVE)
billareaLabel.pack(fill=X)

scrollbar=Scrollbar(billframe,orient=VERTICAL)
scrollbar.pack(side=RIGHT,fill=Y)
textarea=Text(billframe,height=18,width=55,yscrollcommand=scrollbar.set)
textarea.pack()
scrollbar.config(command=textarea.yview)

billmenuFrame=LabelFrame(root,text='Bill Menu',font=('times new roman',13,'bold'),fg='gold',bd=8,relief=GROOVE,bg='gray20')
billmenuFrame.pack()

cosmeticpriceLabel=Label(billmenuFrame,text='Cosmetic Price',font=('times new roman',13,'bold'),bg='gray20',fg='white')
cosmeticpriceLabel.grid(row=0,column=0,pady=5,padx=10,sticky='w')
cosmeticpriceEntry=Entry(billmenuFrame,font=('times new roman',13,'bold'),width=10,bd=5)
cosmeticpriceEntry.grid(row=0,column=1,pady=5,padx=10)
#cosmeticpriceEntry.config(state="disable")

grocerypriceLabel=Label(billmenuFrame,text='Grocery Price',font=('times new roman',13,'bold') ,bg='gray20',fg='white')
grocerypriceLabel.grid(row=1,column=0,pady=5,padx=10,sticky='w')
grocerypriceEntry=Entry(billmenuFrame,font=('times new roman',13,'bold'),width=10,bd=5)
grocerypriceEntry.grid(row=1,column=1,pady=5,padx=10)
#grocerypriceEntry.config(state="disable")

colddrinkspriceLabel=Label(billmenuFrame,text='Cold Drink  Price',font=('times new roman',13,'bold'),bg='gray20',fg='white')
colddrinkspriceLabel.grid(row=2,column=0,pady=5,padx=10,sticky='w')
colddrinkspriceEntry=Entry(billmenuFrame,font=('times new roman',13,'bold'),width=10,bd=5)
colddrinkspriceEntry.grid(row=2,column=1,pady=5,padx=10)
#colddrinkspriceEntry.config(state="disable")

cosmetictaxLabel=Label(billmenuFrame,text='Cosmetic Tax',font=('times new roman',13,'bold'),bg='gray20',fg='white')
cosmetictaxLabel.grid(row=0,column=2,pady=5,padx=10,sticky='w')
cosmetictaxEntry=Entry(billmenuFrame,font=('times new roman',13,'bold'),width=10,bd=5)
cosmetictaxEntry.grid(row=0,column=3,pady=5,padx=10)
#cosmetictaxEntry.config(state="disable")

grocerytaxLabel=Label(billmenuFrame,text='Grocery Tax',font=('times new roman',13,'bold') ,bg='gray20',fg='white')
grocerytaxLabel.grid(row=1,column=2,pady=5,padx=10,sticky='w')
grocerytaxEntry=Entry(billmenuFrame,font=('times new roman',13,'bold'),width=10,bd=5)
grocerytaxEntry.grid(row=1,column=3,pady=5,padx=10)
#grocerytaxEntry.config(state="disable")

colddrinkstaxLabel=Label(billmenuFrame,text='Cold Drink Tax',font=('times new roman',13,'bold'),bg='gray20',fg='white')
colddrinkstaxLabel.grid(row=2,column=2,pady=5,padx=10,sticky='w')
colddrinkstaxEntry=Entry(billmenuFrame,font=('times new roman',13,'bold'),width=10,bd=5)
colddrinkstaxEntry.grid(row=2,column=3,pady=5,padx=10)
#colddrinkstaxEntry.config(state="disable")

buttonFrame=Frame(billmenuFrame,bd=8,relief=GROOVE)
buttonFrame.grid(row=0,column=4,rowspan=3)

totalButton=Button(buttonFrame,text='Total',font=('arial',16,'bold'),bg='gray20',fg='white',bd=5,width=8,pady=10,command=total)
totalButton.grid(row=0,column=0,pady=20,padx=5)

billButton=Button(buttonFrame,text='Bill',font=('arial',16,'bold'),bg='gray20',fg='white',bd=5,width=8,pady=10,command=bill)
billButton.grid(row=0,column=1,pady=20,padx=5)

emailButton=Button(buttonFrame,text='Email',font=('arial',16,'bold'),bg='gray20',fg='white',bd=5,width=8,pady=10,command=send_email)
emailButton.grid(row=0,column=2,pady=20,padx=5)

printButton=Button(buttonFrame,text='Print',font=('arial',16,'bold'),bg='gray20',fg='white',bd=5,width=8,pady=10,command=print_bill)
printButton.grid(row=0,column=3,pady=20,padx=5)

clearButton=Button(buttonFrame,text='Clear',font=('arial',16,'bold'),bg='gray20',fg='white',bd=5,width=8,pady=10,command=clear)
clearButton.grid(row=0,column=4,pady=20,padx=5)

root.mainloop() # this will help in viewing our window