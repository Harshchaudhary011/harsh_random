import os

import InvoiceGenerator
from InvoiceGenerator.api import Invoice, Item, Client, Provider, Creator

from InvoiceGenerator.pdf import SimpleInvoice

# choosing English as the document language
from tensorboard import summary

InvoiceGenerator.api.Address(summary, city='Noida', logo_filename=r'C:\Users\dell\Downloads\mykletricate.jfif')


os.environ["INVOICE_LANG"] = "en"

client = Client('Client company')

client= Client('HARSH')
client= Client('HARSH')
provider = Provider('MYK LATRICATE', bank_account='6454-6361-217273', bank_code='2021')

creator = Creator('Karl Iris')

invoice = Invoice(client, provider, creator)


#tiles
p = input('Is Tile Work Done(YES OR NO)')
if p == "YES":
    floor_area = input('Enter the floor area')

   #tiles dismantling work

    q = input('Dismantling of Old Tiles Required(YES OR NO)')

    if q == 'YES':

        tiles_dismentle_cost = input('Cost for Tiles Dismentle Work')
        invoice.add_item(Item(tiles_dismentle_cost, 1, description="Tiles Dismantle Work"))

    #Floor levelling work

    levelling_loading_charges =input('Enter loading charges for floor levelling')

    invoice.add_item(Item(floor_area,55, description="Floor Levelling"))

    invoice.add_item(Item(levelling_loading_charges, 1, description="Loading/Unloading Charges"))

    r = input('Is Tile Fixing Work Done(YES OR NO)')
    if r == 'YES':
        s = input('Enter Area for Tile Fixing')
        invoice.add_item(Item(s, 5, description="Tile Installtion Base Rate"))

        t = input('Enter Extra Average Amount for Tile Fixing')
        invoice.add_item(Item(t, 1, description="Extra Average Amount for Tile Fixing"))

    u = input('Is Squirting Work Done(YES OR NO)')
    if u == 'YES':
        invoice.add_item(Item(t, 1, description="Squirting Base Rate"))




    #invoice.add_item(Item(floor_area*55 +levelling_loading_charges, 1, description="Total Floor Levelling Charge"))

    #tile fixing on floor





invoice.currency = "Rs."

invoice.number = "10393069"

docu = SimpleInvoice(invoice)
print(docu.gen("invoice2.pdf", generate_qr_code=False))

docu = docu.gen("invoice2.pdf", generate_qr_code=False) #you can put QR code by setting the #qr_code parameter to ‘True’
print(docu)
#docu.gen("invoice.xml") ## We can also generate an XML file of this invoice