import pandas as pd
from datetime import datetime, date
from pyinvoice.models import InvoiceInfo, ServiceProviderInfo, ClientInfo, Item, Transaction
from pyinvoice.templates import SimpleInvoice
import streamlit as st


sheet_url = "https://docs.google.com/spreadsheets/d/1VOlggXzc2y9bonMI876Z1xNiyYHqWqULNyCFj93AOJA/edit?resourcekey#gid=1246927422"

url_1 = sheet_url.replace("/edit?resourcekey#gid=", "/export?format=csv&gid=")
df = pd.read_csv(url_1)

# client_data = df.iloc[-1]




doc = SimpleInvoice('invoice_new_lib.pdf')




def invo_generate(floor_area,loading_charge_floor_leveling,Extra_average_amount,x,y,z,t):
    doc.invoice_info = InvoiceInfo(1023, datetime.now(), datetime.now())  # Invoice info, optional

    # Service Provider Info, optional
    doc.service_provider_info = ServiceProviderInfo(
        name='MYTK LATRICATE',
        street='NOIDA',
        # city='My City',
        # state='My State',
        # country='My Country',
        post_code='222222',
        vat_tax_number='Vat/Tax number'
    )

    # Client info, optional
    # doc.client_info = ClientInfo(name=client_data['NAME of CLient?'],email='client@example.com')

    # Add Item
    doc.add_item(Item('Tile Dismentle', 'Item desc', floor_area, '50'))
    doc.add_item(Item('Loading/Unloading Charges', 'Item desc', loading_charge_floor_leveling, '2.2'))
    doc.add_item(Item('Tile Installation', 'Item desc', floor_area, '100'))
    doc.add_item(Item('Extra average amount', 'Item desc', Extra_average_amount, '3.3'))

    if x == 'YES':
        doc.add_item(Item('Tile Dismentle(ROOM2)', 'Item desc', y, '50'))
        doc.add_item(Item('Loading/Unloading Charges(ROOM2)', 'Item desc', z, '2.2'))
        doc.add_item(Item('Tile Installation(ROOM2)', 'Item desc', y, '100'))
        doc.add_item(Item('Extra average amount(ROOM2)', 'Item desc', t, '3.3'))

    # Tax rate, optional
    doc.set_item_tax_rate(18)  # 20%

    # Transactions detail, optional
    # doc.add_transaction(Transaction('Paypal', 111, datetime.now(), 1))
    # doc.add_transaction(Transaction('Stripe', 222, date.today(), 2))

    # Optional
    doc.set_bottom_tip("Email: example@example.com<br />Don't hesitate to contact us for any questions.")
    doc.finish()


    return doc






def main():

    st.title("Invoice Generator")
    html_temp = """
        <div style="background-color:tomato;padding:10px">
        <h2 style="color:white;text-align:center;">Streamlit Bill Generator Web App </h2>
        </div>
        """

    st.markdown(html_temp, unsafe_allow_html=True)
    floor_area = st.text_input("Enter floor area")
    loading_charge_floor_leveling = st.text_input("Enter Loading Charge")
    Extra_average_amount = st.text_input("Extra Average Amount ")

    x = st.text_input("Enter Data for Second Room?(YES/NO)",'Type')


    if x == 'YES':
        y = st.text_input("Enter floor area(ROOM2)", "Type Here")
        z= st.text_input("Enter Loading Charge(ROOM2)", "Type Here")
        t= st.text_input("Extra Average Amount(ROOM2)", "Type Here")

        if st.button("Generate"):
            invo_generate(floor_area, loading_charge_floor_leveling, Extra_average_amount, x, y, z, t)
            st.title("Bill is saved in your local directory")


    elif st.button('Generate'):
        (y,z,t)=(0,0,0)
        invo_generate(floor_area, loading_charge_floor_leveling, Extra_average_amount,x,y,z,t)
        st.title("Bill is saved in your local directory")



    # entropy = st.text_input("entropy","Type Here")
    result = ""
    # if st.button("Generate"):
    #     r = invo_generate(floor_area, loading_charge_floor_leveling, Extra_average_amount)

        # result = create_download_link(r)


        # PDFbyte = r.read()
        # print(PDFbyte)

    # if st.download_button(
    #  label="Download data as pdf",
    #  data=invo_generate(floor_area,loading_charge_floor_leveling,Extra_average_amount),
    #  file_name='large_df.pdf',mime='pdf')

    # st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("Lets LEarn")
        st.text("Built with Streamlit")


if __name__=='__main__':
    main()